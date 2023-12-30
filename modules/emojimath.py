import re


def solveEmojiMath(input: str) -> int:
    chars = {":)": 0,
             "=(": 1,
             "(:": 2,
             ")=": 3,
             ":(": 4,
             "):": 5,
             "=)": 6,
             "(=": 7,
             ":|": 8,
             "|:": 9}
    new = ""
    op = str()
    match = re.search(r"[\+\-*/]", input)
    if match:
        op = match.group()
    number1, number2 = input.split(op)
    for i in range(0, len(number1)-1, 2):
        new += str(chars.get(number1[i:i+2]))
    new += op
    for i in range(0, len(number2)-1, 2):
        new += str(chars.get(number2[i:i+2]))
    try:
        return f"The answer to emoji math is {eval(new)}"
    except:
        return "Was there a typo in the prompt\nTry again"
