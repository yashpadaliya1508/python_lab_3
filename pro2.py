class company:
    def dis1(self):
        nm = "Y2C"
        city = "Rajkot"
        mobo = 247273435
        print(f"Company Name :- {nm}\nCity :- {city}\nMobile Number :- {mobo}\n\n")

class employee(company):
    def dis2(self):
        empnm = "Yash Patel"
        desig = "Manager"
        sal = 120000
        print(f"Employee Name :- {empnm}\nDesignation :- {desig}\nSalary :- {sal}")

dis = employee()
dis.dis1()
dis.dis2()
