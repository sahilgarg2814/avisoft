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
     
     # constructor for initialising objects or student records
     def __init__(self,name:str,age:int,gender:str,python_marks:int,dsa_marks:int,ml_marks:int):
          self.name=name
          self.age=age
          self.gender=gender
          self.python_marks=python_marks
          self.dsa_marks=dsa_marks
          self.ml_marks=ml_marks
     
     # calculate average marks of all subjects
     def calculate_average_marks(self):
          return (self.python_marks+self.dsa_marks+self.ml_marks)//3
     
     
     # set the minimum and maximum threshold for sorting of students based on their average marks
     @classmethod
     def set_maximum_minimum_threshold(cls,mini,maxi):
          cls.min_marks=mini
          cls.max_marks=maxi

     # set the  threshold for selecting the students who need personal attention
     @classmethod
     def set_personal_attention_threshold(cls,p):
          cls.Personal_attention_threshold=p
     

     # this function sort the students based on their averge marks into three lists namely above_max_threshold,
     # below_min_threshold and in_between_max_min_threshold
     def sorting_students(self):
          avg=self.calculate_average_marks()
          if avg < students.min_marks:
               students.student_below_minimum_threshold.append((avg,self.name))
          elif avg <= students.min_marks and avg >= students.max_marks:
               students.student_between_minimum_maximum_threshold.append((avg,self.name))
          else:
               students.student_above_maximum_threshold.append((avg,self.name))
     
     # this function form the list of the top 5 students from above_max threshold list
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
    

    # this function return the list of top 5 students
     @staticmethod
     def get_top_5():
          if students.top_5_students:
               return students.top_5_students
          else:
               return False
     
     # this function return the list of students who scored below minimum_threshold
     @staticmethod
     def get_minimum_list():
          if students.student_below_minimum_threshold:
               return students.student_below_minimum_threshold
          else:
               return False 
     # this function return the list of students who scored above maximum_threshold
     @staticmethod
     def get_maximum_list():
          if students.student_above_maximum_threshold:
               return students.student_above_maximum_threshold
          else:
               return False
     
     # this function return the list of students who scored in between minimum_threshold and maximum threshold
     @staticmethod
     def get_in_between_minimum_maximum_list():
          if students.student_between_minimum_maximum_threshold:
               return students.student_between_minimum_maximum_threshold
          else:
               return False
          
     # this function return the top students based on average marks
     @staticmethod
     def top_performer():
          if students.top_5_students:
               return students.top_5_students[0]
          else:
               return False
          
     #  this function makes the list of the students who need personal attention
     def Personal_attention(self):
          if self.dsa_marks<=students.Personal_attention_threshold  or self.ml_marks<=students.Personal_attention_threshold or self.python_marks<=students.Personal_attention_threshold:
               students.Personal_attention_list.append(self.name)

     # this function return the list of students who need personal attention
     @staticmethod
     def get_personal_attention_list():
          if students.Personal_attention_list:
               return students.Personal_attention_list
          else:
               return False         


     
     

     
# main function
if __name__=='__main__':

     obj_list=[]

     try:                            # enter the number of students records to enter
          n=int(input("enter the no. of students records to enter: "))
     except ValueError:
          print("Invalid Input")
          sys.exit()

     for obj in range(n):
          while True:
               try:           # initialising the attributes of the student objects like assinging them marks,name,age
                    name=input("Enter the name: ")
                    age=int(input("Enter the age (must be above 0 and less than 120): "))
                    gender=input("enter the gender(must be male,female and other): ")
                    python_marks=int(input("enter the python marks(must be between 0 and 100): "))
                    dsa_marks=int(input("enter the dsa marks(must be between 0 and 100): "))
                    ml_marks=int(input("enter the marks for machine learning(must be between 0 and 100): "))

               except ValueError:
                    print("Invalid Input")
                    sys.exit()
               
               else:
                    if (age in range(0,121)) and (gender.lower() in ['male','female','other']) and (python_marks in range(0,101)) and(dsa_marks in range(0,101)) and (ml_marks in range(0,101)):
                         break
                    else:
                         print("invalid inputs in the record of student.")
          

          obj=students(name,age,gender,python_marks,dsa_marks,ml_marks)
          obj_list.append(obj)  # entering each record in a list
     

     # entering the minimum and maximum thresholds for sorting
     while True:
          try:
               mi=int(input("enter the minmum threshold: "))
               ma=int(input("enter the maximum threshold: "))
               pa=int(input("enter the personal_attention threshold: "))
          except ValueError:
               print("invalid input")
          else:
               if mi in range(0,101) and ma in range(0,101) and pa in range(0,101) and mi<ma and pa<=mi:
                    break
               else:
                    print("in valid inputs in thresholds")
     students.set_maximum_minimum_threshold(mi,ma)
     students.set_personal_attention_threshold(pa)

    
     # performing sorting and personal_attention students on each student object in the obj_list
     for i in range(n):
          a1=obj_list[i]
          a1.sorting_students()
          a1.Personal_attention()
     students.top_5()

     
     # the layout of the program or menu of functions to perform
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