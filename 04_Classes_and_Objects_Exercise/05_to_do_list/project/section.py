from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def find_task_by_name(self, name):
        searched_task = [t for t in self.tasks if t.name == name]
        if searched_task:
            return searched_task[0]
        return None

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        searched_task = self.find_task_by_name(task_name)
        if not searched_task:
            return f"Could not find task with the name {task_name}"
        searched_task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        removed_tasks = [t for t in self.tasks if t.completed]
        for t in removed_tasks:
            if t in self.tasks:
                self.tasks.remove(t)
        return f"Cleared {len(removed_tasks)} tasks."

    def view_section(self):
        result = f'Section {self.name}:\n'
        for t in self.tasks:
            result += t.details() + '\n'
        return result


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
