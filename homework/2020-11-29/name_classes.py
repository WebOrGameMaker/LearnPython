class Name:
    def __init__(self, first_name, last_name):
        self.fname = first_name.title()
        self.lname = last_name.title()
        self.fullname = first_name.title() + ' ' + last_name.title()
        self.initials = first_name[0] + '.' + last_name[0]

name1 = Name('john', 'DOE')
print(name1.fname)
print(name1.lname)
print(name1.fullname)
print(name1.initials)