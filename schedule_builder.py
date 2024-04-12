import pandas as pd
import re



def classOrganizer(schedule):
    """takes a schedule organizes it and returns it. 

    Args:
        schedule (List): A list of scheduled class can show in a pandas df

    Returns:
        list: the schedule organized by course code and credits
    """
    sorted_schedule = sorted(schedule, key=lambda x: (x['Course code'], x['Credits']))
    return sorted_schedule

class Schedule:
    def __init__(self,name):
        self.name = name
        self.schedule = []
    
    def coursecode_validation(self, course_code):
        """Validates the course code format.
        
        Args: course_code (str): course code validation.
        
        Returns: bool: True if the input course code is valid, otherwise False.
        """
        expr = r"""(?x)
^(?P<course_name>[a-zA-Z]+\d\d\d)"""
        if re.match(expr, course_code):
            return True
        else: 
            return False
    
    def add_class(self):
        course_code = input('Course code: ')
        if self.coursecode_validation(course_code):
            credits = input('Credits: ')
            day = input('Day: ')
            time = input('Time: ')
            self.schedule.append({'Course code': course_code, 'Credits': credits, 'Day': day, 'Time': time})
        else: 
            print("Invalid course code. Enter a valid course code.")
            
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
    

    # will need a method with a with stateent to store courses for self.schedule, that way self.schedule can maintain updates as we add and remove classes



s1 = Schedule('Devin')
s1.add_class()
print(s1.show_schedule())

