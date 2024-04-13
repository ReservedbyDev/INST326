import pandas as pd

#print('TestFile')

#print("Hello its Davis")

#print("Hello its Andy")

class Schedule:
    def __init__(self,name):
        self.name = name
        self.schedule = []
    
    def add_class(self):
        course = {'Course code':input('Course code:'),'Credits': input('Credits:'),'Day':input('Day:'),'Time':input('Time')}
        self.schedule.append(course)
    def clear_schedule(self):
        self.schedule = []
    def drop_class(self, code):
        for i in self.schedule:
            if i['Course code'] == code:
                self.schedule.remove(i)
                break
    def show_schedule(self):
        df = pd.DataFrame(self.schedule)
        print(df)
    # will need a method with a with stateent to store courses for self.schedule, that way self.schedule can maintain updates as we add and remove classes
    # after each method or change to the schedule, it should save to the file to keep self.schedule always updated.



s1 = Schedule('Devin')
s1.add_class()
s1.add_class()
print(s1.show_schedule())