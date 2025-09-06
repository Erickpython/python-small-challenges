# DEFINING THE STUDENT CLASS - HAS NAME, AGE AND GRADE 
class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age 
        self.grade = grade

    def get_info (self):
        return f"Student: {self.name}, Age: {self.age}, Grade: {self.grade}"
    

#DEFINING THE TEACHER CLASS - HAS A NAME AND SUBJECT
class teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def get_info(self):
        return f"Teacher: {self.name}, Subject: {self.subject}"
    

# DEFINING THE SCHOOL CLASS >> CAN ADD BOTH STUDENTS AND TEACHERS  
class school:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def addStudent (self, student):
        self.students.append (student)

    def addTeachers (self, teacher):
        self.teachers.append (teacher)

    def showMembers (self):
        print (f"\n--- {self.name}  Members---")

        print ("\n Teachers:")
        for t in self.teachers:
            print (t.get_info())


        print ("\n Student: ")
        for s in self.students:
            print (s.get_info())            


# DECLARING SCHOOL NAME 
school = school ("NGWATA PRIMARY SCHOOL")

# DECLARING TEACHER  IN THE SCHOOL
teacher1 = teacher ("ERICK", "PRE TECHNICAL STUDIES")
teacher2 = teacher ("BEN", "SOCIAL STUDIES")
teacher3 = teacher ("STACY", "ENGLISH")

# ADDING THE TEACHERS TO THE SCHOOL
school.addTeachers (teacher1)
school.addTeachers (teacher2)
school.addTeachers (teacher3)


# DECLARING STUDENTS IN THE SCHOOL 
student1 = student ("EVANS", 12, "B+")
student2 = student ("MARY", 15, "A")
student3 = student ("JOHN", 14, "B")

# ADDING STUDENTS TO THE SCHOOL 
school.addStudent (student1)
school.addStudent (student2)
school.addStudent (student3)


# TO SHOW EVERY MEMBER IN THE SCHOOL
school.showMembers ()

