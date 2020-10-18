# interactive-dictionary
#A python dictionary

import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    close_match = get_close_matches(w, data.keys());
    if w in data:
        return data[w]
    elif len(close_match) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % close_match[0])
        if yn == "Y":
            return data[close_match[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

