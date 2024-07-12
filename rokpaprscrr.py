user_score = 0
comp_score = 0

while(True):

    n = input("choose-").lower()
    list_1= ['rock','paper','scissor']
    a = 'You Lose !!'
    b = 'You Win !!'
    import random
    l = random.choice(list_1)
    print(f"computer choose-{l}")
    
    if n=='rock' and l=='paper':
        print(a)
        comp_score+=1
    elif n=='scissor' and l=='paper':
        print(b)
        user_score+=1
    elif n=='paper' and l=='scissor':
        print(a)
        comp_score+=1
    elif n=='rock' and l=='scissor':
        print(b)
        user_score+=1
    elif n=='scissor' and l == 'rock':
        print(a)
        comp_score+=1
    elif n=='paper' and l == 'rock':
        print(b)
        user_score+=1
    else:
        print("Tie")
        
    print(f"Your score is {user_score} and computer score is {comp_score}.")
    x = input("Do you wanna play again yes/no = ").lower()
    if (x == 'no'):
        break
print("Game Over")
