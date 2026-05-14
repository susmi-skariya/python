class Person:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height

    def display(self):
        print(f"The person name {self.name} with {self.age} years old having {self.height} cm height")

p1=Person("Susmi",15,172)
p2=Person("Rishana",10,162)

p1.name="Aami" # modifying objects

print(p1.name)
# print(p2.name)

p1.display()
# p2.display()