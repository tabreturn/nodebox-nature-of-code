from math import sqrt
from math import atan2
from math import acos

class PVector:
    def __init__(self, x_=0, y_=0):
        self.x = x_
        self.y = y_
        
    def add(self, v):
        self.x = self.x + v.x
        self.y = self.y + v.y
    
    @staticmethod
    def addStatic(v1, v2):
        v3 = PVector(v1.x+v2.x, v1.y+v2.y)
        return v3
    
    def sub(self, v):
        self.x = self.x - v.x
        self.y = self.y - v.y
    
    @staticmethod
    def subStatic(v1, v2):
        v3 = PVector(v1.x-v2.x, v1.y-v2.y)
        return v3;
    
    def mult(self, n):
        self.x = self.x * n
        self.y = self.y * n
        
    def div(self, n):
        self.x = self.x / n
        self.y = self.y / n
    
    def mag(self):
        return sqrt(self.x*self.x + self.y*self.y)
        
    def normalize(self):
        m = self.mag()
        if(m != 0):
            self.div(m)
    
    def limit(self, max):
        if(self.mag() > max):
            self.normalize()
            self.mult(max)
    
    def random2D(self):
        self.x = random(-1., 1.)
        self.y = random(-1., 1.)
        self.normalize()
    
    def get(self):
        return PVector(self.x, self.y)
    
    def heading(self):
        angle = atan2(-self.y, self.x)
        angle *= -1
        return angle
    
    def dot(self, v):
        return self.x*v.x + self.y*v.y
        #return self.x*v.x + self.y*v.y + self.z*v.z
    
    @staticmethod    
    def angleBetween(v1, v2):
        dot = v1.dot(v2)
        theta = acos(dot / (v1.mag() * v2.mag()))
        return theta
    
    @staticmethod
    def dist(v1, v2):
        dx = v1.x - v2.x
        dy = v1.y - v2.y
        return sqrt(dx*dx + dy*dy)
        

