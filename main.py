from modules.emojimath import solveEmojiMath
while True:
    print("Enter 'q' to exit")
    module = input("What's the module: ")
    module = module.lower().replace(" ", "")
    if module == "emojimath":
        print("Solving emoji math")
        print(solveEmojiMath(input("What is the display saying: ")))
    elif (module == "q"):
        exit()
    else:
        print("Module doesn't exist yet")
