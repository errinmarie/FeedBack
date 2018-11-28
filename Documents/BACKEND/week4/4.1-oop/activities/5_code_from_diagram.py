# Challenge #1: Discussion
# Can you explain in your own words to the person next to you how the Employee
# and Position class code below corresponds to the diagram in
# "solution_diagrams"?

class Employee:
    def __init__(self, name, boss):
        self.name = name
        self.boss = boss
        self.position = None

    def print_info(self):
        print('---- Employee ----')
        print('Name: ', self.name)

        if self.boss:
            print('Boss: ', self.boss.name)
        else:
            print('Boss: None (Yay!)')

        if self.position:
            print('Position: ', self.position.name)
        else:
            print('Position: None (What do I even do here?)')


class Position:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.is_filled = False

    def fill_with_employee(self, employee):
        self.is_filled = True
        employee.position = self


bossman = Employee('Bill Lumbergh', None)
programmer = Position('Software Engineer', 80000)
waiter = Position('Waiter', 18000)

peter = Employee('Peter Gibbons', bossman)
joanna = Employee('Joanna', bossman)

programmer.fill_with_employee(peter)
waiter.fill_with_employee(joanna)

peter.print_info()
joanna.print_info()



# Challenge #2: Implementation
# Now, write code to correspond to each of the other diagrams you find in
# "solution_diagrams" in real code.
# Hint: The way we have the diagrams could have a few interpretations, so there
# isn't one true answer to them.


