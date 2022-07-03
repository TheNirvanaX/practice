import sys
import time
indent=0 #number of indentaion
indentation_status=True #status of indentation, True->increasing: False->Decreasing

try:
    while True: #main loop
        print(" "*indent,end="")
        print("**********")
        time.sleep(0.03)

        if indentation_status: #increase indentation
            indent+=1
            if indent==20:
                indentation_status=False
        else: #decrease indentation
            indent-=1
            if indent==0:
                indentation_status=True
except KeyboardInterrupt: #exit program if user interrupt
    sys.exit()