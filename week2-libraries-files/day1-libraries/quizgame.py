#quiz that is randomly shuffled
# 11/11/25
#time spent: 30min

import random 

#create a list and then randomize it 
quizQandA = {}

try:
  def print_error(e): 
    print(f"Error: {e}")
    print("Please try again.")

  def another_question():
    while True:
      try:
        another = input("Would you like to add another question?(y/n): ")
        if another != 'y' and another != 'n':
          raise ValueError("Input has to be 'y' or 'n'." )
      except ValueError as e:
        print_error(e)
      else: break
    if another == 'y': return True
    else: return False
      
  def create_questions(): 
    while True: 
      while True:
        try:
          question = input("Add a question: ").strip().capitalize()
          if len(question) == 0:
            raise ValueError("Question can't be left empty.")
        except ValueError as e:
          print_error(e)
        else: break

      while True: 
        try:
          create_answer = input("What is the answer?: ").strip().capitalize()
          if len(create_answer) == 0:
            raise ValueError("Answer can't be left empty.")
        except ValueError as e:
          print_error(e)
        else: break
      quizQandA[question] = create_answer

      if another_question() == True: continue 
      else: break

  def grade_respose(quizgrade):
    if quizgrade > 89:
      print("Nice work you got an A!")
    elif quizgrade > 79:
      print("Good job you got a B!")
    elif quizgrade > 69:
      print("You got a C.")
    elif quizgrade > 59:
      print("You got a D. You will have to retake the test.")
    else: 
      print("You got an F. You will have to retake the test.")

    

  def main():
    quizscore = 0
    create_questions()
    
    #make the dictionary into a list that can be shuffled
    quiz = list(quizQandA.items())
    random.shuffle(quiz)

    for i, (question, create_answer) in enumerate(quiz, 1):
      print(f"{i}. {question}")
      answer = input("What is the answer?: ").strip().capitalize()

      if answer == create_answer:
        quizscore += 1
        print("Correct!")
      else:
        print(f"Wrong. The answer is {create_answer}.")
    
    quizgrade = (quizscore / len(quiz)) * 100

    print(f"Your final grade on the quiz is {quizgrade:.1f}%.")
    grade_respose(quizgrade)
      

  main()
except KeyboardInterrupt:
  print("Quiz interrupted.")