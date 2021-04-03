class Person(object):

    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


def print_depth(data, depth=1):

    if isinstance(data, Person):
        print_family_details(data, depth)
        if isinstance(data.father, Person):
            print_depth(data.father, depth + 1)

    elif isinstance(data, dict):
        for key in data:
            print(f"{key} {depth}")
            if isinstance(data[key], object):
                print_depth(data[key], depth + 1)

def print_family_details(person, depth):
    print_fields = ["first_name", "last_name", "father"]
    for field in print_fields:
        print(f"{getattr(person, field)} {depth}")
