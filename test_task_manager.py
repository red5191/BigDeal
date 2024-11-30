from task_manager import TaskManager

manager2 = TaskManager()

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
        raise AssertionError('Ошибка: Задание не было удалено')
    except IndexError:
        pass

    print('Все тесты пройдены.')


test_task_manager(manager2)