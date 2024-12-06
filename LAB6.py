import pickle


class Course_grades:
    def __init__(self):
        self.course_name = ""
        self.stu_id = []
        self.stu_grade = []

    def get_details(self):
        self.course_name = input("Enter course name: ")
        print("Enter details for 5 students")
        for i in range(5):
            self.stu_id.append(input("enter STU ID:"))
            self.stu_grade.append(int(input("Enter Student Grade (0-100): ")))

    def display(self):
        print("Course Name: ", self.course_name)
        print("Students and Grades: ")
        for i in range(len(self.stu_id)):
            print("ID: ",self.stu_id[i], "Grade", self.stu_grade[i])

class Student:
    def __init__(self):
        self.name = ""
        self.dob = ""
        self.courses = ""
    def get_details(self):
        self.name = input("Enter students Name:")
        self.dob = input("Enter the DOB:")
        self.courses = input("Enter the Course")
    def display(self):
        print("Student's Name:", self.name)
        print("DOB:", self.dob)
        print("Courses", self.courses)


courses = []
print("Create 4 courses and enter their details: ")
for i in range(4):
    course= Course_grades()
    course.get_details()
    courses.append(course)

file_name = "grades_info.dat"
with open(file_name, "ab") as file:
    for course in courses:
        pickle.dump(course, file)
print("Courses have been saved")

read_courses = []
with open(file_name, "rb") as file:
    while True:
        try:
            course = pickle.load(file)
            read_courses.append(course)
        except EOFError:
            break

print("Loaded Course Details")
for i, course in enumerate(read_courses,start =1):
    print(f"\nCourse {i}:")
    course.display()



#Create Objects s1, s2 for student class
s1 = Student()
s1.get_details()
s2 = Student()
s2.get_details()
#Write the objects s1, s2 into a *.dat file
f=open('myStudent.dat', 'ab')
pickle.dump(s1, f)
pickle.dump(s2,f)
f.close()
#open the same dat file in read-binary mode
f = open('myStudent.dat','rb')
#use iterations to read the objects from the file and print the attributes of the class
while 1:
    try:
        data = pickle.load(f)
        print(data.name)
        print(data.dob)
        print(data.courses)
    except(EOFError):
        break


f.close()