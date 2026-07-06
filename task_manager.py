class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        return self.tasks

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return True
        return False