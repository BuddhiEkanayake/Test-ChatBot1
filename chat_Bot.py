while True:
    user_input = input("You:") . lower()
    if "hi" in user_input :
        print("Hellow! welcome to the chatbot.")

    elif "how are you" in user_input:
        print("I'm Great ! Hope you are well,")

    elif "bye" in user_input:
        print("Good bye!")
        break
    else:
        print("I'm sorry, I don't understand that.")