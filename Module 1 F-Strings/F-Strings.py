# F-Strings
# f"Display {variable}"
# f"Evaluate {expression}"
# f"Call {function}"

# F Strings Variables
print('-------- Display Variables Through F-Strings ------------')
name = 'Ammar'
course = 'Beyond the Basic'
print(f"Hello, I'm {name}. We are learning {course}.")

# Call Functions Through F-Strings
print('-------- Call Functions Through F-Strings ------------')
animal = 'CAT'
print(f"{animal.lower()}")

# Conditionals Formatting Through F-Strings
print('-------- Conditionals Formatting Through F-Strings ------------')
import datetime

time_today = datetime.datetime.now()
print(f'Result: {time_today:{"Weekday" if time_today.weekday() < 5 else "Weekend!"}}')

# F-Strings in Classes
print('-------- F-Strings in Classes ------------')

class Person():
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    def description(self):
        return f"{self.name} is {self.age} years old and likes {self.hobby}"


obj = Person(name='Ammar', age="1000", hobby='Snooker')
print(obj.description())

