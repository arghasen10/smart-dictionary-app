import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        response =  input("Did you mean %s instead.Enter Y if yes and N if No." %get_close_matches(w,data.keys())[0])
        if response == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        else:
            return "the word does not exist.Please Double check again."

    else:
        return "word does not exist.Please double check it"

word = input("Enter a word:")
output = translate(word)
for item in output:
    print(item)