# Parent class
class User():
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def show_name(self):
        return self.name

    def show_password(self):
        return self.password

    def show_details(self):
        print(f'{self.name}')
        print(f'{self.password}')
