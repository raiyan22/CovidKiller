#print(input("Who is this?\n"))

#import sys
#print("good")
#for i in range(1,5,1):
#    print("\n")
#sys.exit()

#print("hello", end='\t')
#print("great")


#print('cat','dog','mouse', sep='\n')

#def lo():
#    return 4
#nu = lo()
#print(nu)

#def spam():
#    print(eggs) # global eggs    
#eggs = 90
#spam()
#
#def spam():
#    eggs = 50   # as i assign a value in eggs in the def scope eggs gets localized
#    print(eggs) # local eggs    
#eggs = 90
#spam()
# to use global var in local scope >>>
#def spam():
#    global eggs   ## this tells that the eggs we want is that global one 
#    eggs = "Hello"
#    print(eggs)
#eggs = 45
#spam()

# lists

# start from 13th video
#spam = ['cat','bat',56]
#print(spam[1])

import pyttsx3


pyttsx3.init()
voice = pyttsx3.init()
voice.say('I can speak')
#voice.runAndWait()





