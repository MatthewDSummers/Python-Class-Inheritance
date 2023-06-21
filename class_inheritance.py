HIGHLIGHT_GREEN = "\033[42m"
HIGHLIGHT_YELLOW = "\033[43m"
RED = "\033[31m"
RESET = "\033[0m"

class Person:
    objects = {}
    object_id = 1

    def __init__(self, first_name, last_name, age):
        self.id = Person.object_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.register()

    def register(self):
        Person.objects[self.id] = self
        Person.increment_id()

    @classmethod
    def increment_id(cls):
        cls.object_id += 1

    @classmethod
    def get(cls, id=None):
        person = cls.objects.get(id)
        if issubclass(cls, Employee):
            object_type = " Employee"
            COLOR = HIGHLIGHT_YELLOW
        else:
            COLOR = HIGHLIGHT_GREEN
            object_type = " Person"

        if person:
            print("\n" + COLOR + f"{object_type}: " + RESET +"\n" + "-------------")

            for k, v in vars(person).items():
                print(f"{k}: {v}")
            print("-------------")

            return cls.objects.get(id)
        else:
            print(RED + f"{object_type} does not exist" + RESET)

    @classmethod
    def get_all(cls):
        if issubclass(cls, Employee):
            object_type = " Employees"
            COLOR = HIGHLIGHT_YELLOW
        else:
            object_type = " People"
            COLOR = HIGHLIGHT_GREEN

        if cls.objects:
            print("\n" + COLOR + f" Printing{object_type}: " + RESET)

            for person in cls.objects.values():
                print(f"-------------\nID: {person.id}")
                if issubclass(cls, Employee):
                    print(f"Company: {employee.company}")
                print(f"Name: {person.first_name} {person.last_name}")
                print(f"Age: {person.age}")
            print("-------------")

            return cls.objects.values()
        else:
            print(RED + f" There are no{object_type}" + RESET)

class Employee(Person):
    objects = {}
    object_id = 1

    def __init__(self, PERSON_OBJECT, company):
        self.id = Employee.object_id
        self.company = company
        self.first_name = PERSON_OBJECT.first_name
        self.last_name = PERSON_OBJECT.last_name
        self.age = PERSON_OBJECT.age
        self.register()

    def register(self):
        Employee.objects[self.id] = self
        Employee.increment_id()

Person.get(909)
Employee.get(909)

Person.get_all()
Employee.get_all()

#create some people
person = Person("Alice", "Alabaster", 35)
person_two = Person("Bob", "Bardswell", 49)
person_three = Person("Harold", "Helper", 94)
person_four = Person("Wally", "Winslow", 20)

# create some employees
employee = Employee(person, "Microsoft")
employee_two = Employee(person_two, "Samsung")
employee_three = Employee(person_four, "Celcom")


### P E O P L E ###

# Get all people
every_person = Person.get_all()

# Accessing the data of each person
print("\n" + HIGHLIGHT_GREEN + " Accessing each person: " + RESET)
for person in every_person:
    print(person)
    for k, y in vars(person).items():
        print(f"{k}: {y}")
    print("------------")

# Get single person
print(Person.get(id=1))


### E M P L O Y E E S ###

# Get all employees 
every_employee = Employee.get_all()

# Accessing the data of each employee
print("\n" + HIGHLIGHT_YELLOW + " Accessing each employee: " + RESET)
for employee in every_employee:
    print(employee)
    for k, y in vars(employee).items():
        print(f"{k}: {y}")
    print("------------")

# Get single employee
print(Employee.get(id=2))