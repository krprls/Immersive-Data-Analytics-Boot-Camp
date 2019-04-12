import random
import time
choices=[
"It is certain",
 "It is decidedly so",
"Without a doubt",
"Yes definitely",
"You may rely on it",
 "As I see it, yes",
 "Most likely",
 "Outlook good",
 "Yes",
"hazy, try again",
 "Signs point to yes",
"Reply hazy try again",
 "Ask again later",
 "Better not tell you now",
 "Cannot predict now",
"Concentrate and ask again",
 "Don't count on it",
 "My reply is no",
"My sources say no",
"Outlook not so good",
 "Very doubtful",
"Thank you for playing!",

]
while True:
    input("Ask the mighty 8-Ball a question\nOo")
    for i in range(0,3):
        print("Shaking{}".format("."*i))
        time.sleep(1)
    print(random.choice(choices))
