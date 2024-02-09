class person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height


# class named student inheriting from class named person

class student(person):

    # can we also inherit (base, main, super) constructor

    def __init__(self, name, age, height, id):
        # person.__init__(name, age, height)
        # or

        # super - refers to upperClass of student class
        super().__init__(name, age, height)

        self.id = id

    def sayId(self):
        return f"My id is {self.id}"


ahmed = student("ahmed", 22, 177, 99999)

print(ahmed.sayId())
