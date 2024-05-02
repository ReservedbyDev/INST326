import pandas as pd
import re



def classOrganizer(schedule):
    """takes a schedule organizes it and returns it. 

    Args:
        schedule (List): A list of scheduled class can show in a pandas df

    Returns:
        list: the schedule organized by course code and credits
    """
    sorted_schedule = sorted(schedule, key=lambda x: (x['Course code'], 
                                                      x['Credits']))
    return sorted_schedule

class Schedule:
    '''Class that creates the schedule object, takes in a name as an object.
    '''    
    def __init__(self,name):
        '''Initializes schedule given a person's name

        Args:
            name (str): The name of the person that the schedule is being made
            for.
        
        Attributes: schedule(list) = list of dictionaries built from each class
        inputed into the list.
        '''        
        self.name = name
        self.schedule = []
    
    def coursecode_validation(self, course_code):
        """Validates the course code format.
        
        Args: 
            course_code (str): course code validation.
        
        Returns: 
            bool: True if the input course code is valid, otherwise False.
        """
        expr = r"""(?x)
^(?P<course_code>[a-zA-Z]{4}\d{3}$)"""
        return bool(re.match(expr, course_code))
    
    def add_class(self):
        '''Method used to add classes to the self.schedule attribute. 
        '''        
        while True:
            course_code = input('Course code: ')
            if self.coursecode_validation(course_code):
                break
            else:
                print("Invalid course code. Enter a valid course code.")
        credits = input('Credits: ')
        day = input('Day: ')
        time = input('Time: ')
        self.schedule.append({'Course code': course_code, 'Credits': credits, 'Day': day, 'Time': time})
            
    def clear_schedule(self):
        '''Method to clear the self.schedule object. 
        '''        
        self.schedule = []
        
    def drop_class(self, code):
        '''Method used to drop a class from the schedule attribute

        Args:
            code (str): Course code to be removed from the attribute. Breaks out
            of the loop once it is found because each course should only be 
            listed once.
        '''        
        for course in self.schedule:
            if course['Course code'] == code:
                self.schedule.remove(course)
                break
        else:
            print("Course not found in schedule.")
            
    def show_schedule(self):
        '''Takes the schedule object and creates a dataframe object neatly 
        displaying the class schedule for the given student. 
        '''        
        organized_schedule = classOrganizer(self.schedule)
        df = pd.DataFrame(organized_schedule, columns=['Course code', 'Credits'
                                                       , 'Day', 'Time'])
        return df
    
    def __str_(self):
        return f"Schedule Name: {self.name} Schedule: {self.schedule}"
    
    def __len__(self):
        return len(self.schedule)
    

    # will need a method with a with stateent to store courses for self.schedule
    # , that way self.schedule can maintain updates as we add and remove classes



s1 = Schedule('Devin')
s1.add_class()
schedule_df = s1.show_schedule()
if not schedule_df.empty:
    print(schedule_df)
    
print(s1)
print(f"Number of courses in {s1.name}'s schedule: {len(s1)}")

