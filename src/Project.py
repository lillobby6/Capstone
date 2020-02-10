import random
import os
import time

fileName = "file.cpp" #can be any cpp file in one directory above .vscode
master = f"g++ -std=c++1y {fileName}"
dic = { 1:"fauto-inc-dec", 2:"fbranch-count-reg", 3:"fcombine-stack-adjustments", 4:"fcompare-elim", 5:"fcprop-registers", 6:"fdce", 7:"fdefer-pop", 8:"fdelayed-branch", 9:"fdse", 10:"fforward-propagate", 11:"fguess-branch-probability", 12:"fif-conversion", 13:"fif-conversion2", 14:"finline-functions-called-once", 15:"fipa-profile", 16:"fipa-pure-const", 17:"fipa-reference", 18:"-fipa-reference-addressable", 19:"fmerge-constants", 20:"fmove-loop-invariants", 21:"fomit-frame-pointer", 22:"freorder-blocks", 23:"fshrink-wrap", 24:"fshrink-wrap-separate", 25:"fsplit-wide-types", 26:"fssa-backprop", 27:"fssa-phiopt", 28:"ftree-bit-ccp", 29:"ftree-ccp", 30:"ftree-ch", 31:"ftree-coalesce-vars", 32:"ftree-copy-prop", 33:"ftree-dce", 34:"ftree-dominator-opts", 35:"ftree-dse", 36:"ftree-forwprop", 37:"ftree-fre", 38:"ftree-phiprop", 39:"ftree-pta", 40:"ftree-scev-cprop", 41:"ftree-sink", 42:"ftree-slsr", 43:"ftree-sra", 44:"ftree-ter", 45:"funit-at-a-time", 46:"falign-functions", 47:"falign-jumps", 48:"falign-labels", 49:"falign-loops", 50:"fcaller-saves", 51:"fcode-hoisting", 52:"fcrossjumping", 53:"fcse-follow-jumps", 54:"fcse-skip-blocks", 55:"fdelete-null-pointer-checks", 56:"fdevirtualize", 57:"fdevirtualize-speculatively", 58:"fexpensive-optimizations", 59:"ffinite-loops", 60:"fgcse", 61:"fgcse-lm", 62:"fhoist-adjacent-loads", 63:"finline-functions", 64:"finline-small-functions", 65:"findirect-inlining", 66:"fipa-bit-cp", 67:"fipa-cp", 68:"fipa-icf", 69:"fipa-ra", 70:"fipa-sra", 71:"fipa-vrp", 72:"fisolate-erroneous-paths-dereference", 73:"flra-remat", 74:"foptimize-sibling-calls", 75:"foptimize-strlen", 76:"fpartial-inlining", 77:"fpeephole2", 78:"freorder-blocks-algorithm=stc", 79:"freorder-blocks-and-partition", 80:"freorder-functions", 81:"frerun-cse-after-loop", 82:"fschedule-insns", 83:"fschedule-insns2", 84:"fsched-interblock", 85:"fsched-spec", 86:"fstore-merging", 87:"fstrict-aliasing", 88:"fthread-jumps", 89:"ftree-builtin-call-dce", 90:"ftree-pre", 91:"ftree-switch-conversion", 92:"ftree-tail-merge", 93:"ftree-vrp"}
 

def mutate(s: str, chance: int):
    ret = ''
    for i in s:
        r = random.randint(0, chance)
        if r == 0:
            if i == '0':
                ret += '1'
            elif i == '1':
                ret += '0'
        else:
            ret += i
    return ret

def breed(s: str, s2: str, chance: int):
    ret = ''
    for i in range(len(s)):
        if random.randint(0, 1) == 0:
            ret += s[i]
        else:
            ret += s2[i]
    return mutate(ret, chance)

def score(s: str):
    t = ' '
    for i in range(len(s)):
        if s[i] == 1:
            t += f"-{dic[i]} "
    os.system(master + t)
    timels = []
    for i in range(20):
        start = time.time()
        os.system("a.exe")
        end = time.time()
        elapsed = end - start
        timels.append(elapsed)
    score = sum(timels)/len(timels)
    return score

def main():
    generation = 0
    populationSize = 30
    masterLs = []
    ls = []
    for i in range(populationSize):
        s = ''
        for i in range(len(dic)):
            s += str(random.randint(0, 1))
        ls.append(s)
    scoredLs = []
    for i in ls:
        scoredLs.append((score(i), i))
    sortedLs = sorted(scoredLs)
    for i in range(len(ls)):
        ls[i] = sortedLs[i][1]
    masterLs.append(sortedLs[0][1])
    while generation < 20:
        print(f"Current fastest is {sortedLs[0][1]} with a timescore of {sortedLs[0][0]} in generation {generation}.")
        for i in range(populationSize//2):
            x = populationSize - i - 1
            p1 = ls[random.randint(0, populationSize//2 - 1)]
            p2 = ls[random.randint(0, populationSize//2 - 1)]
            child = breed(p1, p2, 5)
            ls[x] = child
        scoredLs = []
        for i in ls:
            scoredLs.append((score(i), i))
        sortedLs = sorted(scoredLs)
        for i in range(len(ls)):
            ls[i] = sortedLs[i][1]
        masterLs.append(sortedLs[0][1])
        generation += 1
    print(f"Fastest found is {sortedLs[0][1]} with a timescore of {sortedLs[0][0]} after {generation} generations.")
    masterScoredLs = []
    for i in masterLs:
        masterScoredLs.append((score(i), i))
    masterSortedLs = sorted(masterScoredLs)
    print(f"Given the fastest from each previous generation another option of the fastest is {masterSortedLs[0][1]} with a timescore of {masterSortedLs[0][0]}.")
    

if __name__ == "__main__":
    main()
