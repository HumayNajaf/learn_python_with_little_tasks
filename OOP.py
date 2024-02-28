import time

# class Employee():
#     position = "manager"
#     working_hours = "9:00 - 18:30"
    
#     def __init__(self, skills, salary, working_days):
#         self.skills = skills
#         self.salary = salary
#         self.working_days =  working_days
#         self.days = 0
    
#     def startToWork(self):
#         self.days += 1
        
    
# class  Manager(Employee):
#     pass

# mustafa = Manager(['Python'],  '500$',7)
# print(mustafa)

class Machine():
    def __init__(self):
        self.cycle = 0
        self.ink = 100
        self.charg = 100
        self.print = []
    def start(self):
        if (self.charg<=0 or self.ink<=0):
            print(f'Machine is not available now. Please check ink or the charge the machine')
            time.sleep(2)
            
        else:
            self.cycle += 1
            self.ink -= 3
            self.charg -= 6
            print("Machine is running. Please wait...")
            time.sleep(2)
            if self.cycle==20:
                self.newPrint()
                self.cycle = 0
    def newPrint(self):
        print("Print is ready!")
        printName = input("Enter the print's name: ")
        self.print.append(printName)
        time.sleep(2)
    def refillCharge(self):
        if self.charg<100:
            self.charg += 10
            print('Charged successfully')
        else:
            print('The machine is already charged')
    def fillInk(self):
        if self.ink<100:
            self.ink  += 10
            print('Ink filled succesfully')
    def currentStatus(self):
        print("Current status of the machine: ")
        print("Ink: ", self.ink)
        print("Charge: ", self.charg)
        print("Ink: ", self.ink)
        print("Total print count: ", len(self.print))
        if len(self.print)>=1:
            for i in print:
                print(i)
        print("New print loading: ", self.cycle*5,'%' )
        
machine1 = Machine()

print("Hi! Welcome to our printer.")
print('     ***     '*3)
print('Start machine  ->1\n'
    'Add Ink        ->2\n'
    'Refill Charge  ->3\n'
    'Print a page   ->4\n'
    'Current status ->5\n'
    'Exit           ->6')

while True:
    command = input(str("Choose an option: "))
    if (command == '1'):
        machine1.start()
    elif  (command=='2'):
        machine1.fillInk()
    elif (command=='3'):
        machine1.refillCharge()
    elif (command=='4'):
        #Bu bölmə tam hazır deyil! Səhifə sayı daxil edildikdə error(((...
        while True:
            try:
                pages = int(input("Enter number of pages you want to print: "))
                break
            except ValueError:
                print ("That is not a valid entry, please enter a number")
        machine1.printPage(pages)
        #! -------------------------------------------------------------------------
    elif (command=='5'):
        machine1.currentStatus()
    else:
        quit()