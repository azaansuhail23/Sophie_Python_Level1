class Train_Reservation:
    #normal function --> constructor --> It runs automatically when the object is created from this class
    def __init__ (self,name,age,address,_from,_to,train_name):
        self.name=name
        self.age=age
        self.address=address
        self._from=_from
        self._to=_to
        self.train_name=train_name

person1=Train_Reservation("Sophie",16,"XYZ_Canada","toronto","barrie","DLR_TR")

print(person1.name)
print(person1.age)
print(person1.address)
print(person1._from)
print(person1._to)
print(person1.train_name)

print("-----------")

person2=Train_Reservation("Azaan",24,"Bareilly","Bareilly","New Delhi","Vande Bharat")

print(person2.name)
print(person2.age)
print(person2.address)
print(person2._from)
print(person2._to)
print(person2.train_name)
