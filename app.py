import json
data = json.load(open("data.json"))

def translate(w):
    if w in data:
        return data[w]
    else:
        print("word does not exist.Please double check it")

word = input("Enter a word:")
print(translate(word.lower()))