from modules.emojimath import solveEmojiMath
from bomb.bomb import Bomb


while True:
    print("Enter 'q' to exit")
    print("I will ask you info about the bomb")
    sn = input("Whats the serial number: ")
    bat = int(input("How many batteries: "))
    hold = int(input("How many holders: "))
    print("Indicators, please type 'indicator lit/unlit'\ntype 'done' when there is no more indicators")
    indicator = input("Indicator: ")
    litIndicators = list()
    unlitIndicators = list()
    while indicator.lower().strip() != "done":
        i, t = indicator.split(" ")
        if t.lower().strip() == "unlit":
            unlitIndicators.append(i.lower().strip())
        else:
            litIndicators.append(i.lower().strip())
        indicator = input("Indicator: ")
    plates = int(input("How many plates: "))
    ports = list()
    print("I will ask you about indicators\nType 'done' when there are no more ports")
    port = input("Port: ")
    while port.lower().strip() != "done":
        ports.append(port.lower().strip())
        port = input("Port: ")
    bomb = Bomb(bat, hold, sn, unlitIndicators, litIndicators, ports, plates)
    module = input("What's the module: ")
    module = module.lower().replace(" ", "")
    if module == "emojimath":
        print("Solving emoji math")
        print(solveEmojiMath(input("What is the display saying: ")))
    elif (module == "q"):
        exit()
    else:
        print("Module doesn't exist yet")
