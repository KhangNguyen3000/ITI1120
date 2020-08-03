class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'


class Rectangle:
    'represents a 2D (axis-parallel) rectangle'

    def __init__(self, bottomLeft = Point(), topRight = Point(), color = "red"):
        '''
        (Rectangle,Point,Point,String)->None
        Initialize bottomleft, and top right coordinates and color'''
        self.bL = bottomLeft
        self.tR = topRight
        self.c = color
        self.p = 2*((self.tR.get()[0] - self.bL.get()[0]) + (self.tR.get()[1] - self.bL.get()[1]))
        self.a = (self.tR.get()[0] - self.bL.get()[0]) * (self.tR.get()[1] - self.bL.get()[1])

    def __eq__(self, other):
        '''(Rectangle,Rectangle)->bool
        Returns True if self and other have the same coordinates for bottom left and top right and have the same colors'''
        return (self.bL.get() == other.bL.get()) and (self.tR.get() == other.tR.get() and self.c == other.c)

    def __repr__(self):
        '''(rectangle)->str
        Returns canonical string representation Rectangle(bottom left, top right, color)'''
        return "Rectangle("+str(self.bL)+","+str(self.tR)+", '"+str(self.c)+"')"

    def __str__(self):
        '''(rectangle)->str
        Returns canonical string representation
        I am a color rectangle with bottom left corner at () and top right corner at ().'''
        return "I am a "+str(self.c)+" rectangle with a bottom left corner at "+str(self.bL.get())+" and a top right corner at "+str(self.tR.get())+"."
        
    def get_color(self):
        '''(Rectangle)->String
        Returns color of the rectangle'''
        return(self.c)

    def get_bottom_left(self):
        '''(Rectangle)->Point
        Returns coordinates of bottom left corner'''
        return(self.bL)

    def get_top_right(self):
        '''(Rectangle)->Point
        Returns coordinates of top right corner'''
        return(self.tR)

    def get_perimeter(self):
        '''(Rectangle)->Integer
        Returns perimeter of rectangle'''
        return(self.p)

    def get_area(self):
        '''(Rectangle)->Integer
        Returns area of rectangle'''
        return(self.a)

    def reset_color(self, color = "no color"):
        '''(Rectangle)->None
        Changes the color of the rectangle'''
        self.c = color

    def move(self, x = 0, y = 0):
        '''(rectangle)->None
        Moves the rectangle with variant of x and y'''
        self.bL.move(x,y)
        self.tR.move(x,y)

    def contains(self, x = 0, y = 0):
        '''(Rectangle, Integer, Integer)->boolean
        Return true if the coordinate giving is in or on the rectangle otherwise return false'''
        return(self.bL.get()[0]<= x <= self.tR.get()[0]) and (self.bL.get()[1]<= x <= self.tR.get()[1])

    def intersects(self,other):
        '''(Rectangle,Rectangle)->bool
        Returns True if self and other have atleast a point in common'''
        return not (self.bL.get() > other.tR.get() or self.tR.get() < other.bL.get())


class Canvas:
    'represents a collections of Rectangles'

    def __init__(self):
        '''(Canvas)->None
        Creates a canvas'''
        self.rL = []
        
    def __len__(self):
        '''(Canvas)->Integer
        Returns the number of rectangles in the canvas'''
        return len(self.rL)

    def __repr__(self):
        '''(rectangle)->str
        Returns canonical string representation Canvas(List of rectangles)'''
        return "Canvas("+str(self.rL)+"')"

    def add_one_rectangle(self, rect = Rectangle()):
        '''(Canvas, Rectangle)->None
        Adds a rectangle to the list'''
        self.rL.append(rect)

    def count_same_color(self, s = ""):
        '''(Canvas, String)->Integer
        Returns number of rectangles with the color asked'''
        c = 0
        for i in self.rL:
            if i.c == s:
                c = c+1
        return c

    def total_perimeter(self):
        '''(Canvas)->Integer
        Returns the total perimeter'''
        c = 0
        for i in self.rL:
            c = c+i.p
        return c

    def min_enclosing_rectangle(self):
        '''(Canvas)->Rectangle
        Returns the smallest rectangle to hold all rectangles'''
        mx = self.rL[0].bL.get()[0]
        x = self.rL[0].tR.get()[0]
        my = self.rL[0].bL.get()[1]
        y = self.rL[0].tR.get()[1]
        for i in self.rL:
            if i.bL.get()[0] < mx:
                mx = i.bL.get()[0]
            if i.tR.get()[0] > x:
                x = i.tR.get()[0]
            if i.bL.get()[1] < my:
                my = i.bL.get()[1]
            if i.tR.get()[1] > y:
                y = i.tR.get()[1]
        return (Rectangle(Point(mx,my),Point(x,y),'red'))

    def common_point(self):
        '''(Canvas)->boolean
        Returns True if all the rectangles have a point in common and false if they do not'''
        for i in range(len(self.rL)):
            for x in range(i,len(self.rL)):
                if (self.rL[i].intersects(self.rL[x]) == False):
                    return False
        return True
