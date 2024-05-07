import pandas as pd
import re
import json
import os


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
        if not os.path.exists(f"{self.name}_schedule.json"):
            self.schedule = []
            print(f'No existing schedule found for {self.name}. Starting with an empty schedule.')
        else:
            self.load_schedule()
    
    def coursecode_validation(self, course_code):
        """Validates the course code format while also ensuring that the inputted course code exists in UMD's course catalog.
        
        Args: 
            course_code (str): course code validation.
        
        Returns: 
            bool: True if the input course code is valid, otherwise False.
        """
        courseid = []
        with open('202008.json','r') as f1:
            courses = json.load(f1)
            for course in courses:
                courseid.append(course['course_id'])
        if course_code in courseid:
                expr = r"""(?x)^(?P<course_code>[a-zA-Z]{4}\d{3}$)"""
                return bool(re.match(expr, course_code))
        else:
            print(['Course code not found in course catalog. Enter a valid course code'])
    def add_class(self):
        '''Method used to add classes to the self.schedule attribute. 
        '''      
        while True:
            course_code = input('Course code: ').upper()
            if self.coursecode_validation(course_code):
                break
            else:
                print("Invalid course code. Enter a valid course code.")
        credits = input('Credits: ')
        days = input('Days: ')
        time = input('Time: ')
        self.schedule.append({'Course code': course_code, 'Credits': credits, 'Days': days, 'Time': time})
        
        self.save_schedule()
    
    def save_schedule(self):
        '''Saves the student schedule
        '''        
        with open(f'{self.name}_schedule.json','w') as f2:
            json.dump(self.schedule, f2)
    
    def load_schedule(self):
        '''Loads the student schedule
        '''        
        try:
            with open(f"{self.name}_schedule.json", 'r') as file:
                self.schedule = json.load(file)
        except FileNotFoundError:
            self.schedule=[]
            print('New schedule created')
            
    
    def clear_schedule(self):
        '''Method to clear the self.schedule object. 
        ''' 
        self.load_schedule()      
        self.schedule = []
        self.save_schedule()
        
        
    def drop_class(self, code):
        '''Method used to drop a class from the schedule attribute

        Args:
            code (str): Course code to be removed from the attribute. Breaks out
            of the loop once it is found because each course should only be 
            listed once.
        ''' 
        self.load_schedule()      
        for course in self.schedule:
            if course['Course code'] == code:
                self.schedule.remove(course)
                break
        else:
            print("Course not found in schedule.")
        self.save_schedule()
            
    def show_schedule(self):
        '''Takes the schedule object and creates a dataframe object neatly 
        displaying the class schedule for the given student. 
        '''        
        if len(self.schedule) != 0:
            organized_schedule = classOrganizer(self.schedule)
            df = pd.DataFrame(organized_schedule, columns=['Course code', 'Credits', 'Days', 'Time'])
            return df
        else:
            return print('No schedule to display')
    
    def __str__(self):
        return f"Schedule Name: {self.name} Schedule: {self.schedule}"
    
    def __len__(self):
        return len(self.schedule)
    

    # will need a method with a with statement to store courses for self.schedule
    # , that way self.schedule can maintain updates as we add and remove classes




s1 = Schedule('Devin')
#s1.clear_schedule()
#s1.add_class()
schedule_df = s1.show_schedule()
print(schedule_df)
    
print(s1)
print(f"Number of courses in {s1.name}'s schedule: {len(s1)}")

