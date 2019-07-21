

class Person:
    def __init__(self, first, last):
        self.first_name = first
        self.lastname = last

    def full_name(self):
        return f"{self.first_name} {self.lastname}"
    



def main():
    print("main code")
    p1 = Person("tom","victor")
    print(p1.first_name)
    print(p1.lastname)
    print(p1.full_name())

if __name__ == "__main__":
    main()