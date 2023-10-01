class Task:
    """
    For this program, we need to use the next variables:

    * task_name: A string variale to store the name of the variable
    * deadline: A date data type to set a deadline for a given task
    * priority: A string variable to set the importance of given taks
    """
    def __init__(self, task_name, deadline, priority):
        self.task_name = task_name
        self.deadline = deadline
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
    def deadline(self):
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        self._deadline = deadline

    @property
    def priority(self):
        return self._priority
    
    @priority.setter
    def priority(self, priority):
        # If data type is different of str, exit error
        if isinstance(priority, str):
            raise TypeError("Wrong data type prompted, use instead str type attributes")
        
        self._priority = priority

    
     
