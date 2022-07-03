# renameDates - this program renames files with american-style dates to 
# european-style Dates

import os, shutil, re
from pathlib import Path

os.chdir(r"F:/programming/dataset/Files")

# create Regex object
fileRegex=re.compile(r'''
    ([0-1]?\d)      # month
    -        # seperator
    ([0-3]?\d)      # day
    -        # seperator
    (\d{4})         # year
    ''',re.VERBOSE)

# search date and replace
def dateSeRe(text):
    mo=fileRegex.search(text)
    if mo==None: 
        return None
    month=mo.group(1)
    if len(month)<2: month="0"+month
    day = mo.group(2)
    if len(day)<2: day="0"+day
    year= mo.group(3)

    #replace
    newtext= day+"-"+month+"-"+year
    return re.sub(fileRegex,newtext,text)
    

# main program
for file in os.listdir("."):
    new_Name=dateSeRe(file)
    
    if new_Name==None:
        continue
    
    # get full path
    absWd=os.path.abspath(".")
    AmericanStyle=os.path.join(absWd,file)
    EuropianStyle=os.path.join(absWd,new_Name)
    
    # rename
    print(f'Renaming "{AmericanStyle}" to "{EuropianStyle}"...')
    shutil.move(AmericanStyle,EuropianStyle)