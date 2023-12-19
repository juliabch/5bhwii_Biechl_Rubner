class Company:
    def __init__(self, compName):
        self.compName = compName
        self.deps = []
    
    def addDepartment(self, department):
        if isinstance(department, Department) == True:
            self.deps.append(department)
    
    #1. Sum of all workers in the company
    def countWorkers(self):
        count = 0
        for dep in self.deps:
            for person in dep.people:
                if isinstance(person, Worker) == True:
                    count += 1
        return count  

    #1. Sum of all department heads
    def countDepHeads(self):
        count = 0
        for dep in self.deps:
            for person in dep.people:
                if isinstance(person, DepartmentHead) == True:
                    count += 1
        return count  

    #2. Sum of all departments
    def countDeps(self):
        return len(self.deps)         

    #3. Largest department
    def findLargestDep(self):
        largest = Department("Dummy")
        for dep in self.deps:
            if len(dep.people) > len(largest.people):
                largest = dep
        if largest.depName == "Dummy":
            return "No departments with workers"
        return largest.depName
    
    #4. Percentage Women
    def percentageWomen(self):
        count = 0
        for dep in self.deps:
            for person in dep.people:
                if person.isFemale == True:
                    count += 1
        return (count / self.countWorkers()) * 100


class Department(Company):
    def __init__(self, depName):
        self.depName = depName
        self.people = []
    
    def addPeople(self, person):
        if isinstance(person, Worker) == True:
            self.people.append(person)

class Person:
    def __init__(self, name, age, isFemale):
        self.name = name
        self.age = age
        self.isFemale = isFemale

class Worker(Person):
    def __init__(self, name, age, isFemale):
        super().__init__(name, age, isFemale)

class DepartmentHead(Worker):
    def __init__(self, name, age, isFemale):
        super().__init__(name, age, isFemale)

