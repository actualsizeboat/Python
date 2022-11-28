class Employee:

    # class variables
    raise_amt = 1.04
    num_of_emps = 0

    # the init function runs every time the class is instatiated
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int (self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return ('{} - {}'.format(self.fullname(),self.email))

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

# this is inheritance - will inherit all methods unless otherwise defined
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # super declares that it's taking from the parent class,
        # else use parentclassname no parens and call self
        # Employee.__init__(self, first, last, pay)
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = [] # don't pass an empty list or dict as default var
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

emp_1 = Employee('JohnE', 'Doe',50000)
emp_2 = Employee('2FirstE', '2Last',2000)
dev_1 = Developer('Djoe','Ddohn',400000, 'Python')
dev_2 = Developer('JohnD','Ddoe',500000,'Python')
mgr_1 = Manager('Mgr','Dept',90000, [dev_1, dev_2])
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
# print(mgr_1.email)
# mgr_1.print_emps()
# print(isinstance(mgr_1, Employee))

print(emp_1)