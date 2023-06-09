# make a person class
# define what a person does 
# by using person class, I'd like to make teacher and student 

class person():
    def __init__(self, name, age, gender, height, weight):
        self.name = name 
        self.age = age 
        self.gender = gender
        self.height = height 
        self.weight = weight
    
    def talk(self, quote):
        print(quote)
    
    def introduce (self):
        print(f'my name is {self.name}, I am {self.age} years old. My height is {self.height}cm, my weight is {self.weight}kg and I am a {self.gender}.')

me = person('hayden', 17, 'male', 179, 70)
me.introduce()

class teacher(person):
    pass

class student(person):
    def __init__(self, name, age, gender, school_name, school_year, height = None, weight = None):
        super().__init__(name, height, age, gender, weight)
        self.school_name = school_name 
        self.school_year = school_year

    def sleep(self, hours):
        self.sleep_hours = hours
        print(f'{self.name} sleeps for {hours} hours')

    def eat(self, food_type):
        print(f'{self.name} eats {food_type}')

    def study(self):
        print(f'{self.name} studies for {(24-self.sleep_hours)} hours')