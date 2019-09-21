def do_calculation():
    print("Let's " + answer + " some numbers!")
    input1 = input("n1 = ")
    input2 = input("n2 = ")
    n1 = int(input1)
    n2 = int(input2)
    if answer == "add":
        result = n1 + n2
    elif answer == "multiply":
        result = n1 * n2
    output = str(result)
    if answer == "add":
        print(input1 + "+" + input2 + "= " + output)
    elif answer == "multiply":
        print(input1 + "*" + input2 + "= " + output)
        
finished = False 
while finished == False: 
    print("Hi! I'm calculator-bot")
    answer = input("Ready to work! What should I do?<> ")
    if answer == "add":
        do_calculation()
    elif answer == "multiply":
        do_calculation()
    elif answer == "average":
        how_many = input("How many number you will use? >> ")
        how_many = int(how_many)
        total = 0
        for count in range(how_many):
            number = input("Enter number >")
            total = total + int(number)
            result = total / how_many
        print("the average is " + str(result))
    elif answer == "bye":
        finished = True
        print("Bye! See you!")
    else:
        print("Just add, multiply or average. Choose again, please! Or say bye!")