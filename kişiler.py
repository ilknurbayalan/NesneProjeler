class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):
    def _init_(self, name, age, student_id):
        super()._init_(name, age)
        self.student_id = student_id

    def display_info(self):
        return f"{super().display_info()}, Student ID: {self.student_id}"

class Teacher(Person):
    def _init_(self, name, age, subject):
        super()._init_(name, age)
        self.subject = subject

    def display_info(self):
        return f"{super().display_info()}, Subject: {self.subject}"

# Örnek kullanım
student = Student("Ahmet", 20, "12345")
teacher = Teacher("Ayşe", 35, "Matematik")

print(student.display_info())
print(teacher.display_info())


