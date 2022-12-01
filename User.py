# Parent class
class User():
    def __init__(self, name, password, age):
        self.name = name
        self.password = password
        self.age = age

    def show_name(self):
        return self.name

    def show_password(self):
        return self.password

    def show_age(self):
        return self.age

    def show_details(self):
        print("Personal Details")
        print(f'{self.name}')
        print(f'{self.password}')
        print(f'{self.age}')