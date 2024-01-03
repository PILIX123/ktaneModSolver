from bomb.bomb import Bomb


def solveStrip() -> str:
    print("Press and hold the button")
    strip = input("Color of the strip: ")
    strip = strip.strip().lower()
    match strip:
        case "blue":
            return "Release when the countdown timer has a 4 in any position."
        case "white":
            return "Release when the countdown timer has a 1 in any position."
        case "yellow":
            return "Release when the countdown timer has a 5 in any position."
        case _:
            return "Release when the countdown timer has a 1 in any position."


def solveButton(bomb: Bomb, color: str, text: str) -> str:
    color = color.lower().strip()
    text = text.lower().strip()
    if color == "blue" and text == "abort":
        return solveStrip()
    elif bomb.batteriesAA + bomb.batteriesD < 1 and text == "detonate":
        return "Tap the button."
    elif color == "white" and bomb.indicatorsLit.count("car") >= 1:
        return solveStrip()
    elif bomb.batteriesAA + bomb.batteriesD > 2 and bomb.indicatorsLit.count("frk") >= 1:
        return "Tap the button."
    elif color == "yellow":
        return solveStrip()
    elif color == "red" and text == "hold":
        return "Tap the button."
    else:
        return solveStrip()
