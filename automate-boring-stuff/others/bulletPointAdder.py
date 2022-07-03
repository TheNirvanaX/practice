# bulletPointAdder - Adds Wikipedia bullet points to the start of each line of text on the clipboard.

import pyperclip

text = [i.strip() for i in pyperclip.paste().split("\n")] # paste from clip board and split it
modified_text=[]
for line in text: # make bullets
    line="* "+line
    modified_text.append(line)
new_text="\n".join(modified_text) #join back to string
pyperclip.copy(new_text) 
