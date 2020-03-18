class Person:
    def __init__(self, _name=str, _pwd=str):
        self.name = _name
        self.pwd = _pwd

    def to_string(self):
        print("Person [name:{0},pwd:{1}]".format(self.name, self.pwd))


