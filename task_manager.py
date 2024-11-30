import json


class TaskManager():
    def __init__(self):
        self.tasklist = []
        self.task = {}

    def add_task(self, description : str):
        for self.task in self.tasklist:
            if description == self.task['description']:
                return print(f'Задача {self.task['description']} уже есть в списке.')

        self.task = {'description' : description, 'completed' : False}
        self.tasklist.append(self.task)
        print(f'Задача {self.task['description']} добавлена в список.')

    def complete_task(self, index: int):
        try:
            if self.tasklist[index]['completed']:
                print(f'Задача {self.task['description']} уже помечена как выполненная')
            else:
                self.tasklist[index]['completed'] = True
        except (IndexError, TypeError):
            print('Задача не найдена')

    def remove_task(self, index: int):
        try:
            print(f'Задача {self.tasklist[index]['description']} удалена')
            del self.tasklist[index]
        except (IndexError, TypeError):
            print('Задача не найдена')

    def save_to_json(self, filename: str):
        with open(filename, 'w') as file:
            json.dump(self.tasklist, file, indent=4)

    def load_from_json(self, filename: str):
        with open(filename, 'r') as file:
            from_file = json.load(file)
        print(from_file)
        return from_file

    def get_list(self):
        return self.tasklist


manager1 = TaskManager()

manager1.add_task(12345)
manager1.add_task(12345)
manager1.add_task('aboba')
manager1.add_task('zizi')
manager1.complete_task(1)
manager1.complete_task(1)
manager1.remove_task(0)
manager1.remove_task(2)
manager1.save_to_json('tasklist.json')
manager1.load_from_json('tasklist.json')