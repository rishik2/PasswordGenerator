# Readable password generator in the format  words + num + character
# eg (Skylight4@)
import random


with open ('PasswordGenerator/poems.txt' , 'r') as f:
    lines = f.readlines()
    
    
    
    char = ['@', '!', '$', '^', '*', '#']


    words_ls_4 = []


    for line in lines:
        words_ls = line.split()

        for word in words_ls:
            if len(word) > 4:
                words_ls_4.append(word)
     
    
    passw = random.choice(words_ls_4)+ str(random.randint(1,999)) + random.choice(char)

    print(passw)          
