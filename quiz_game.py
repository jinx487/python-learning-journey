# Python quiz game 

questions = ("What is the longest river in the world?: ",
             "What is the smallest independent state in the world by both area and population?: ",
             "In which countrty will you find the ancient city of Machu Picchu?: ",
             "Which of these is a desert located in Africa?: ",
             "What is the capital city of Kenya?: ",
             "Mount Everest, the world highest peak, is located in which mountain range?: ",
             "Which country has the most natural lakes?: ",
             "Which European country is shaped like a boot?: ",
             "What is the world's largest ocean?: ",
             "The amazon rain forest is primarily located in which country?: ")

options = (("A.Amazon river", "B.Yangtze river", "C.Mississippi river", "D.Nile river"),
           ("A.Monaco", "B.Vatican", "C.San Marino", "D.Liechtenstein"),
           ("A.Mexico", "B.Colombia", "C.Peru", "D.Chile"),
           ("A.Gobi desert", "B.Atacama desert", "C.Arabian desert", "D.Sahara desert"),
           ("A.Nairobi", "B.Mombasa", "C.Nakuru", "D.Kisumu"),
           ("A.Andes", "B.Himalayas", "C.Rockies", "D.Alps"),
           ("A.Canada", "B.Russia", "C.Usa", "D.Brazil"),
           ("A.Spain", "B.Greece", "C.Italy", "D.Croatia"),
           ("A.Atlantic ocean", "B.Indian ocean", "C.Pacific ocean", "D.Artic ocean"),
           ("A.Peru", "B.Colombia", "C.Bolivia", "D.Brazil"))

answers = ("D", "B", "C", "D", "A", "B", "A", "C", "C", "D")
guesses = []
question_num = 0
score = 0 

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter a guess (A, B, C, D): ")
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]}, is the correct answer!")
    question_num += 1

print("-------------------------")
print("          RESULTS        ")
print("-------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int((score / question_num) * 100)
print(f"Your score is: {score}%")