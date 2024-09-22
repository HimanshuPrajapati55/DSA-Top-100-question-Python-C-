print("welcome to quiz game")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()

print("Lets Play")
score = 0
answer = input("what does CPU stand for?")
if answer.lower() == "central processing unit":
    print("correct")
    score += 1
    print("Score: ",score)
else:
    print("incoorect")
