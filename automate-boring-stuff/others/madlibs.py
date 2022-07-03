# mad libs without regex
import os
from pathlib import Path

os.chdir(r"F:/programming/code/automate-boring-stuff")
file_path=Path("F:/programming/code/automate-boring-stuff/"+input("Enter File Name:\n")+".txt")

file=open(file_path,"r")
fileobj=file.read()

newfile=""
start=0
for word in fileobj.split():
	if not word[-1].isalpha():
		word=word[:-1]
	if word in ["ADJECTIVE","NOUN","ADVERB","VERB"]:
		last=fileobj.find(word,start)
		newfile+=fileobj[start:last]+input(f"Enter {word}:")
		start=last+len(word)
		
newfile+=fileobj[start:]
file.close()
file=open(file_path,"w")
file.write(newfile)
file.close()
