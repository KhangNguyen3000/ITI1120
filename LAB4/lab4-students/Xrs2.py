from builtins import str
def mess(string):
    '''
    (String)-> String
    takes a phrase (i.e., a string) as input and then
returns the copy of that phrase where each character that is one of the last 8
consonants of English alphabet is capitalized (so, r, s, t, v, w, x,y , z) and where
each blank space is replaced by dash.
    '''
    
    for e in "rstvwxyz":
        str = ""
        for i in string:
            if e == i:
                str = str+(e.upper())
            else:
                str = str+i
        string = str

    str = ""
    
    for i in string:
        if i == " ":
            str = str+("-")
        else:
            str = str+i
    string = str
    
    print(string)