import json
import re
from copy import deepcopy


def create_weights(optimization_param: list):  # возвращает три переменные - веса. В порядке - время, деньги, ресурсы
    dict_of_params = {'time': 0, 'money': 0, 'resource': 0}

    if not (0 < len(optimization_param) < 4):
        raise Exception('incorrect input data format')
    for temp in optimization_param:
        if temp not in dict_of_params:
            raise Exception('incorrect input data format')
    if not (len(optimization_param) == len(set(optimization_param))):
        raise Exception('incorrect input data format')

    if len(optimization_param) == 1:
        dict_of_params[optimization_param[
            0]] = 2  # коэффициент для значения, по которому идет оптимизация, в случае если передали одно значение
    if len(optimization_param) == 2:
        dict_of_params[optimization_param[
            0]] = 1.5  # коэффициент для 1-го значения, по которому идет оптимизация, в случае если передали два значения
        dict_of_params[optimization_param[
            1]] = 1  # коэффициент для 2-го значения, по которому идет оптимизация, в случае если передали два значения
    if len(optimization_param) == 3:
        dict_of_params[optimization_param[
            0]] = 1  # коэффициент для 1-го значения, по которому идет оптимизация, в случае если передали три значения
        dict_of_params[optimization_param[
            1]] = 0.6  # коэффициент для 2-го значения, по которому идет оптимизация, в случае если передали три значения
        dict_of_params[optimization_param[
            2]] = 0.4  # коэффициент для 3-го значения, по которому идет оптимизация, в случае если передали три значения

    return dict_of_params['time'], dict_of_params['money'], dict_of_params['resource']


def load_input_json(file_name: str) -> dict:  # принимает название файла, возвращает его в виде словаря
    with open('data_json.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def projects(list_projects):
    list_of_proj = []

    for row in list_projects:
        for values in row['rows']:
            for child in values['children']:
                for proj_data in child.keys():

                    if proj_data == 'children':

                        for part_proj in child[proj_data]:
                            parts_pr = []
                            for items in part_proj.keys():

                                if items == 'name' or items == 'effort' or items == 'id' or items == 'parentId':
                                    parts_pr.append(part_proj[items])
                            list_of_proj.append(parts_pr)

    return list_of_proj


def depend(list_depend):
    depend_list = []
    for line in list_depend:
        if 'rows' in line:
            for item in line['rows']:
                depend = []
                for key in item.keys():
                    if key == 'from' or key == 'to':
                        depend.append(item[key])
                depend_list.append(depend)
    return depend_list


def resources(list_workers):
    workers = []

    for line in list_workers:
        if 'rows' in line:
            for item in line['rows']:
                worker = {}
                for key in item.keys():
                    if key == 'projectRoleId' or key == 'id':
                        worker[key] = item[key]
                    elif key == 'name':
                        match = re.search(r'\((\d+)\D', str(item[key]))

                        if match:
                            worker['salary'] = int(match.group(1))

                workers.append(worker)
    return workers


def events_dis(list_events):
    events = []
    event = []

    for line in list_events:
        if 'rows' in line:
            for item in line['rows']:
                event = []
                for key in item.keys():
                    if key == 'event' or key == 'resource':
                        event.append(item[key])
                events.append(event)
    return events


def search_id(id, time, projects_final, depend_dict):
    for project in projects_final:
        for item in project:
            for k in depend_dict.keys():
                for i in range(len(item)):
                    if k == id and depend_dict[k] == item[i]:
                        item[0] = item[0] + time
                        item.insert(0, time)
                        break


def get_data_from_json(
        project_data: dict):  # принимает json в виде словаря. Возвращает данные о проекте, данные о сотрудниках, календарь, зависимости, связи задач и разработчиков. Именно в таком порядке
    list_projects = []
    list_people = []
    list_events = []
    list_depend = []
    dict_calendar = {}

    for keys in data.keys():
        if keys == 'tasks':
            list_projects.append(data[keys])
        elif keys == 'resources':
            list_people.append(data[keys])
        elif keys == 'assignments':
            list_events.append(data[keys])
        elif keys == 'dependencies':
            list_depend.append(data[keys])
        elif keys == 'calendars':
            dict_calendar = data[keys]

    list_projects = projects(list_projects)
    list_people = resources(list_people)
    list_events = events_dis(list_events)
    list_depend = depend(list_depend)

    dict_proj = {}

    for item in list_projects:
        if item[0] in dict_proj.keys():
            dict_proj[item[0]].append(item[1:])
        else:
            dict_proj[item[0]] = [item[1:]]

    dict_events_inside = {}

    for item in list_people:
        for id in list_events:
            if id[1] == item['id']:
                dict_events_inside[id[0]] = [item['salary'], item['id']]

                # теперь преобразую словарь событий в нужный для выгрузки вид

    list_events_out = []
    for item in list_events:
        dict_events_out = {}
        dict_events_out['event'] = item[0]
        dict_events_out['resource'] = item[1]
        list_events_out.append(dict_events_out)

    depend_dict = {}

    for item in list_depend:
        depend_dict[item[0]] = item[1]

    projects_final = []

    for k, v in dict_proj.items():
        parts = v.copy()
        for part in v:
            if part[2] in dict_events_inside.keys():
                parts.append(dict_events_inside[part[2]])
        parts.append(k)
        projects_final.append(parts)

    for project in projects_final:
        for i, item in enumerate(project):
            if isinstance(item, list) and len(item) == 3:
                project[i] = [item[1], item[2], item[0]]

    for project in projects_final:
        time = 0
        for item in project:
            for i in range(len(item)):
                if item[i] in depend_dict.keys() and item[i] not in depend_dict.values():
                    time = item[i - 1]
                    search_id(item[i], time, projects_final, depend_dict)
                    item.insert(0, 0)
                    break
                else:
                    if item[i] in depend_dict.keys():
                        time = item[i - 1]
                        search_id(item[i], time, projects_final, depend_dict)
                        break
    return projects_final, list_people, dict_calendar, depend_dict, list_events_out


def get_max_working_hours(
        calendar: dict) -> int:  # Принимает календарь, возвращает число - количество рабочих часов
    return 1000000


def optimization_by_time(
        project: list) -> list:  # Принимает данные о входном проект, оптимизирует их и возвращает (не вызывать, если вес time = 0)
    return [[[0, 120, '7332181498130530316', 'Аналитика'], [120, 360, "7332181498130530317", 'Разработка'],
             [360, 480, "7332181498130530318", 'Тестирование'], [2000, "7332181498130530315"],
             [2000, "7332176511673499649"], [1500, "7332183950556856321"], "7332181498130530315"],
            [[120, 200, '7332181498130530312', 'Аналитика'], [200, 360, "7332181498130530313", 'Разработка'],
             [360, 440, "7332181498130530314", 'Тестирование'], [2000, "7332176661559640067"],
             [4000, "7332176618609967105"], [3000, "7332176618609967105"], "7332181498130530311"],
            [[200, 240, '7332181498130530308', 'Аналитика'], [240, 320, "7332181498130530309", 'Разработка'],
             [320, 360, "7332181498130530310", 'Тестирование'], [2000, "7332176661559640067"],
             [4000, "7332176571803041799"], [1500, "7332183950556856321"], "7332181498130530307"]]


def set_workers(
        project: list) -> list:  # Приинимает проект, оптимизированные по времени. Назначает на него сотрудников, а именно расставляет в списке их зарплаты. Затем возвращает результат
    return [[[0, 120, '7332181498130530316', 'Аналитика'], [120, 360, "7332181498130530317", 'Разработка'],
             [360, 480, "7332181498130530318", 'Тестирование'], [2000, "7332181498130530315"],
             [2000, "7332176511673499649"], [1500, "7332183950556856321"], "7332181498130530315"],
            [[120, 200, '7332181498130530312', 'Аналитика'], [200, 360, "7332181498130530313", 'Разработка'],
             [360, 440, "7332181498130530314", 'Тестирование'], [2000, "7332176661559640067"],
             [4000, "7332176618609967105"], [3000, "7332176618609967105"], "7332181498130530311"],
            [[200, 240, '7332181498130530308', 'Аналитика'], [240, 320, "7332181498130530309", 'Разработка'],
             [320, 360, "7332181498130530310", 'Тестирование'], [2000, "7332176661559640067"],
             [4000, "7332176571803041799"], [1500, "7332183950556856321"], "7332181498130530307"]]


def choose_best_project(projects_list:list):
    global time_index, money_index, resurces_index
    time_index_set = []
    money_index_set = []
    resurces_index_set = []
    count_projects = len(projects_list[0])
    for i in range(len(projects_list)):
        money = 0
        time = 0
        resurces_set = set()
        for j in range(count_projects):
            for k in range((len(projects_list[i][j])-1)//2):
                print(projects_list[i][j][k])
                money += (projects_list[i][j][k][1] - projects_list[i][j][k][0]) * projects_list[i][j][k+count_projects][0]
                time = max(time, projects_list[i][j][k][1])
                resurces_set.add(projects_list[i][j][k+count_projects][1])
        print(len(resurces_set))
        time_index_set.append(time)
        money_index_set.append(money)
        resurces_index_set.append(len(resurces_set))
    best_option = 999999999999
    best_option_id = 0
    for i in range(len(time_index_set)):
        index = (time_index_set[i]*time_index)+(money_index_set[i]*money_index)+(resurces_index_set[i]*1000*resurces_index)
        if best_option > index:
            best_option = index
            best_option_id = i
    return projects_list[best_option_id]







def optimization_by_weights(
        project: list) -> list:  # Принимает оптимизированные проект, с расставленными работниами. Оптимизирует его по оставщимся двум параметрам и возвращает.
    global time_index, money_index, resurces_index, dependencies
    count_projects = len(project)
    data_set = [deepcopy(project)]
    project_moved = deepcopy(project)
    for i in range(1, count_projects):
        for j in range(count_projects):
            if project_moved[i][j][0] > project_moved[i - 1][j][0] and project_moved[i][j][0] < project_moved[i - 1][j][
                1]:
                time = abs(project_moved[i][j][0] - project_moved[i - 1][j][1]) * time_index
                time_dif = abs(project_moved[i][j][0] - project_moved[i - 1][j][1])
                salary_1 = project_moved[i][j + count_projects][0]
                salary_2 = project_moved[i - 1][j + count_projects][0]
                salary = abs(salary_1 - salary_2) / 1000 * time_dif * money_index
                resurce = resurces_index
                print(time, salary, resurce)
                print(time_dif)
                if max(resurce, salary) > time:
                    project_moved[i][j][1] += time_dif
                    project_moved[i][j][0] = project_moved[i - 1][j][1]
                    if salary_1 > salary_2:
                        project_moved[i][j + count_projects][0] = salary_2
                        project_moved[i][j + count_projects][1] = \
                            project_moved[i - 1][j + count_projects][1]
                        for k in range(j+1, count_projects):
                            dep_task_id = project_moved[i][k-1][2]
                            if dep_task_id in dependencies:
                                if dependencies[dep_task_id] == project_moved[i][k][2]:
                                    project_moved[i][k][0] += time_dif
                                    project_moved[i][k][1] += time_dif
                                    if project_moved[i - 1][k][0] <= project_moved[i][k][0]:
                                        if project_moved[i][k + count_projects][0] < \
                                                project_moved[i - 1][k + count_projects][0]:
                                            project_moved[i - 1][k + count_projects][0] = \
                                            project_moved[i][k + count_projects][0]
                                            project_moved[i - 1][k + count_projects][1] = \
                                            project_moved[i][k + count_projects][1]
                                        else:
                                            project_moved[i][k + count_projects][0] = \
                                            project_moved[i - 1][k + count_projects][0]
                                            project_moved[i][k + count_projects][1] = \
                                            project_moved[i - 1][k + count_projects][1]
                        # проверить на проектах, в которых больше трех задач
                        for k in range(i + 1, count_projects):
                            for h in range(j, len(project_moved[k])-count_projects-1):
                                project_moved[k][h][0] += time_dif
                                project_moved[k][h][1] += time_dif
                    else:
                        project_moved[i - 1][j + count_projects][0] = salary_1
                        project_moved[i - 1][j + count_projects][1] = \
                            project_moved[i][j + count_projects][0]
                    data_set.append(deepcopy(project_moved))
                else:
                    continue
            else:
                continue
    return choose_best_project(data_set)
    #return choose_best_project(set_workers(data_set))


def write_project_into_json(
        project: list) -> None:  # Принимает проект и записывает новые данные в словарь data. Записывает его в файл и выводит сообщением общие затраты, время и ресурсы.
    pass


if __name__ == '__main__':
    input_values = ['money']  # передать список параметров
    time_index, money_index, resurces_index = create_weights(input_values)
    data = load_input_json(str(input('введите название файла: ')))  # открыть, когда будет реализована функция
    project, resurces, calendars, dependencies, assignments = get_data_from_json(data)
    max_working_hours = get_max_working_hours(calendars)  # пока не делаем
    optimized_by_time_project = optimization_by_time(project)
    optimized_by_time_and_money_project = set_workers(optimized_by_time_project)
    final_project = optimization_by_weights(optimized_by_time_and_money_project)
    print(final_project)
    write_project_into_json(final_project)
    print(calendars)
