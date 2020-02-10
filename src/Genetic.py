import math
import random   

def mutate(string: str):
    match = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,!?'1234567890-():;" \n"""
    num = random.randint(0, len(string)-1)
    num2 = random.randint(0, 1)
    if num2 == 0:
        newn = match[match.find(string[num]) - 1]
    else:
        newne = match.find(string[num]) + 1
        if newne == len(match):
            newn = match[0]
        else:
            newn = match[match.find(string[num]) + 1]
    newstring = ''
    for j in range(len(string)):
        if j == num:
            newstring += newn
        else:
            newstring += string[j]
    if random.randint(0, 3) == 0:
        newstring = mutate(newstring)
    return newstring

def mutate2(string: str, chance=3):
    match = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,!?'1234567890-():;" \n"""
    num = random.randint(0, len(string)-1)
    newn = match[random.randint(0, len(match)-1)]
    newstring = ''
    for j in range(len(string)):
        if j == num:
            newstring += newn
        else:
            newstring += string[j]
    if random.randint(0, chance) == 0:
        newstring = mutate2(newstring, chance)
    return newstring

def mutate3(string: str, chance = 3):
    match = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,!?'1234567890-():;" \n"""
    num = random.randint(0, len(string)-1)
    newn = match[random.randint(0, len(match)-1)]
    newstring = string.replace(string[num], '', 1)
    newstring += newn
    if random.randint(0, chance) == 0:
        newstring = mutate2(newstring, chance)
    return newstring

def mutate4(string: str, chance = 3):
    match = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,!?'1234567890-():;" \n"""
    string2 = ''
    for i in range(len(string)):
        if random.randint(0, chance) == 0:
            string2 += match[random.randint(0, len(match)-1)]
        else:
            string2 += string[i]
    return string2

def crossOver(word1: str, word2: str, chance=3):
    name = ''
    num1 = random.randint(0, len(word1))
    done = False
    while(not done):
        num2 = random.randint(0, len(word1))
        if not (num2 > num1):
            done = True
    for i in range(0, num2):
        if random.randint(0, 1) == 0:
            name += word1[i]
        else:
            name += word2[i]
    if random.randint(0, 1) == 1:
        name += word1[num2:num1+num2]
    else:
        name += word2[num2:num1+num2]
    for i in range(num1+num2, len(word1)):
        if random.randint(0, 1) == 0:
            name += word1[i]
        else:
            name += word2[i]
    if random.randint(0, chance) == 0:
        if random.randint(0, 1) == 0:
            crossOver(name, word1)
        else:
            crossOver(name, word2)
    return name

def mate(word1: str, word2: str):
    name = ''
    score = 0
    mutateChance = len(word1)//9
    crossOverChance = len(word1)//9
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            score += 1
    if score >= (9*len(word1))//10:
        mutateChance = len(word1)//8
        crossOverChance = len(word1)//8
    for i in range(len(word1)):
        if random.randint(0, 1) == 0:
            name += word1[i]
        else:
            name += word2[i]
    name = mutate2(name, 2)
    # num = random.randint(0, 1)
    # if num == 0: #mutate v2
    #     for i in range(len(word1)):
    #         if random.randint(0, 1) == 0:
    #             name += word1[i]
    #         else:
    #             name += word2[i]
    #     name = mutate2(name, mutateChance)
    # elif num == 1: #cross over and mutate
    #     name = crossOver(word1, word2, crossOverChance)
    #     name = mutate2(name, mutateChance)
    return name

def main():
    num = 0
    total = 0
    gens = []
    while(num < 10):
        match = """Hello there, General Kenobi."""
        length = len(match)
        lst = []
        for i in range(100):
            name = ''
            for i in range(length):
                    add = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,!?'1234567890-():;" \n"""
                    x = random.randint(0, len(add)-1)
                    name += add[x]
            lst.append(name)
        lstmatch = []
        for i in lst:
            score = 0
            for j in range(len(i)):
                if i[j] == match[j]:
                    score += 1
            lstmatch.append((score, i))
        srt = sorted(lstmatch, key=lambda x: x[0])
    
    
        correct = False
        generation = 0
        while(not correct):
            print(f"""Current most accurate is "{srt[99][1]}" in Generation {generation} with a score of {srt[99][0]}.""")
            generation += 1
            lst = [word for num, word in srt]
            for i in range(0, 49):
                parent1 = lst[random.randint(50, 99)]
                parent2 = lst[random.randint(50, 99)]
                lst[i] = mate(parent1, parent2)
            lstmatch = []
            for i in lst:
                score = 0
                for j in range(len(i)):
                    if i[j] == match[j]:
                        score += 1
                lstmatch.append((score, i))
            srt = sorted(lstmatch, key=lambda x: x[0])
            if(srt[99][0] == length):
                correct = True
        print(f"""Found correct answer, "{srt[99][1]}", in {generation} generations.""")
        num+=1
        total+=generation
        gens.append(generation)
    print(f"On average, finding the correct answer took {total/num} generations for {num} repetitions.")
    gens = sorted(gens)
    print(f"The longest time was {gens[len(gens)-1]} generations and the shortest was {gens[0]}.")

if __name__ == "__main__":
    main()