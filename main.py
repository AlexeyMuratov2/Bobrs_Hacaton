from data import data  # пока данные подтягиваем так, потом добавим функцию


def create_weights(optimization_param: list):  # возвращает три переменные - веса. В порядке - время, деньги, ресурсы
    return 2, 1, 0.5


def load_input_json(file_name: str) -> dict:  # принимает название файла, возвращает его в виде словаря
    return data


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
               {"projectRoleId": "developer", 'salary': 4000, "id": "7332176571803041799"}], data['calendars'], data[
               'dependencies'], data['assignments']

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
        return [[[0, 120, '7332181498130530316', 'Аналитика'], [120, 360, "7332181498130530317", 'Разработка'],
             [360, 480, "7332181498130530318", 'Тестирование'], [2000, "7332181498130530315"],
             [2000, "7332176511673499649"], [1500, "7332183950556856321"], "7332181498130530315"],
            [[120, 200, '7332181498130530312', 'Аналитика'], [200, 360, "7332181498130530313", 'Разработка'],
             [360, 440, "7332181498130530314", 'Тестирование'], [2000, "7332176661559640067"],
             [4000, "7332176618609967105"], [3000, "7332176618609967105"], "7332181498130530311"],
            [[200, 240, '7332181498130530308', 'Аналитика'], [240, 320, "7332181498130530309", 'Разработка'],
             [320, 360, "7332181498130530310", 'Тестирование'], [2000, "7332176661559640067"],
             [4000, "7332176571803041799"], [1500, "7332183950556856321"], "7332181498130530307"]]

    def write_project_into_json(
            project: list) -> None:  # Принимает проект и записывает новые данные в словарь data. Записывает его в файл и выводит сообщением общие затраты, время и ресурсы.
        pass

    def main():
        input_values = []  # передать список параметров
        time_index, money_index, resurces_index = create_weights(input_values)
        data = load_input_json(str(input('введите название файла: ')))  # открыть, когда будет реализована функция
        project, resurces, calendars, dependencies, assignments = get_data_from_json(data)
        max_working_hours = get_max_working_hours(calendars)  # пока не делаем
        optimized_by_time_project = optimization_by_time(project)
        optimized_by_time_and_money_project = set_workers(optimized_by_time_project)
        final_project = optimization_by_weights(optimized_by_time_and_money_project)
        write_project_into_json(final_project)

    if __name__ == '__main__':
        main()
