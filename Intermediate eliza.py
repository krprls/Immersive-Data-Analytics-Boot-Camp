
dict = {"i": "you",
        "me": "you",
        "my": "your",
        "am": "are"}


while True:
    chat = input("Good day. What is your problem? Enter your response here or Q to quit: ")
    chatsplit = chat.split()
    newStr = " "

    for item in chatsplit:
        if item == "i":
           print(dict["i"]) 
        elif item == "me":
            print(dict["me"])
        elif item == "my":
            print(dict["my"])
        elif item == "am":
           print(dict["am"])

        newStr = newStr + " "
        print(newStr)

    chatCont = input("Enter your response here or Q to quit: ")
    print(chatCont)

    if chatCont.upper().startswith("Q"):
        print("you exit to chat!")
        exit()
