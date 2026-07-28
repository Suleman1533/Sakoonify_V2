class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value.strip()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age can't be negative")
        self._age = value

    def greet(self):
        return f"Salam, I am {self.name}."


class Student(Person):
    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        return f"Salam, I am {self.name} (Student ID: {self.student_id})."


# Test it
if __name__ == "__main__":
    s = Student("Suleman", 22, "BSCS-1234")
    print(s.greet())
    print(f"Age: {s.age}")
    
    # Test the setter
    s.age = 23
    print(f"Updated Age: {s.age}")
    
    # Uncomment to test validation:
    # s.age = -5  # This will raise an error