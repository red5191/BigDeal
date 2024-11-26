class TaskManager():
    def __init__(self):
        self.tasklist = []

    def add_task(self, description : str):
        task = {description : str, complete : False}
        self.tasklist.append(task)

    def complete_task(self, index: int):
        self.tasklist[index[complete]] = True

    # def remove_task(self, index: int)
    #
    # def save_to_json(self, filename: str)
    #
    # def load_from_json(self, filename: str)

man1 = TaskManager
man1.add_task()
print(man1)