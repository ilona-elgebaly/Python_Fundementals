class StudentGrades:
    def __init__(self):
        self.students={}
    def add_student(self,name,grade):
        if grade<0 or grade>100:
            raise ValueError("Grade must be between 0 and 100")
        self.students[name]=grade
    def get_grade(self,name):
        if name not in self.students:
            raise KeyError ("Student not found")
        return self.students[name]
    def get_average(self):
        if len(self.students)==0:
            raise Exception ("No students on the list")
        total = sum(self.students.values())
        return total/len(self.students)
    def __str__(self): 
        return "Class has " +str(len(self.students)) + " students. Average grade is " + str(self.get_average())
    
if __name__=="__main__":
    grades=StudentGrades()
    grades.add_student("Jan",89)
    grades.add_student("Kate",90)
    print(grades.get_grade("Jan"))
    print(grades.get_average())
    print(grades)

    try:
        grades.add_student("Ilona", 110)
    except ValueError as e:
        print(e)
    try:
        grades.get_grade("Suzan")
    except KeyError as e:
        print(e)
    try:
        grades.get_average()
    except Exception as e:
        print(e)


    