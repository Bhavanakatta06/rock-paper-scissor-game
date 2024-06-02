import random
print("Winning rules:\nRock vs Paper -> Paper wins \nRock vs Scissors -> Rock wins \nPaper vs Scissors -> Scissor wins \n")
while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    userchoice = int(input("Enter your choice :"))
    while userchoice > 3 or userchoice < 1:
        userchoice = int(input('Enter a valid choice please '))
    if userchoice == 1:
        choice_name = 'Rock'
    elif userchoice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'
    print('User choice is \n', choice_name)
    print('Now its Computers Turn....')
    comp_choice = random.randint(1, 3)
    while comp_choice == userchoice:
        comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'RocK'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    print("Computer choice", comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)
    if userchoice == comp_choice:
        print('Its a Draw')
        result = "DRAW"
    if (userchoice == 1 and comp_choice == 2):
        print('paper wins')
        result = 'Paper'
    elif (userchoice == 2 and comp_choice == 1):
        print('paper wins')
        result = 'Paper'
    if (userchoice == 1 and comp_choice == 3):
        print('Rock wins')
        result = 'Rock'
    elif (userchoice == 3 and comp_choice == 1):
        print('Rock wins')
        result = 'RocK'
    if (userchoice == 2 and comp_choice == 3):
        print('Scissors wins')
        result = 'Scissors'
    elif (userchoice == 3 and comp_choice == 2):
        print('Scissors wins')
        result = 'Rock'
    if result == 'DRAW':
        print("Its a tie")
    if result == choice_name:
        print("User wins")
    else:
        print("Computer wins")
    print("Do you want to play again..(Y/N)")
    ans = input().lower()
    if ans == 'n':
        break
print("thanks for playing")
