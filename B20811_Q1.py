
# Question 1
#### creating class course
class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code

    def __repr__(self):
        return f"{self.course_name} ({self.course_code})"

#### creating class student
class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.enrolled_courses = []

    def enroll(self, course):
        
       
        if course in self.enrolled_courses:
            print(f"{self.name} is already enrolled in {course.course_name}.")
        else:
            self.enrolled_courses.append(course)
            print(f"{self.name} successfully enrolled in {course.course_name}.")


    def drop(self, course):
        
       
        if course not in self.enrolled_courses:
            print(f"{self.name} is not enrolled in {course.course_name}. Cannot drop.")
        else:
            self.enrolled_courses.remove(course)
            print(f"{self.name} successfully dropped {course.course_name}.")


    def display_student_info(self):
        
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        
        print(f"Student ID: {self.student_id}")
        print("Enrolled Courses:")
        
        if not self.enrolled_courses:
            print("No courses enrolled.")
        else:
            for course in self.enrolled_courses:
                print(f"  - {course.course_name} ({course.course_code})")


course1 = Course("OOP", "OOP101")
course2 = Course("Ethics", "ET101")
course3 = Course("Old Testament", "OT101")

student1 = Student("Yokana", 20, "S123")
student2 = Student("Mugerwa", 22, "S124")


student1.enroll(course1)
student1.enroll(course2)

student2.enroll(course1)
student2.enroll(course3)


student1.drop(course1)


student1.display_student_info()
print()  
student2.display_student_info()
