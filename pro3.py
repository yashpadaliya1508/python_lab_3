class uni:
    def __init__(self,uninm,city):
        self.uninm = uninm
        self.city = city

class tnrao:
    def __init__(self,clgnm,strm):
        self.clgnm = clgnm
        self.strm = strm

class student(uni,tnrao):
    def __init__(self,uninm,city,clgnm,strm,stdnm,enroll):
        uni.__init__(self,uninm,city)
        tnrao.__init__(self,clgnm,strm)
        self.stdnm = stdnm
        self.enroll = enroll

    def dis(self):
        print(f"Univesity Name :- {self.uninm}\nCity :- {self.city}\n")
        print(f"College Name :- {self.clgnm}\nStream :- {self.strm}\n")
        print(f"Student Name :- {self.stdnm}\nEnrollment No :- {self.enroll}")

data = student("Saurashtra University","Rajkot","T.N.Rao College","BCA","Yash Patel",234762834632)
data.dis()
