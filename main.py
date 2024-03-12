import json
from copy import deepcopy


def create_weights(optimization_param: list):  # возвращает три переменные - веса. В порядке - время, деньги, ресурсы
    dict_of_params = {'time': 0, 'money': 0, 'resource': 0}

    if not(0 < len(optimization_param) < 4):
        raise Exception('incorrect input data format')
    for temp in optimization_param:
        if temp not in dict_of_params:
            raise Exception('incorrect input data format')
    if not(len(optimization_param) == len(set(optimization_param))):
        raise Exception('incorrect input data format')

    if len(optimization_param) == 1:
        dict_of_params[optimization_param[0]] = 2 # коэффициент для значения, по которому идет оптимизация, в случае если передали одно значение
    if len(optimization_param) == 2:
        dict_of_params[optimization_param[0]] = 1.5 # коэффициент для 1-го значения, по которому идет оптимизация, в случае если передали два значения
        dict_of_params[optimization_param[1]] = 0.5 # коэффициент для 2-го значения, по которому идет оптимизация, в случае если передали два значения
    if len(optimization_param) == 3:
        dict_of_params[optimization_param[0]] = 1 # коэффициент для 1-го значения, по которому идет оптимизация, в случае если передали три значения
        dict_of_params[optimization_param[1]] = 0.6 # коэффициент для 2-го значения, по которому идет оптимизация, в случае если передали три значения
        dict_of_params[optimization_param[2]] = 0.4 # коэффициент для 3-го значения, по которому идет оптимизация, в случае если передали три значения

    return dict_of_params['time'], dict_of_params['money'], dict_of_params['resource']


def load_input_json(file_name: str) -> dict:  # принимает название файла, возвращает его в виде словаря
    with open('data_json.json', 'r', encoding='utf-8') as file:
        return json.load(file)



def get_data_from_json(
        project_data: dict):  # принимает json в виде словаря. Возвращает данные о проекте, данные о сотрудниках, календарь, зависимости, связи задач и разработчиков. Именно в таком порядке
    return [[[0, 40, '7332181498130530308', 'Аналитика'], [40, 120, "7332181498130530309", 'Разработка'],
             [120, 160, "7332181498130530310", 'Тестирование'], [2000, "7332176661559640067"],
             [2000, "7332176511673499649"], [1500, "7332183950556856321"], "7332181498130530307"],
            [[0, 80, '7332181498130530312', 'Аналитика'], [80, 240, "7332181498130530313", 'Разработка'],
             [240, 320, "7332181498130530314", 'Тестирование'], [2000, "7332176661559640067"],
             [4000, "7332176618609967105"], [3000, "7332176618609967105"], "7332181498130530311"],
            [[0, 120, '7332181498130530308', 'Аналитика'], [120, 360, "7332181498130530309", 'Разработка'],
             [360, 480, "7332181498130530310", 'Тестирование'], [2000, "7332176661559640067"],
             [4000, "7332176571803041799"], [1500, "7332183950556856321"], "7332181498130530315"]], [
               {"projectRoleId": "tester", 'salary': 1000, "id": "7332176730716831745"},
               {"projectRoleId": "tester", 'salary': 1500, "id": "7332183950556856321"},
               {"projectRoleId": "developer", 'salary': 2000, "id": "7332176511673499649"},
               {"projectRoleId": "developer", 'salary': 3000, "id": "7332176618609967105"},
               {"projectRoleId": "analyst", 'salary': 2000, "id": "7332176661559640067"},
               {"projectRoleId": "developer", 'salary': 4000, "id": "7332176571803041799"}], data['calendars'], {
               "7332181498130530308": '7332181498130530309', '7332181498130530309': '7332181498130530310',
               '7332181498130530312': '7332181498130530313', '7332181498130530313': '7332181498130530314',
               '7332181498130530316': '7332181498130530317', '7332181498130530317': '7332181498130530318'}, data['assignments']


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


def optimization_by_weights(
        project: list) -> list:  # Принимает оптимизированные проект, с расставленными работниами. Оптимизирует его по оставщимся двум параметрам и возвращает.
    global time_index, money_index, resurces_index, dependencies
    count_projects = (len(project[0]) - 1) // 2
    data_set = [project]
    for i in range(1, len(project)):
        project_moved = deepcopy(project)
        for j in range(count_projects):
            print(project_moved[i][j][0], project_moved[i - 1][j][1])
            if project_moved[i][j][0] > project_moved[i - 1][j][0] and project_moved[i][j][0] < project_moved[i - 1][j][
                1]:
                time = abs(project_moved[i][j][0] - project_moved[i - 1][j][1]) * time_index
                time_dif = abs(project_moved[i][j][0] - project_moved[i - 1][j][1])
                salary_1 = project_moved[i][j + count_projects][0]
                salary_2 = project_moved[i - 1][j + count_projects][0]
                salary = abs(salary_1 - salary_2) / 1000 * time_dif * money_index
                resurce = resurces_index
                task_id = project_moved[i][j][2]
                if max(resurce, salary) > time:
                    project_moved[i][j][1] += project_moved[i][j][1] - project_moved[i][j][0]
                    project_moved[i][j][0] = project_moved[i - 1][j][1]
                    if salary_1 > salary_2:
                        project_moved[i][j + count_projects][0] = salary_2
                        project_moved[i][j + count_projects][1] = \
                            project_moved[i - 1][j + count_projects][1]
                        for k in project_moved[i][j + 1:count_projects]:
                            print(task_id, dependencies)
                            if task_id in dependencies:
                                if dependencies[task_id] == k[2]:
                                    print(k)
                    else:
                        project_moved[i - 1][j + count_projects][0] = salary_1
                        project_moved[i - 1][j + count_projects][1] = \
                            project_moved[i][j + count_projects][0]
                    print(project_moved)
                else:
                    continue
            else:
                continue


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
    write_project_into_json(final_project)
