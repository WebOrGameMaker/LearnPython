class Name:
    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name
        self.fullname = first_name + ' ' + last_name
        self.initials = first_name[0] + '.' + last_name[0]

name1 = Name('John', 'Doe')
print(name1.fname)
print(name1.lname)
print(name1.fullname)
print(name1.initials)