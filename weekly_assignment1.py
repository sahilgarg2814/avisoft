import sys
class students:
     min_marks=0
     max_marks=0
     student_below_minimum_threshold=[]
     student_above_maximum_threshold=[]
     student_between_minimum_maximum_threshold=[]
     top_5_students=[]
     Personal_attention_list=[]
     Personal_attention_threshold=0

     def __init__(self,name:str,age:int,gender:str,python_marks:int,dsa_marks:int,ml_marks:int):
          self.name=name
          self.age=age
          self.gender=gender
          self.python_marks=python_marks
          self.dsa_marks=dsa_marks
          self.ml_marks=ml_marks
     
     def calculate_average_marks(self):
          return (self.python_marks+self.dsa_marks+self.ml_marks)//3
     
     @classmethod
     def set_maximum_minimum_threshold(cls,mini,maxi):
          cls.min_marks=mini
          cls.max_marks=maxi
     
     @classmethod
     def set_personal_attention_threshold(cls,p):
          cls.Personal_attention_threshold=p
     
     def sorting_students(self):
          avg=self.calculate_average_marks()
          if avg < students.min_marks:
               students.student_below_minimum_threshold.append((avg,self.name))
          elif avg <= students.min_marks and avg >= students.max_marks:
               students.student_between_minimum_maximum_threshold.append((avg,self.name))
          else:
               students.student_above_maximum_threshold.append((avg,self.name))
     
     @staticmethod
     def top_5():
          l=len(students.student_above_maximum_threshold)
          students.student_above_maximum_threshold.sort()
          if l<6:
               students.top_5_students=students.student_above_maximum_threshold
               students.top_5_students.reverse()
               return students.top_5_students
          else:
               students.top_5_students=students.student_above_maximum_threshold[l-5:]
               students.top_5_students.reverse()
               return students.top_5_students

     @staticmethod
     def get_top_5():
          if students.top_5_students:
               return students.top_5_students
          else:
               return False

     @staticmethod
     def get_minimum_list():
          if students.student_below_minimum_threshold:
               return students.student_below_minimum_threshold
          else:
               return False 
     
     @staticmethod
     def get_maximum_list():
          if students.student_above_maximum_threshold:
               return students.student_above_maximum_threshold
          else:
               return False
     
     @staticmethod
     def get_in_between_minimum_maximum_list():
          if students.student_between_minimum_maximum_threshold:
               return students.student_between_minimum_maximum_threshold
          else:
               return False
          
     
     @staticmethod
     def top_performer():
          if students.top_5_students:
               return students.top_5_students[0]
          else:
               return False

     def Personal_attention(self):
          if self.dsa_marks<=students.Personal_attention_threshold  or self.ml_marks<=students.Personal_attention_threshold or self.python_marks<=students.Personal_attention_threshold:
               students.Personal_attention_list.append(self.name)

     @staticmethod
     def get_personal_attention_list():
          if students.Personal_attention_list:
               return students.Personal_attention_list
          else:
               return False         


     
     

     

if __name__=='__main__':
     obj_list=[]
     n=int(input("enter the no. of students records to enter: "))
     for obj in range(n):
          name=input("Enter the name: ")
          age=int(input("Enter the age: "))
          gender=input("enter the gender: ")
          python_marks=int(input("enter the python marks: "))
          dsa_marks=int(input("enter the dsa marks: "))
          ml_marks=int(input("enter the marks for machine learning: "))
          obj=students(name,age,gender,python_marks,dsa_marks,ml_marks)
          obj_list.append(obj)
     
     mi=int(input("enter the minmum threshold: "))
     ma=int(input("enter the maximum threshold: "))
     pa=int(input("enter the personal_attention threshold: "))
     students.set_maximum_minimum_threshold(mi,ma)
     students.set_personal_attention_threshold(pa)

     for i in range(n):
          a1=obj_list[i]
          a1.sorting_students()
          a1.Personal_attention()
     students.top_5()

     while True:
          print("1. print top 5 students: ")
          print("2. print top performer: ")
          print("3. print personal attention list: ")
          print("4. print above above threshold list: ")
          print("5. print below minimum threshold list: ")
          print("6. print between minimum and maximum list: ")
          print(" print anything other than 0 to 6 to exit the program.")

          option=int(input("enter the option: "))
          if option==1:
               print(students.get_top_5())
          elif option==2:
               print(students.top_performer())
          elif option==3:
               print(students.get_personal_attention_list())
          elif option==4:
               print(students.get_maximum_list())
          elif option==5:
               print(students.get_minimum_list())
          elif option==6:
               print(students.get_in_between_minimum_maximum_list())
          else:
               sys.exit()