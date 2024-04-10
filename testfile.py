#print('TestFile')

#print("Hello its Davis")

#print("Hello its Andy")

class Schedule:
    def __init__(self,name):
        self.name = name
        self.schedule = []
    
    def add_class(self,code,credits,day,time):
        course = {'Course code':code,'Credits': credits,'Day':day,'Time':time}
        self.schedule.append(course)
    def clear_schedule(self):
        self.schedule = []
    def drop_class(self, code):
        for i in self.schedule:
            print(i)
            if i['Course code'] == code:
                self.schedule.remove(i)
                break
        


s1 = Schedule('Devin')

s1.drop_class('INST126')
print(s1.schedule)