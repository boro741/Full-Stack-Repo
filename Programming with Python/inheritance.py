class Parent():
    def __init__(self, last_name,eye_color ):
        print("Parent Constructor is called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last name - "+self.last_name)
        print("Eye color - "+self.eye_color)
        
class Child(Parent):
    def __init__(self,last_name,eye_color,number_of_toys):
        print("Child Constructor is called")
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys = number_of_toys

pavan_boro = Parent("Boro","Black")

#print(pavan_boro.last_name)

boro = Child("boro","black",5)
pavan_boro.show_info()
