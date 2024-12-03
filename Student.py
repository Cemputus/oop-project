class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.courses = []

    def enroll(self, course_name):
        if course_name not in self.courses:
            self.courses.append(course_name)
            print(f"{self.name} has enrolled in {course_name}.")
        else:
            print(f"{self.name} is already enrolled in {course_name}.")

    def drop(self, course_name):
        if course_name in self.courses:
            self.courses.remove(course_name)
            print(f"{self.name} has dropped {course_name}.")
        else:
            print(f"{course_name} is not in {self.name}'s enrolled courses.")

    def display_student_info(self):
        print(f"Student Name: {self.name}, ID: {self.student_id}, Enrolled Courses: {self.courses}")


class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code


# Demonstration
student1 = Student("Alice", 20, "S001")
student2 = Student("Bob", 22, "S002")

student1.enroll("Math")
student1.enroll("Physics")
student2.enroll("Chemistry")
student2.enroll("Biology")

student1.drop("Physics")
student1.display_student_info()
student2.display_student_info()
