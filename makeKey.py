import random
import json

jsonKey = {
    "a": "a",
    "b": "b",
    "c": "c",
    "d": "d",
    "e": "e",
    "f": "f",
    "g": "g",
    "h": "h",
    "i": "i",
    "j": "j",
    "k": "k",
    "l": "l",
    "m": "m",
    "n": "n",
    "o": "o",
    "p": "p",
    "q": "q",
    "r": "r",
    "s": "s",
    "t": "t",
    "u": "u",
    "v": "v",
    "w": "w",
    "x": "x",
    "y": "y",
    "z": "z"
}

def makeKey(chatName: str, Random=1):
    keys = list(jsonKey.keys())
    values = list(jsonKey.values())

    random.shuffle(values)
    rnd = dict(zip(keys, values))
    rev_rnd = dict(zip(values, keys))
    
    with open(f"./chats/{chatName}/key.json", 'w', encoding='utf-8') as nJson:
        json.dump(rnd, nJson, indent=4, ensure_ascii=False)

    with open(f"./chats/{chatName}/reverse.key.json", 'w', encoding='utf-8') as revKey:
        json.dump(rev_rnd, revKey, indent=4, ensure_ascii=False)

def executeKey(chatName: str, text: str) -> str:
    convStr = ""
    with open(f'./chats/{chatName}/key.json', 'r', encoding='utf-8') as jsn:
        dataKey = json.load(jsn)

        keyKeys = list(dataKey.keys())
        for char in text.lower():
            if char in keyKeys:
                convStr += dataKey[char]

            else:
                convStr += char

    return convStr

def reverseKey(chatName: str, text: str) -> str:
    convStr = ""
    with open(f'./chats/{chatName}/reverse.key.json', 'r', encoding='utf-8') as jsn:
        dataKey = json.load(jsn)

        keyKeys = list(dataKey.keys())
        for char in text.lower():
            if char in keyKeys:
                convStr += dataKey[char]

            else:
                convStr += char

    return convStr