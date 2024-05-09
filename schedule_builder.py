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

    def __init__(self, name):
        '''Initializes schedule given a person's name

        Args:
            name (str): The name of the person that the schedule is being made
            for.
        
        Attributes: schedule(list) = list of dictionaries built from each class
        inputed into the list.
        Author : Devin 
        '''
        self.name = name
        if not os.path.exists(f"{self.name}_schedule.json"):
            self.schedule = []
            print(
                f'No existing schedule found for {self.name}. Starting with an empty schedule.')
        else:
            self.load_schedule()

    def coursecode_validation(self, course_code):
        """Validates the course code format while also ensuring that the inputted course code exists in UMD's course catalog.
        
        Args: 
            course_code (str): course code validation.
        
        Returns: 
            bool: True if the input course code is valid, otherwise False.
        Author : 
        Method : Devin, list comprehension
        """
        courseid = []
        with open('202008.json', 'r') as f1:
            courses = json.load(f1)
            courseid = [course['course_id'] for course in courses]
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
        self.schedule.append(
            {'Course code': course_code, 'Credits': credits, 'Days': days, 'Time': time})

        self.save_schedule()

        while True:
            choice = input(
                "Do you want to add another class? (Y/N): ").strip().lower()
            if choice == 'y':
                self.add_class()
                break
            elif choice == 'n':
                return
            else:
                print("Not a valid choice. Please enter 'Y' or 'N'.")

    def save_schedule(self):
        '''Saves the student schedule
            Author: Devin
            Method: json.dump
        '''
        with open(f'{self.name}_schedule.json', 'w') as f2:
            json.dump(self.schedule, f2)

    def load_schedule(self):
        '''Loads the student schedule
            Author: Devin
            Method: json.load
        '''
        try:
            with open(f"{self.name}_schedule.json", 'r') as file:
                self.schedule = json.load(file)
        except FileNotFoundError:
            self.schedule = []
            print('New schedule created')

    def clear_schedule(self):  
        '''Method to clear the self.schedule object. 
            Author: Devin
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
        Author : Devin
        Method : pandas df and filtering out duplicates from the student course schedule
        '''
        if len(self.schedule) != 0:
            organized_schedule = classOrganizer(self.schedule)
            df = pd.DataFrame(organized_schedule, columns=['Course code', 'Credits',
                                                           'Days', 'Time'])
            dfsorted = df.drop_duplicates(
                subset='Course code').reset_index(drop=True)
            return dfsorted
        else:
            return print('No schedule to display')

    def __str__(self):
        """Return a string representation of the number of courses in the schedule.

    Returns:
        str: A string indicating the number of courses in the schedule for the specified name.
    """
        return f"Number of courses in {self.name}'s schedule: {len(self.schedule)}"

    def __len__(self):
        """Return the number of courses in the schedule.

    Returns:
        int: The number of courses in the schedule.
    """
        return len(self.schedule)


def options():
    '''Presents a list of options to the user
    Author : Devin
    '''
    options = '1. Add a class \n2. Drop a class \n3. Clear your schedule\n4. Display your schedule'
    print("Select an option:")
    print(options)

if __name__ == '__main__':
    name = input('What is your name?: ')
    schedule = Schedule(name)
    while True:
        options()
        choice = (input('Select 1, 2, 3 or 4: '))
        choice = int(choice)
        if choice == 1:
            schedule.add_class()
            print('A class was added to your schedule.')
        elif choice == 2:
            schedule.drop_class(input('What is the course code of the class you would like to drop? '))
            print('A class was dropped from your schedule.')
        elif choice == 3:
            schedule.clear_schedule()
            print('Your schedule has been cleared')
        elif choice == 4:
            print(schedule.show_schedule())
        else:
            print('Incorrect input option selected. Try again')

        print(f'Number of courses in {name}\'s schedule: {len(schedule)}')

        while True:
            schedule_action = input(
                "Would you like to perform another schedule action? (Y/N): ").strip().lower()
            if schedule_action == 'y':
                break
            elif schedule_action == 'n':
                exit()
            else:
                print("Not a valid choice. Please enter 'Y' or 'N'.")
