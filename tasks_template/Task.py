class Task:
    """
    For this program, we need to use the next variables:
    * task_name: The name of the tasks prompted
    * dead_line: A date data type which will be helpful to organize data in program
    * priority: The other sorting variable in this program 
    gotta change this
    """
    def __init__(self, task_name, dead_line, priority):
        self.task_name = task_name
        self.dead_line = dead_line
        self.priority = priority

    @property
    def task_name(self):
        return self._task_name
    
    @task_name.setter
    def task_name(self, task_name):
        # If data type is different of str, exit error
        if isinstance(task_name, str):
            raise TypeError("Wrong data type prompted, use instead str type attributes")
        self._task_name = task_name

    @property
    def priority(self):
        return self._priority
    
    @priority.setter
    def priority(self, priority):
        if isinstance(priority, str):
            raise TypeError("Wrong data type prompted, use instead str type attributes")
        self._priority = priority
     
