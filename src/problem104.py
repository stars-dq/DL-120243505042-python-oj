import copy
class Person:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def displayPerson(self):
        print(f"{self.name} {self.id}")
if __name__ == "__main__":
    name, id_str = input().split()
    id_num = int(id_str)
    p1 = Person(name, id_num)
    p2 = copy.copy(p1)
    p1.displayPerson()
    p2.displayPerson()
    