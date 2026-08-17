print("----- python OOP project: Employee managment system -----")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("\nPerson Details:")
        print("Name:", self.name)
        print("Age:", self.age)


class Employee:
    def __init__(self, employee_id, name, age, salary):
        self.__employee_id = employee_id
        self.name = name
        self.age = age
        self.__salary = salary

    # Getter for employee_id
    def get_employee_id(self):
        return self.__employee_id

    # Setter for employee_id
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    # Getter for salary
    def get_salary(self):
        return self.__salary 

    # Setter for salary
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary")

    def display(self):
        print("\nEmployee Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.__employee_id)
        print("Salary: $", self.__salary)

    def __del__(self):
        pass


class Manager(Employee):
    def __init__(self, name, age,employee_id, salary, department):
        super().__init__( name, age, employee_id,salary)
        self.department = department

    def display(self):
        print("\nManager Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary: $", self.get_salary())
        print("Department:", self.department)

        
class Developer(Employee):
    def __init__(self, employee_id, name, age, salary, programming_language):
        super().__init__(employee_id, name, age, salary)
        self.programming_language = programming_language

    def display(self):
        print("\nDeveloper Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary: $", self.get_salary())
        print("Programming Language:", self.programming_language)
        
# Dictionary

data = {
    "person": None,
    "employee": None,
    "manager": None
}

# issubclass()
print("Manager is subclass of Employee:", issubclass(Manager, Employee))
print("Developer is subclass of Employee:", issubclass(Developer, Employee))


while True:

    print("\n--- Python OOP Project: Employee Management System ---")
    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))

        person = Person(name, age)

        print(f"\nPerson created with name: {name} and age: {age}.")
        
    elif choice == 2:

        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))
        employee_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))

        employee = Employee( name, age,employee_id, salary)
        

        print(f"\nEmployee created with name: {name}, "f"age: {age}, ID: {employee_id}, "f"and salary: ${salary}.")
        

    elif choice == 3:

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        employee_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")

        manager = Manager(name, age,employee_id,salary,department)

        print( f"\nManager created with name: {name}, "f"age: {age}, ID: {employee_id}, "f"salary: ${salary}, "f"and department: {department}.")

    elif choice == 4:

        print("\nChoose details to show:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            if person :
                person.display()
            else:
                print("\nPerson object not created.")

        elif choice == 2:
            
            if employee :
                employee.display()
            else:
                print("\nEmployee object not created.")

        elif choice == 3:

            if manager :
                manager.display()
            else:
                print("\nManager object not created.")

        else:
            print("Invalid choice.")

    elif choice == 5:

        print("\nExiting the system. All resources have been freed.")
        print("\nGoodbye!")
        break  

    else:
        print("Invalid choice")


    
