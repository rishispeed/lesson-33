import random 

import time

def comic_chatbox():
    print("I am comicbot,I am here to assist you")
    print("type bye to exit the session \n")

replies=("O really thats much . . . interesting ",
         "cool story by your side lets code",
         "you are much smarter","I love to talk to you , say more about it ")

while True:
    user = input("you:  ").lower()
    if user == "bye":
        print("Comicbot: thank you!This session has ended.")
        break

    time.sleep(0.5)
    print("COmicbot:", random.choice(replies))

comic_chatbox()
