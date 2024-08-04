yeslsit = ["yes" , "y" , "no" , "n" ]
choiceList = ["A" , "B" , "C" , "D"]

#----------------------------------------------
def newgame():
   
   guesses = []
   correct_guesses = 0
   question_num = 1

   for key in question:
      
      guess = ""
      print("-------------------------------------")
      print(key)

      for i in options[question_num - 1]:
         print(i)
      
      while guess not in choiceList:
        guess = input("Enter (A , B , C or D) : ").upper()
      guesses.append(guess)
      question_num += 1
      correct_guesses += checkanswer(question.get(key) , guess)
   displayscore(correct_guesses , guesses)

#------------------------------------------------------

def checkanswer(answer , guess):
   if answer == guess:
      print("CORRECT")
      return 1
   else:
      print("WRONG")
      return 0
   
#------------------------------------------------------

def displayscore(correct_guesses , guesses):
    print("-------------------------------------")
    print("RESULTS")
    print("-------------------------------------")

    print("Answers: ")
    for i in question:
       print(question.get(i) , end=" ")
    print()

    print("Guesses: ")
    for i in guesses:
       print(i , end=" ")
    print()
    
    score = int((correct_guesses/len(question))*100)
    print("Your score is : " + str(score) + "%")

#------------------------------------------------------

def playagain():
   YesOrNo = ""
   while YesOrNo not in yeslsit:
      YesOrNo = input("Do you want to play again ? ").lower()

   if YesOrNo == "yes":
      newgame()
   elif YesOrNo == "y":
      newgame()
   else:
      print("Thanks for answering my quiz")

#------------------------------------------------------

question = {
   "Who is the Greatest Football Player ? " : "C" ,
   "Where is egypt ? " : "B" ,
   "Is the Earth flat ? " : "D" ,
   "What is the biggest company in the world ?" : "C"
} 

#------------------------------------------------------

options = [
   ["A. Messi" , "B. Zlatan" , "C. Cristiano Ronaldo" , "D. Antony"] ,
   ["A. Asia" , "B. Africa" , "C. Europe" , "D. S.America"] ,
   ["A. Yes" , "B. No" , "C. Sometimes" , "D. I am an Alein"] ,
   ["A. Nvidia" , "B. Microsoft" , "C. Apple" ,"D. Aramco"]
]

#------------------------------------------------------

newgame()

while playagain():
   newgame()

print("BYE , Thanks for answering my quiz \nCredit : Ahmed Fouad")