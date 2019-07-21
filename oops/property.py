

class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
    
    @property
    def full_name(self):
        return f"{self.firstname} {self.lastname}"
    
    @full_name.setter
    def full_name(self,value):
        print(value)
        self.first_name, self.lastname = value.split(" ")
        print(self.firstname)
        print(self.lastname)
    

def main():
    print("main code")
    p1 = Person("tom","victor")
    # print(p1.first_name)
    # print(p1.lastname)
    # print(p1.full_name)

if __name__ == "__main__":
    main()