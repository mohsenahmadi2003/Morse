from data.data import DATA

"""
Text encryption to Morse
"""

def morse_encrypt(message: str):
    code = ""

    for char in message:
        if char != " ":
            code += DATA[char.upper()] + " "
        else:
            code += " "

    return code


"""
Unlock Morse code
"""


def morse_decrypt(code: str):
    message = ""
    code = code.split(" ")
    data_keys = list(DATA.keys())
    data_values = list(DATA.values())

    for char in code:
        if char != "":
            index = data_values.index(char.upper())
            message += data_keys[index]
        else:
            message += " "

    return message