#python classes are a way of defining entirely new type in python

class Point:
    #this function is called whenever I create a new Point object
    #self is the name referring to the new point object I just created
    def __init__(self,x,y):
        self.x = x
        self.y = y

p = Point(1,2)
print(p.x)
print(p.y)