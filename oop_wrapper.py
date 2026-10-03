# ==========================================
# OOP WRAPPER - EMPLOYEE MANAGEMENT SYSTEM
# ==========================================


# ---------- MAIN MENU ----------
def main():
    employees = []

    while True:
        print("\n================================")
        print(" EMPLOYEE MANAGEMENT SYSTEM")
        print("================================")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Create a Developer")
        print("5. Show Details")
        print("6. Check OOP Concepts")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        # Create Person
        if choice == "1":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))

            person = Person(name, age)
            employees.append(person)

            print("\nPerson created successfully!")

        # Create Employee
        elif choice == "2":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            employee_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))

            employee = Employee(name, age, employee_id, salary)
            employees.append(employee)

            print("\nEmployee created successfully!")

        # Create Manager
        elif choice == "3":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            employee_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            department = input("Enter Department: ")

            manager = Manager(
                name, age, employee_id, salary, department
            )

            employees.append(manager)

            print("\nManager created successfully!")

        # Create Developer
        elif choice == "4":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            employee_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            language = input("Enter Programming Language: ")

            developer = Developer(
                name, age, employee_id, salary, language
            )

            employees.append(developer)

            print("\nDeveloper created successfully!")

        # Show Details
        elif choice == "5":
            if len(employees) == 0:
                print("\nNo records available.")
            else:
                print("\n========== DETAILS ==========")

                for employee in employees:
                    employee.display()
                    print("-----------------------------")

        # Check OOP Concepts
        elif choice == "6":
            print("\n========== OOP CONCEPTS ==========")

            print(
                "Manager is subclass of Employee:",
                issubclass(Manager, Employee)
            )

            print(
                "Developer is subclass of Employee:",
                issubclass(Developer, Employee)
            )

            print(
                "Employee is subclass of Person:",
                issubclass(Employee, Person)
            )

            print("\nInheritance, Encapsulation,")
            print("Method Overriding and super() are used.")

        # Exit
        elif choice == "7":
            print("\nExiting the system...")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")


# ---------- PERSON CLASS ----------
class Person:

    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def display(self):
        print("\nPerson Details")
        print("Name:", self.name)
        print("Age:", self.age)


# ---------- EMPLOYEE CLASS ----------
class Employee(Person):

    def __init__(
        self,
        name="",
        age=0,
        employee_id="",
        salary=0
    ):
        super().__init__(name, age)

        # Private attributes = Encapsulation
        self.__employee_id = employee_id
        self.__salary = salary

    # Getter for Employee ID
    def get_employee_id(self):
        return self.__employee_id

    # Setter for Employee ID
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    # Getter for Salary
    def get_salary(self):
        return self.__salary

    # Setter for Salary
    def set_salary(self, salary):
        self.__salary = salary

    # Display method
    def display(self):
        print("\nEmployee Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.__employee_id)
        print("Salary: $", self.__salary)

    # Destructor
    def __del__(self):
        pass


# ---------- MANAGER CLASS ----------
class Manager(Employee):

    def __init__(
        self,
        name="",
        age=0,
        employee_id="",
        salary=0,
        department=""
    ):
        super().__init__(
            name, age, employee_id, salary
        )

        self.department = department

    # Method Overriding
    def display(self):
        print("\nManager Details")

        # Calling parent method using super()
        super().display()

        print("Department:", self.department)


# ---------- DEVELOPER CLASS ----------
class Developer(Employee):

    def __init__(
        self,
        name="",
        age=0,
        employee_id="",
        salary=0,
        programming_language=""
    ):
        super().__init__(
            name, age, employee_id, salary
        )

        self.programming_language = programming_language

    # Method Overriding
    def display(self):
        print("\nDeveloper Details")

        # Calling parent method using super()
        super().display()

        print(
            "Programming Language:",
            self.programming_language
        )


# ---------- START PROGRAM ----------
if __name__ == "__main__":
    main()
