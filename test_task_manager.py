import json

from task_manager import TaskManager

test_manager = TaskManager()

def test_task_manager(manager):
    manager.add_task('DO IT')
    try:
        manager.get_list()[0]
    except IndexError:
        raise AssertionError('Ошибка: Задание не было создано')

    manager.complete_task(0)
    assert manager.get_list()[0]['completed'] == True,'Ошибка: Задание не отмечено выполненым'

    manager.add_task('JUST DO IT')
    manager.remove_task(1)
    try:
        manager.get_list()[1]
        raise AssertionError('Ошибка: Задание не было удалено.')
    except IndexError:
        pass

    manager.save_to_json('test.json')
    try:
        with open('test.json', 'r') as file:
            test_file = json.load(file)
    except FileNotFoundError:
        raise AssertionError('Ошибка: файл json не был создан.')

    manager.load_from_json('test.json')
    try:
        with open('test.json', 'r') as file:
            test_from_file = json.load(file)
            assert len(test_from_file) != 0, "Ошибка: файл json содержит пустой список"
    except FileNotFoundError:
        raise AssertionError('Ошибка: файл json не найден')

    print('Все тесты пройдены.')


test_task_manager(test_manager)