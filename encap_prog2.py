class Student:
    def __init__(self,name,grade):
        self.name = name
        self.__grade = grade
    def set_grade(self,new_grade):
        self.__grade = new_grade
    def get_grade(self):
        return self.__grade
st = Student("john",85)
st.set_grade(95)
print(st.get_grade())
