# *Weekly Assignment: Quiz Game*

# Problem Statement:
# Create a simple command-line quiz game that reads questions from a file, allows users to answer them, and 
# provides a score at the end. The questions and answers should be stored in a text file.

# Question Class:

# Create a Question class with attributes like question_text and correct_answer. 
# Include methods to initialize the question and check if a provided answer is correct.

# File Handling:

# Use a text file (quiz_questions.txt) to store questions and answers. 
# Each line in the file represents a question with the format: <question_text>|<correct_answer>.

# Read Questions:

# Implement a function to read questions from the file and create instances of the Question class for each question.

# Quiz Game Loop:

# Create a loop that presents each question to the user, allows them to input their answer, checks if it's correct, and keeps track of their score.

# Score Calculation:

# Calculate and display the user's score at the end of the quiz.

# Error Handling:

# Implement error handling to handle cases where the file is not found or if there is an issue reading its content.

# Negative Marking:

# If there are 4 wrong answers in the quiz, 1 mark will be deducted.
# There will be no negative marking for one-word answers

import random
class question:
    
    # the cunstructor initialises the the dictionaries and the file from which we are reading
    # made separate dictionaries for mcq question,answers,one word question, answers
    def __init__(self,file1):
        self.file1=file1
        self.mcq=False
        self.one_word=False
        self.mcq_questions={}
        self.mcq_answers={}
        self.mcq_options={}
        self.one_word_questions={}
        self.one_word_answer={}
        self.neg=0
        self.mcq_mark=0
        self.one_word_mark=0
        
    # this fuction sort the mcq questions , answers and one word questions and answers into dictionaries
    def sort1(self):
        ques=False
        num=0
        for line in self.file1:

            if line.startswith("MCQ")==True :
                self.mcq=True
                self.one_word=False
                continue
            
            if line.startswith("One")==True:
                self.mcq=False
                self.one_word=True
                continue
            
            line=line.replace("\n","")
            data=line.split()

            if data[0].isnumeric() and data[len(data)-1]=='?':

                if self.mcq:
                    num=data[0]
                    self.mcq_questions[num]=line
                    ques=True

                elif self.one_word:
                    num=data[0]
                    self.one_word_questions[num]=line
                    
                
            elif data[0][0]=="A":
                if self.mcq:
                    self.mcq_answers[num]=data[1]
                    ques=False
                elif self.one_word:
                    line=line.lstrip("A")
                    self.one_word_answer[num]=line

            elif ques and data[0]!="A":
                if num in self.mcq_options:
                    self.mcq_options[num].append(line)
                else:
                    self.mcq_options[num]=[]
                    self.mcq_options[num].append(line)
    
    # this function matches the input answer to the correct answer for mcq questions
    def solve_mcq1(self,no,input1):
        if input1.strip().lower()==self.mcq_answers[no].strip().lower():
            self.mcq_mark+=1
            print("correct answer")
        else:
            print("Wrong answer")
            self.neg+=1

    # this function matches the input answer to the correct answer for one_word wuestions
    def solve_one_word(self,no,input1):
        if input1.strip().lower()==self.one_word_answer[no].strip().lower():
            self.one_word_mark+=1
            print("correct answer")
        else:
            print("wrong answer")
    
    # this function display mcq_questions and options
    def display_mcq(self,no):
        print(self.mcq_questions[no])
        l1=self.mcq_options[no]
        for i in l1:
            print(i)
    
    # this function display one word answer
    def display_one_word(self,no):
        print(self.one_word_questions[no])
    
    # this function calculate the final score
    def calculate_final_marks(self):
        res=(self.mcq_mark+self.one_word_mark) - (self.neg // 3  )
        print(f"final score achieved: {res}")



        
# main function         
if __name__=='__main__':
    try:
        path=r"D:\datasets2\mcq_quiz.txt"
        f=open(path,'r',encoding='utf8')
        a=question(f)
    except FileNotFoundError:             # exception handling for wrong path of file
        print("File not found or invalid path")
    else:
        a.sort1()
        mc=list(range(1,16))
        ow=list(range(1,15))

        print("MCQ QUESTIONS: ")
        while True:                           # solve mcq questions first
            a1=random.choice(mc)              # my logic for displaying random question
            mc.remove(a1)                      
            a1=str(a1)
            a.display_mcq(a1)

            while True:
                input_answer=input("Enter a,b,c or d as options: ")      # handling of invalid options in mcq
                if input_answer=='a' or input_answer=='b' or input_answer=='c' or input_answer=='d':
                    break
                else:
                    print("Invalid Input")
            
            # matching the user answer to the correct answer
            a.solve_mcq1(a1,input_answer)
            if not mc:
                break
        
        # same concept used for one word answers
        print("ONE WORD QUESTIONS: ")
        while True:
            a1=random.choice(ow)
            ow.remove(a1)
            a1=str(a1)
            a.display_one_word(a1)
            input_answer=input("enter text anwers: ")

            # matching the user answer to the correct answer
            a.solve_one_word(a1,input_answer)
            if not ow:
                break
        
        # calulate final score
        a.calculate_final_marks()
        f.close()