course_eval=open("shilling.txt", "w")
Q1=input("What did you like/dislike about Code Academy?")

Q2=input("What did you enjoy most about the class?")

Q3=input("How was the pace of the class?")

Q4=input("What would you change about the class?")

Q5=input("Would you recommend this class to a friend?")

answers=(Q1 + '\n' + Q2 + '\n' + Q3 + '\n' + Q4 + '\n' + Q5 + '\n')

course_eval.write(answers)

course_eval.close()
