import datetime
from datetime import date
import sys

class Deadline:
    def __init__(self, task_year, task_month, task_day):
        try:
            date(task_year, task_month, task_day)
        except ValueError:
            print("You must input a real date")
            sys.exit()
        else:
            self.task_year = task_year
            self.task_month = task_month
            self.task_day = task_day   
    
    @property
    def task_year(self):
        return self._task_year
    
    @task_year.setter
    def task_year(self, task_year):
        if task_year > datetime.MAXYEAR  or task_year < datetime.MINYEAR:
            raise ValueError("Plase, input an accepted year")
        self._task_year = task_year

    @property
    def task_month(self):
        return self._task_month
    
    @task_month.setter
    def task_month(self, task_month):
        if task_month < 1 or task_month > 12:
            raise ValueError("Plase, input an accepted month")
        self._task_month = task_month

    @property
    def task_day(self):
        return self._task_day
    
    @task_day.setter
    def task_day(self, task_day):
        try:
            date(self.task_year, self.task_month, task_day)
        except ValueError():
            print("Day input doesn't match with a real date")
        else:
            self._task_day = task_day
            