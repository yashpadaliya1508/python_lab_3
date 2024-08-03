class Employee:
    def __init__(self,empnm,doj,desig,sal):
        self.empnm = empnm
        self.doj = doj
        self.desig = desig
        self.sal = sal
data = Employee("Yash Patel","27-2-2024","Manager",120000)
print(f"Employee Name :- {data.empnm}\nDate Of Join :- {data.doj}\nDesignation :- {data.desig}\nSlary :- {data.sal}") 
