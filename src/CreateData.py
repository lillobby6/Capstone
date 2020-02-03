import random
import shutil
import os

def main():
    count = 0
    os.mkdir('files')
    os.mkdir('files/train')
    os.mkdir('files/test')
    os.mkdir('files/validate')
    os.mkdir('files/train/original')
    os.mkdir('files/train/compare')
    os.mkdir('files/train/answer')
    os.mkdir('files/test/original')
    os.mkdir('files/test/compare')
    os.mkdir('files/test/answer')
    os.mkdir('files/validate/original')
    os.mkdir('files/validate/compare')
    while(count <= 10000):
        
        q = random.randint(20, 60)
        d = random.randint(0, 1)
        print(count)
        file = open('original' + str(count) + ".txt", 'w+')
        sss = ''
        for i in range(0, q):
            r = random.randint(0, 25)
            ls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            sss += ls[r]
        
        print(f"Adding training string: {sss} to original file #{count}.")
        file.write(''.join(format(ord(i), 'b') for i in f"""print("{sss}")"""))
        file.close()
        shutil.move('original' + str(count) + ".txt", 'files/train/original')
        if d == 0:
            abl = ''
            file = open('compare' + str(count) + '.txt', 'w+')
            for i in sss:
                abl += f"""print("{i}")\n"""
            print(f"Adding training string: {abl} to compare file #{count}.")
            file.write(''.join(format(ord(i), 'b') for i in abl))
            file.close()
            shutil.move('compare' + str(count) + ".txt", 'files/train/compare')
        else:
            abl = ''
            oop = random.randint(1, len(sss))
            for i in range(0, oop):
                r = random.randint(0, len(sss))
                abl = sss.replace(sss[r:r+1], '', 1)
            file = open('compare' + str(count) + '.txt', 'w+')
            qbl = ''
            for i in abl:
                qbl += f"""print("{i}")\n"""
            print(f"Adding training string: {qbl} to compare file #{count}.")
            file.write(''.join(format(ord(i), 'b') for i in qbl))
            file.close()
            shutil.move('compare' + str(count) + ".txt", 'files/train/compare')
        file = open('answer' + str(count) + '.txt', 'w+')
        if d == 0:
            file.write('True')
            t = True
        else:
            file.write('False')
            t = False
        print(f"Adding training boolean: {t} to answer file #{count}.")
        file.close()
        shutil.move('answer' + str(count) + '.txt', 'files/train/answer')

        if count < 5000:
            q1 = random.randint(20, 60)
            d1 = random.randint(0, 1)
            print(count)
            file = open('original' + str(count) + ".txt", 'w+')
            sss1 = ''
            for i in range(0, q1):
                r1 = random.randint(0, 25)
                ls1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                sss1 += ls1[r1]
            
            print(f"Adding testing string: {sss1} to original file #{count}.")
            file.write(''.join(format(ord(i), 'b') for i in f"""print("{sss1}")"""))
            file.close()
            shutil.move('original' + str(count) + ".txt", 'files/test/original')
            if d1 == 0:
                abl1 = ''
                file = open('compare' + str(count) + '.txt', 'w+')
                for i in sss1:
                    abl1 += f"""print("{i}")\n"""
                print(f"Adding testing string: {abl1} to compare file #{count}.")
                file.write(''.join(format(ord(i), 'b') for i in abl1))
                file.close()
                shutil.move('compare' + str(count) + ".txt", 'files/test/compare')
            else:
                abl1 = ''
                oop1 = random.randint(1, len(sss1))
                for i in range(0, oop1):
                    r1 = random.randint(0, len(sss1))
                    abl1 = sss1.replace(sss1[r1:r1+1], '', 1)
                file = open('compare' + str(count) + '.txt', 'w+')
                qbl1 = ''
                for i in abl1:
                    qbl1 += f"""print("{i}")\n"""
                print(f"Adding testing string: {qbl1} to compare file #{count}.")
                file.write(''.join(format(ord(i), 'b') for i in qbl1))
                file.close()
                shutil.move('compare' + str(count) + ".txt", 'files/test/compare')
            file = open('answer' + str(count) + '.txt', 'w+')
            if d1 == 0:
                file.write('True')
                t1 = True
            else:
                file.write('False')
                t1 = False
            print(f"Adding testing boolean: {t1} to answer file #{count}.")
            file.close()
            shutil.move('answer' + str(count) + '.txt', 'files/test/answer')
        
        if count < 2500:
            q2 = random.randint(20, 60)
            d2 = random.randint(0, 1)
            print(count)
            file = open('original' + str(count) + ".txt", 'w+')
            sss2 = ''
            for i in range(0, q2):
                r2 = random.randint(0, 25)
                ls2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                sss2 += ls2[r2]
            
            print(f"Adding testing string: {sss2} to original file #{count}.")
            file.write(''.join(format(ord(i), 'b') for i in f"""print("{sss2}")"""))
            file.close()
            shutil.move('original' + str(count) + ".txt", 'files/validate/original')
            if d2 == 0:
                abl2 = ''
                file = open('compare' + str(count) + '.txt', 'w+')
                for i in sss2:
                    abl2 += f"""print("{i}")\n"""
                print(f"Adding testing string: {abl2} to compare file #{count}.")
                file.write(''.join(format(ord(i), 'b') for i in abl2))
                file.close()
                shutil.move('compare' + str(count) + ".txt", 'files/validate/compare')
            else:
                abl2 = ''
                oop2 = random.randint(1, len(sss2))
                for i in range(0, oop2):
                    r2 = random.randint(0, len(sss2))
                    abl2 = sss2.replace(sss2[r2:r2+1], '', 1)
                file = open('compare' + str(count) + '.txt', 'w+')
                qbl2 = ''
                for i in abl2:
                    qbl2 += f"""print("{i}")\n"""
                print(f"Adding testing string: {qbl2} to compare file #{count}.")
                file.write(''.join(format(ord(i), 'b') for i in qbl2))
                file.close()
                shutil.move('compare' + str(count) + ".txt", 'files/validate/compare')
        count+=1
    

if __name__ == "__main__":
    main()