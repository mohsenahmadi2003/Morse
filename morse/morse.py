from morse.data import DATA

"""
We do the following for the coder: 
>>> print(a:=morse_encrypt("abcd"))


To decode, we act as follows:
>>> print(morse_decrypt(a))
"""


"""
Text encryption to Morse
"""

def morse_encrypt(message: str) -> str:
    code:str = ""

    for char in message:
        if char != " ":
            code += DATA[char.upper()] + " "
        else:
            code += " "

    return code


"""
Morse code decoding
"""

def morse_decrypt(code: str) -> str:
    message:str = ""
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