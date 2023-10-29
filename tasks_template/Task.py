from enum import Enum
from datetime import datetime
from sys import exit
"""
    For this program, we need to use the next variables:

    * task_name: A string variale to store the name of the variable
    * deadline: A date data type to set a deadline for a given task
    * priority: A string variable to set the importance of given taks
"""

class Priority(Enum):
    URGENT = 1
    HIGH = 2
    MEDIUM = 3
    LOW = 4

class Task:
    def __init__(self, id: int, name: str, priority: Priority, deadline: datetime):
        self.id = id
        self.name = name
        self.priority = priority
        self.deadline = deadline


    """ Id attribute getters and setters"""
    @property
    def id(self):
        return self._id
   
    @id.setter
    def id(self, id):
        # If data type is different of str, exit error
        if isinstance(id, int):
            raise TypeError("Wrong data type prompted, use instead int type attribute")


    """ Name attribute getters and setters """
    @property
    def name(self):
        return self._name
    
    @name.setter
    def task_name(self, name):
        # If data type is different of str, exit error
        if isinstance(name, str):
            raise TypeError("Wrong data type prompted, use instead str type attributes")
        
        self._name = name
    
    
    """ Priority attribute getters and setters """
    @property
    def priority(self):
        return self._priority
    
    @priority.setter
    def priority(self, priority):
        # If there isn't a match with the correct priorities, exit
        if priority  == Priority.URGENT or priority == Priority.HIGH or priority == Priority.MEDIUM or Priority == Priority.LOW:
            self._priority = priority
        
        exit("Priority input is not a correct value")
        
    """ Deadline gettters and setters"""
    @property
    def deadline(self):
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        if isinstance(deadline, datetime):
            raise TypeError("Incorrect data type for deadline")
        
        self._deadline = deadline

    def __repr__(self):
        return f"Task(id= {self.id}, name= {self.name}, priority={self.priority.name}, deadline= {str(self.deadline)})"



     
