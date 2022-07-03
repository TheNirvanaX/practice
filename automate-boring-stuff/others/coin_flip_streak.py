from ntpath import join
import random

#part-1 generate randomly selected 'heads' and 'tails' value.
event = [random.choice(["H","T"]) for i in range(10000)]
#print(event)

#part-2 check streak of 6 heads or tails.
strg= "".join(event)
streak_of_six=strg.count("HHHHHHH")+strg.count("TTTTTT")
print("chance of streak: "+str(streak_of_six*6/100))