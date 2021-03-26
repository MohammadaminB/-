import random
mark = 0

while (True):

    print ("mark : " +str (mark))

    choice = input ("1. stone \n2. paper \n3. Scissors \nto select : ")
    choice = int (choice)

    if (choice == 0) :
        break
    
    if (choice != 1) and (choice != 2) and (choice != 3):
        print ("entrance fee unrelibe")

    choicesystem = random.randint(1,3)
    x = ""

    if choicesystem == 1 : x = "stone"
    elif choicesystem == 2 : x = "paper"
    elif choicesystem == 3 : x = "Scissors"
    print ("choice system : "+x)

    if (choicesystem == 1 and choice == 2) or (choicesystem == 2 and choice == 3) or (choicesystem == 3 and choice == 1):
        print ("you're win")
        mark += 1

    elif (choicesystem == choice):
        print ("equal whit system")

    else :
        print ("game over")
        mark -= 1

    print ("\n") 