# mcb.pyw - mcbshelfs and loads pieces of text to the clipboard.
# Usage: python mcb.pyw save <keyword> - saves clipboard to keyword.
#        python mcb.pyw <keyword> - Loads keyword to clipboard.
#        python mcb.pyw list - Loads all keywords to clipboard.
#        python mcb.pyw delete <keyword> - delete keyword 
#        python mcb.pyw delete - delte all keywords

import pyperclip
import sys
import shelve,os

from requests import delete

try:
    os.makedirs(r"F:/programming/code/automate-boring-stuff/file")
finally:
    os.chdir(r"F:/programming/code/automate-boring-stuff/file")

mcbShelf=shelve.open("mcbFile")

def formatdisp():           # display format message when input format is incorrect.
    print('''
Usage:     * python mcb.pyw save <keyword>     - saves clipboard to keyword.
           * python mcb.pyw <keyword>          - Loads keyword to clipboard.      
           * python mcb.pyw list               - Loads all keywords to clipboard.
           * python mcb.pyw delete <keyword>   - delete keyword. 
           * python mcb.pyw delete             - delte all keywords.
''')

def delete(keyword):        # keyword delete function
    if keyword.lower()=="all":
        for i in list(mcbShelf.keys()):
            del mcbShelf[i]
    else:
        try:
            del mcbShelf[keyword]
        except:
            print(f"keyword <{keyword}> is not found!")

# main program
if len(sys.argv)==3: 
    if sys.argv[1].lower()=="save":
        mcbShelf[sys.argv[2]]=pyperclip.paste()
    elif sys.argv[1].lower()=="delete":
        delete(sys.argv[2])
    else:
        formatdisp()


elif len(sys.argv)==2:
    if sys.argv[1].lower()=="list":
        keywords="\n".join(list(mcbShelf.keys()))
        if keywords=="":                  # no keyword in list
            print("\nNo keyword found! please save new keywords")
            formatdisp()
        else: 
            pyperclip.copy(keywords)
    else:
        try:
            pyperclip.copy(mcbShelf[sys.argv[1]])       # retrive keyword from mcbShelf
        except:
            print(f"keyword <{sys.argv[1]}> is not found!")  # keyword not found!
else:
    formatdisp()  # display format -> for incorrect input    

mcbShelf.close()