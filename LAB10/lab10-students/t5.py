class Point:
#    constructor
#    notice two underscores
    def __init__(self, xcoord=0, ycoord=0):
        '''initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord
        
def get(self):
    '''(Point)->tuple
    return a tuple with x and y coordinates of the point'''
    return (self.x, self.y)

def move(self, dx, dy):
    '''(Point,float,float)->None
    change the x and y coordinates by dx and dy'''
    self.x += dx
    self.y += dy

    def __eq__(self, other):
        'self == other if they have the same coordinates'
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        'return canonical string representation Point(x, y)'
        return 'Point('+str(self.x)+','+str(self.y)+')'

# main

p1=Point(10,-1)
p2=Point(1,2)
s1="today"
a=[1,2]

# TASK 5
# how does python 'translate' each one of these calls?

#for example this one is translated as
get(p1)
# Point.get(p1)

get(p2)

move(p1,1,1)

p1==p2

p2==p1

result = ''
for char in s1:
    if ord(char) >= 65:
        result += chr(ord(char) - 32)
s1 = result

a = a + [3]
