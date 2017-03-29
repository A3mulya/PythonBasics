class Employee:

    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
       print("Name : ", self.name, ", Salary: ", self.salary)

object1=Employee('kolaparthi',9089)
object1.displayCount()
print ("Employee.__doc__:", Employee.__doc__)
print ("\nEmployee.__name__:", Employee.__name__)
print ("\nEmployee.__module__:", Employee.__module__)
print ("\nEmployee.__bases__:", Employee.__bases__)
print ("\nEmployee.__dict__:", Employee.__dict__)