class TaskManager():
    def __init__(self):
        self.tasklist = []
        self.task = {}

    def add_task(self, description : str):
        self.task = {'description' : description, 'completed' : False}
        self.tasklist.append(self.task)

    def complete_task(self, index: int):
        try:
            self.tasklist[index]['completed'] = True
        except (IndexError, TypeError):
            print('Задача не найдена')

    def remove_task(self, index: int):
        try:
            del self.tasklist[index]
        except (IndexError, TypeError):
            print('Задача не найдена')


    # def save_to_json(self, filename: str)
    #
    # def load_from_json(self, filename: str)

man1 = TaskManager()

man1.add_task(12345)
man1.complete_task(1)
man1.remove_task('fdgv')