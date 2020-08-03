
def tsk1():
    '''
    (None)-> None
    does things with the strings
    '''
    s1 = "good"
    s2 = "bad"
    s3 = "silly"
    
    s3 = s3[2:4]
    print (s3)
    s1 = s1.strip()
    print (s1)
    s = s1+s2+s3
    print(s2)
    s2 = " "+s1+s2+s3
    print(s)
    sss = s3*10
    print(sss)
    sn = len(s)
    print(str(sn))

def tsk2():
    '''
    (None)-> None
    does things with the strings
    '''
    aha = "abcdefgh"
    print(aha[0:4])
    print(aha[3:6])
    print(aha[-1])
    print(aha[-3:-1])
    print(aha[3:])
    print(aha[-3:])
    print(aha[0::3])
    print(aha[1:5:3])

def tsk3():
    '''
    (None)-> None
    does things with the strings
    '''
    s = '''It was the best of times, it was the worst of times;
it was the age of wisdom, it was the age of foolishness;
it was the epoch of belief, it was the epoch of incredulity;
it was ...'''
    
    newS = s.replace(","," ")
    newS = newS.replace("."," ")
    newS = newS.replace(";"," ")
    newS = newS.replace("\n"," ")
    print(newS)
    newS = newS.strip()
    print(newS)
    newS = newS.lower()
    print(newS)
    i = 0;
    y = 0;
    for e in s:
        if s[i:i+6] == "it was":
            print(s[i:i+6])
            y = y+1
        i = i+1
    
    print(str(y))
    newS = newS.replace("was","is")
    print(newS)
            

        
tsk1()
tsk2()
tsk3()