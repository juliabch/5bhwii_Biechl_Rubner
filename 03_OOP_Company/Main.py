import Company as comp

if __name__ == '__main__':

    comp1 = comp.Company("blub")
    
    dep1 = comp.Department("IT")
    dep2 = comp.Department("Marketing")
    dep3 = comp.Department("RnD")

    w1 = comp.DepartmentHead("Julia", 18, True)
    w2 = comp.Worker("Eva", 18, True)
    w3 = comp.DepartmentHead("Ian", 19, False)
    w4 = comp.DepartmentHead("Oliver", 18, False)
    w5 = comp.Worker("Kirchmair", 18, False)
    w6 = comp.Worker("Daniel", 19, False)
    w7 = comp.Worker("Haider", 19, False)

    dep1.addPeople(w4)
    dep1.addPeople(w5)

    dep2.addPeople(w1)
    dep2.addPeople(w2)

    dep3.addPeople(w3)
    dep3.addPeople(w6)
    dep3.addPeople(w7)

    comp1.addDepartment(dep1)
    comp1.addDepartment(dep2)
    comp1.addDepartment(dep3)

    print("Count workers: ", comp1.countWorkers())
    print("Count departmentheads: ", comp1.countDepHeads())


    print("Count departments: ", comp1.countDeps())


    print("Largest department: ", comp1.findLargestDep())


    print("Percentage women to men: ", comp1.percentageWomen())

    


    