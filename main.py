class Intern:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Employee(Intern):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def get_salary(self):
        return self.salary


class Company:
    def __init__(self, max_interns, max_employees):
        self.max_interns = max_interns
        self.max_employees = max_employees
        self.interns = []
        self.employees = []
        self.total_salary = 0

    def add(self):
        add = input("Are you adding an intern, employee or done adding (intern or employee or done)? ")
        while add.lower() != 'intern' and add.lower() != 'employee' and add.lower() != 'done':
            add = input('Error: Are you adding an intern or employee (intern or employee)? ')
        while add != 'done':
            if add.lower() == 'intern':
                if len(self.interns) == self.max_interns:
                    print('Max interns reached, please remove an intern to add another')
                else:
                    name = input('What is their name? ')
                    for intern in self.interns:
                        if name.lower() == intern.name.lower():
                            return print('Sorry, we already have an intern by that name')
                    age = input('What is their age? ')
                    intern = Intern(name, int(age))
                    self.add_intern(intern)
            if add.lower() == 'employee':
                if len(self.employees) == self.max_employees:
                    print('Max employees reached, please remove an intern to add another')
                else:
                    name = input('What is their name? ')
                    for employee in self.employees:
                        if name.lower() == employee.name.lower():
                            return print('Sorry, we already have an employee by that name')
                    age = input('What is their age? ')
                    salary = input('What is their salary? ')
                    employee = Employee(name, int(age), int(salary))
                    self.add_employee(employee)
            add = input("Are you adding an intern, employee or done adding (intern or employee or done)? ")
            while add.lower() != 'intern' and add.lower() != 'employee' and add.lower() != 'done':
                add = input('Error: Are you adding an intern or employee (intern or employee)? ')

    def remove(self):
        remove = input('Remove an intern or employee or done removing (intern or employee or done)? ')
        while remove.lower() != 'intern' and remove.lower() != 'employee' and remove.lower() != 'done':
            print('Error: Remove an intern or employee or done removing (intern or employee or done)? ')
        while remove != 'done':
            if remove == 'intern':
                self.remove_intern()
            elif remove == 'employee':
                self.remove_employee()
            remove = input('Remove an intern or employee or done removing (intern or employee or done)? ')
            while remove.lower() != 'intern' and remove.lower() != 'employee' and remove.lower() != 'done':
                print('Error: Remove an intern or employee or done removing (intern or employee or done)? ')
        return

    def add_intern(self, intern):
        self.interns.append(intern)

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_intern(self):
        remove = input('Who do you want to remove? ')
        if len(self.interns) != 0:
            for i in range(len(self.interns)):
                if remove.lower() == self.interns[i].name.lower():
                    self.interns.pop(i)
                    print(f'{remove} has been removed')
                    return
        print(f'There is no {remove} in the list of interns')

    def remove_employee(self):
        remove = input('Who do you want to remove? ')
        if len(self.employees) != 0:
            for i in range(len(self.employees)):
                if remove.lower() == self.employees[i].name.lower():
                    self.employees.pop(i)
                    print(f'{remove} has been removed')
                    return
        print(f'There is no {remove} in the list of employees')

    def get_total_salary(self):
        if len(self.employees) == 0:
            return print('You have no employees')
        for employee in self.employees:
            self.total_salary += employee.salary
        return self.total_salary

    def commit_to_file(self):
        f = open('data.txt', 'w')
        f.write("INTERNS\n-------\n")
        if len(self.interns) == 0:
            f.write("You have no interns")
        else:
            i = 1
            for intern in self.interns:
                f.write(f'{i}) Name: {intern.name}\n   Age: {intern.age}\n')
                i += 1
        f.write("\n\nEMPLOYEES\n---------\n")
        if len(self.employees) == 0:
            f.write("You have no employees")
        else:
            i = 1
            for employee in self.employees:
                f.write(f'{i}) Name:   {employee.name}\n   Age:    {employee.age}\n   Salary: ${employee.salary}\n')
                i += 1
            f.write(f"\nTotal Salary: ${self.get_total_salary()}")
        print('Data saved to a .txt file')


maxInterns = input('What are the max number of interns? ')
maxEmployees = input('What are the max number of employees? ')
company = Company(int(maxInterns), int(maxEmployees))

while True:
    choice = input('add, remove or commit? ')
    while choice.lower() != 'add' and choice.lower() != 'remove' and choice.lower() != 'commit':
        choice = input('Error: add, remove or commit? ')
    if choice.lower() == 'add':
        company.add()
    elif choice.lower() == 'remove':
        company.remove()
    elif choice.lower() == 'commit':
        company.commit_to_file()
