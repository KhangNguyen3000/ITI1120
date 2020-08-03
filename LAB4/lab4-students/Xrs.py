def is_eligible(age, citizenship, prison):
    '''
    (int, string, string)-> boolean
    returns false if any of the declarations are false
    '''
    e = True
    if age <18:
        e = False
    elif "canad" not in citizenship.lower():
        e = False
    elif "no" in prison.lower():
        e = True
    return e
          
          
name=input("What is your name? ")
age= int(input("How old are you? "))
citizenship=input("What citizenship do you have? ")
prison=input("Have you ever been in prison? ")

if is_eligible(age, citizenship, prison) == True:
     print(name, ", you are eligible to vote")
else:
     print(name, ", you are ineligible to vote") 
    



          

