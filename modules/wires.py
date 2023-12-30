import re
from messages.messages import cutWire
from bomb.bomb import Bomb


def solveWires(bomb: Bomb, wires: list[str]) -> str:
    lastDigit = re.findall(r"\d", bomb.serialNumber)[-1]

    match(len(wires)):
        case 3:
            if "red" not in wires:
                return cutWire("second")
            elif wires[-1] == "white":
                return cutWire("last")
            elif wires.count("blue") > 1:
                return cutWire("last blue")
            else:
                return cutWire("last")
        case 4:
            if wires.count("red") > 1 and lastDigit % 2 == 1:
                return cutWire("last red")
            elif wires[-1] == "yellow" and wires.count("red") == 0:
                return cutWire("first")
            elif wires.count("blue") == 1:
                return cutWire("first")
            elif wires.count("yellow") > 1:
                return cutWire("last")
            else:
                return cutWire("second")
        case 5:
            if wires[-1] == "black" and lastDigit % 2 == 1:
                return cutWire("fourth")
            elif wires.count("red") == 1 and wires.count("yellow") > 1:
                return cutWire("first")
            elif wires.count("black") == 0:
                return cutWire("second")
            else:
                return cutWire("first")
        case 6:
            if wires.count("yellow") == 0 and lastDigit % 2 == 1:
                return cutWire("third")
            elif wires.count("yellow") == 1 and wires.count("white") > 1:
                return cutWire("fourth")
            elif wires.count("red") == 0:
                return cutWire("last")
            else:
                return cutWire("fourth")
        case _:
            return "There were too many or too little wire.\nAre you sure you chose thre right module."
