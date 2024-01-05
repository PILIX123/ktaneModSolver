from modules.emojimath import solveEmojiMath
from modules.wires import solveWires
from modules.button import solveButton
from modules.simonsays import solveSimonSays
from bomb.bomb import Bomb


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
while True:
    module = input("What's the module: ")
    module = module.lower().replace(" ", "")
    match module:
        case "emojimath":
            print("Solving emoji math")
            print(solveEmojiMath(input("What is the display saying: ")))
        case "button":
            print("Solving button")
            color = input("Color of the button: ")
            text = input("What's the text on the button: ")
            print(solveButton(bomb, color, text))
        case "wires":
            print("Solving wires")
            print(
                "I will ask you the color of the wires type them in the order the defuser is telling them.\nType 'done' when there are no more wires.")
            wire = input("What color is the wire: ")
            wire = wire.strip().lower()
            wires = list()
            while wire != "done":
                wires.append(wire.lower().strip())
                wire = input("What color is the wire: ")
            print(solveWires(bomb, wires))
        case "simonsays":
            print("Solving Simon Says")
            strikes = int(input("How many strikes do you have?\n"))
            solveSimonSays(bomb, strikes)
        case "q":
            exit()
        case _:
            print("Module doesn't exist yet")
