#programm for intermediate eliza application



dict = {"i": "you",
        "me": "you",
        "my": "your",
        "am": "are"}


while True:
    chat = input("Good day. What is your problem? Enter your response here or Q to quit: ")
    chatsplit = chat.split()
    for items in chat:
        if item == "i":
            chat.replace(item, dict['i'], value)
        elif item == "me":
            chat.replace(item, dict["you"], value)
        elif item == "my":
            chat.replace(item, dict["your"], value)
        else item == "am":
            chat.replace(item, dict["are"], value)
        print(chat)

    chatCont = input("Enter your response here or Q to quit: ")
    print(chatCont)

    if chatCont.upper().startswith("Q"):
        print("you exit to chat!")
        exit()
