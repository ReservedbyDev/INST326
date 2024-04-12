import pandas as pd

#print('TestFile')

#print("Hello its Davis")

#print("Hello its Andy")

def classOrganizer(schedule):
    sorted_schedule = sorted(schedule, key=lambda x: (x['Course code'], x['Credits']))
    return sorted_schedule

class Schedule:
    def __init__(self,name):
        self.name = name
        self.schedule = []
    
    def add_class(self):
        course_code = input('Course code: ')
        credits = input('Credits: ')
        day = input('Day: ')
        time = input('Time: ')
        self.schedule.append({'Course code': course_code, 'Credits': credits, 'Day': day, 'Time': time})
    def clear_schedule(self):
        self.schedule = []
    def drop_class(self, code):
        for course in self.schedule:
            if course['Course code'] == code:
                self.schedule.remove(course)
                break
        else:
            print("Course not found in schedule.")
    def show_schedule(self):
        organized_schedule = classOrganizer(self.schedule)
        df = pd.DataFrame(organized_schedule, columns=['Course code', 'Credits', 'Day', 'Time'])
        print(df)
    
    def save_schedule(self):
        file_name = "class_schedule.txt"
        with open(file_name, 'w') as f:
            for course in self.schedule:
                f.write(f"Course code: {course['Course code']}\n")
                f.write(f"Credits: {course['Credits']}\n")
                f.write(f"Day: {course['Day']}\n")
                f.write(f"Time: {course['Time']}\n")
                f.write("\n") 
    # will need a method with a with stateent to store courses for self.schedule, that way self.schedule can maintain updates as we add and remove classes



s1 = Schedule('Devin')
s1.add_class()
print(s1.show_schedule())
s1.save_schedule()
