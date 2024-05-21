print("*********************")
print("welcome to my quiz Game")
question_bank=[
    {"text": "who is developed by python?","answer":"C"},
    {"text":"which of the extension of python file?","answer":"B"},
    {"text":"which keyword is used to define a fun?","answer":"A"},
    {"text":"which of the character is used for give a single line command in python?","answer":"C"},
    {"text":"What is the syntax to output 'Hello World' in python?","answer":"A"},
    {"text":"The ability of one class to acquire the properties of another class_____","answer":"A"},
    {"text":"which inheritance have multiple parent classes and single sub class","answer":"C"},
    {"text":"which of the function is the build in function i python?","answer":"A"},
    {"text":"is python code is compiled or interpreted?","answer":"B"},
    {"text":"Is python is case sensitive when dealing with identifiers?","answer":"B"},
]
options=[["A.Wick van Rossum","B.Rasmus lerdorf","C.Guido Van Rossum","D.Niene stom"],
         ["A.Python","B.Py","C.Pl","D.p"],
         ["A.Function","B.def","C.Fun","D.Define"],
         ["A.//","B./","C.#","D./*"],
         ["A.print()","B.system.out.print()","C.echo()","D.out.print()"],
         ["A.Inheritance","B.polymorphism","C.abstraction","D.encapsulation"],
         ["A.Factorial()","B.print()","C.seed()","D.sqrt()"],
         ["A.compiled","B.interpreted","C.complied and interpreted","D.none of the above"],
         ["A.no","B.yes","C.machine dependent","D.none of the mentioned"],
]
score=0
def check_answer(user_guess,correst_answer):
    if user_guess==correst_answer:
        return  True
    else:
        return False
for question_num in range(len(question_bank)):
    print("***********")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)
    guess=input("Enter the answer(A/B/C/D):").upper()
    is_correct=check_answer(guess,question_bank[question_num]["answer"])
    if is_correct:
        print("correct Answer")
        score+=1
    else:
        print('Incorrect Answer')
        print(f"the correct answer is {question_bank[question_num]["answer"]}")
    print(f"your current score is {score}/{question_num+1}")
print(f"Your have given {score} correct answers")
print(f"Your score is {(score/len(question_bank))*100}%")

