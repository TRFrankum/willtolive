#This module was authored by Tyler Rincón Frankum
#The purpose of this module is to allow the user to inject random motivational messages into their test cases. 
#It's also funny to put "import willtolive" at the top of your code lul. 

import random
import csv

phrasesfile = open('phrases.csv', 'r')
phrases = list(csv.reader(phrasesfile, delimiter=','))

def motivate():
    randomchoice = random.randint(1,(len(phrases)-1))
    output = str(*phrases[randomchoice])
    print(f'\n{output}')
