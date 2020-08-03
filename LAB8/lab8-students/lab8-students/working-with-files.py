def create_table(file_name):
    '''(str)->list of lists where each "inner" list has 3 elements
    Returns the list as described above
    '''

    # this opens, reads the file and places each line as a string into list called alc
    f=open(file_name).read().splitlines()


    # make empty table 
    t=[]

    print()
    # this for loop populates the table with lists containing info about each metal in the file
    for b in f:
        b=b.split("\t")
        title = b[0]
        author = b[1]
        printn = b[2]
        fict = b[4]
        a = b[3].split("/")
        print(a)
        date = a[2] +"-"+ a[0] +"-"+ a[1]

        # add the list cointaing info about current metal to the table
        t.append( [ date, title, author, printn, fict ]  )       
 
    return t

def nice_print(table):
    for metal in table:
        for info in metal:
            print(info, end='  ')
        print()

def search_by_year(books,year1,year2):
    t = []

    for i in books:
        a = i[0].split("-")
        if int(a[0]) >= year1 and int(a[0]) <= year2:
            print(i[1]+", by "+i[2]+" ("+i[0]+")")
            t.append(i)
    if len(t) == 0:
        print("No books found in that range of years.")
        
        
# main
file_name=input("Enter the name of the file: ")
file_name=file_name.strip()
books=create_table(file_name)
print("\nHere is what the final 2Dlist/table looks like:\n")
print(books)

print("\nHere is what it looks like in humany printable form:\n")
nice_print(books)


