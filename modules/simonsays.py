import re
from bomb.bomb import Bomb


def printAnswers(answers: list):
    print("Tap the colors in the following order.")
    for color in answers:
        print(color, end=" ")


def solveSimonSays(bomb: Bomb, strikes: int) -> str:
    answerSequence = list()
    print("Type done when the module is solved")
    latestColor = input("Whats the last color in the sequence: ")
    latestColor = latestColor.strip().lower()

    vowel = len(re.findall("a|e|i|o|u", bomb.serialNumber)) > 0
    while latestColor != "done":
        if vowel:
            match latestColor:
                case "red":
                    match strikes:
                        case 0:
                            answerSequence.append("blue")
                            printAnswers(answerSequence)
                        case 1:
                            answerSequence.append("yellow")
                            printAnswers(answerSequence)
                        case 2:
                            answerSequence.append("green")
                            printAnswers(answerSequence)
                case "blue":
                    match strikes:
                        case 0:
                            answerSequence.append("red")
                            printAnswers(answerSequence)
                        case 1:
                            answerSequence.append("green")
                            printAnswers(answerSequence)
                        case 2:
                            answerSequence.append("red")
                            printAnswers(answerSequence)
                case "green":
                    match strikes:
                        case 0:
                            answerSequence.append("yellow")
                            printAnswers(answerSequence)
                        case 1:
                            answerSequence.append("blue")
                            printAnswers(answerSequence)
                        case 2:
                            answerSequence.append("yellow")
                            printAnswers(answerSequence)
                case "yellow":
                    match strikes:
                        case 0:
                            answerSequence.append("green")
                            printAnswers(answerSequence)
                        case 1:
                            answerSequence.append("red")
                            printAnswers(answerSequence)
                        case 2:
                            answerSequence.append("blue")
                            printAnswers(answerSequence)
        else:
            match latestColor:
                case "red":
                    match strikes:
                        case 0:
                            answerSequence.append("blue")
                            printAnswers(answerSequence)
                        case 1:
                            answerSequence.append("red")
                            printAnswers(answerSequence)
                        case 2:
                            answerSequence.append("yellow")
                            printAnswers(answerSequence)
                case "blue":
                    match strikes:
                        case 0:
                            answerSequence.append("yellow")
                            printAnswers(answerSequence)
                        case 1:
                            answerSequence.append("blue")
                            printAnswers(answerSequence)
                        case 2:
                            answerSequence.append("green")
                            printAnswers(answerSequence)
                case "green":
                    match strikes:
                        case 0:
                            answerSequence.append("green")
                            printAnswers(answerSequence)
                        case 1:
                            answerSequence.append("yellow")
                            printAnswers(answerSequence)
                        case 2:
                            answerSequence.append("blue")
                            printAnswers(answerSequence)
                case "yellow":
                    match strikes:
                        case 0:
                            answerSequence.append("red")
                            printAnswers(answerSequence)
                        case 1:
                            answerSequence.append("green")
                            printAnswers(answerSequence)
                        case 2:
                            answerSequence.append("red")
                            printAnswers(answerSequence)

        latestColor = input("Whats the last color in the sequence: ")
        latestColor = latestColor.strip().lower()
