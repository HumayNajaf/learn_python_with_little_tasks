class Employee():
    position = "manager"
    working_hours = "9:00 - 18:30"
    
    def __init__(self):
        self.skills = []
        self.salary = 1500
        self.working_days =  ["Mon", "Tue", "Fri"]
        self.days = 0
    
    def startToWork(self):
        self.days += 1
    
employee1 = Employee()
employee1.skills.append("Python")
employee1.salary = 1800
print(employee1.skills, employee1.salary)

employee2 = Employee()
print(employee2.skills)

employee3 = Employee()
employee3.startToWork()
employee3.startToWork()
print(employee3.days)