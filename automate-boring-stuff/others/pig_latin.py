# Pig latin - English to pig latin

print("Enter the English message to translate into Pig Latin")
vowels=["a","e","i","o","u","y"]
text=[i.strip() for i in input().split()]

def convert(word):
    if word[0].lower() in vowels:
        suffix=""
        while not word[-1].isalpha(): # remove non alphabetic character from suffix
            suffix+=word[-1]
            word=word[:-1]

        word=word+"yay"
        word+=suffix
    else:
        suffix=""
        while not word[-1].isalpha(): # remove non alphabetic character from suffix
            suffix+=word[-1]
            word=word[:-1]
        prefix=""
        while word[0].lower() not in vowels:
            prefix+=word[0]
            word=word[1:]

        word=word+prefix+"ay"+suffix
    return word

new_text=[]
for word in text:
    if word.istitle():
        word = convert(word).title()
    
    elif word.isupper():
        word = convert(word).upper()

    elif word.islower():
        word = convert(word).lower()
   
    new_text.append(word)

text_2 = " ".join(new_text)
print(text_2)