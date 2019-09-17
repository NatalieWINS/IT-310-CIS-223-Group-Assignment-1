# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 08:13:47 2019

@author: abloo
"""

class polygon: 
    
    def _init_(self,u_sidelength,u_sidelength2,u_sidelength3):
        self.sidelength = u_sidelength
        self.sidelength2 = u_sidelength2
        self.sidelength3 = u_sidelength3
            
    def getSideLength(self):
        return self.sidelength
    
    def setSideLength(self,u_sidelength):
        self.sidelength = u_sidelength
        
    def getSideLength2(self):
        return self.sidelength2
    
    def setSideLength2(self,u_sidelength2):
        self.sidelength2 = u_sidelength2
        
    def getSideLength3(self):
        return self.sidelength3
    
    def setSideLength3(self,u_sidelength3):
        self.sidelength3 = u_sidelength3  
        
class triangle(polygon):
      
    def calculatePerimeterT(self):
        return (self.getSideLength() + self.getSideLength2() + self.getSideLength3())
    
    def calculateAreaT(self):
        return ((self.getSideLength() * self.getSideLength2())/2)
    
class quadrilateral(polygon):
    
    def _init4_(self,u_sidelength4):
        self.sidelength4 = u_sidelength4
        
    def getSideLength4(self):
        return self.sidelength4
    
    def setSideLength4(self,u_sidelength4):
        self.sidelength4 = u_sidelength4  
    
    def calculatePerimeterQ(self):
        return (self.getSideLength() + self.getSideLength2() + self.getSideLength3() + self.getSideLength4())
    
    def calculateAreaQ(self):
        
class pentagon(polygon):
    
    def _init5_(self,u_sidelength4, u_sidelength5):
        self.sidelength4 = u_sidelength4
        self.sidelength5 = u_sidelength5
    
    def calculatePerimeterP(self):
        return (self.getSideLength() + self.getSideLength2() + self.getSideLength3() + self.getSideLength4() + getSideLength5())
    
    def calculateAreaP(self):
        
class hexagon(polygon):
    
    def _init6_(self,u_sidelength4, u_sidelength5,u_sidelength6):
        self.sidelength4 = u_sidelength4
        self.sidelength5 = u_sidelength5
        self.sidelength6 = u_sidelength6

    def calculatePerimeterH(self):
        return (self.getSideLength() + self.getSideLength2() + self.getSideLength3() + self.getSideLength4() + getSideLength5() +
                self.getSideLength6())
    def calculateAreaH(self):

class octagon(polygon):
    
    def _init_8(self,u_sidelength4, u_sidelength5,u_sidelength6,u_sidelengt7,u_sidelength8):
        self.sidelength4 = u_sidelength4
        self.sidelength5 = u_sidelength5
        self.sidelength6 = u_sidelength6
        self.sidelength7 = u_sidelength7  
        self.sidelength8 = u_sidelength8

    def calculatePerimeterO(self):
        return(self.getSideLength() + self.getSideLength2() + self.getSideLength3() + self.getSideLength4() + getSideLength5() +
                self.getSideLength6() + self.getSideLength7() + self.getSideLength8())  
    def calculateAreaO(self)

class isosceles(triangle):
    
class equilateral(triangle):
    
class rectangle(quadrilateral):
    
class square(quadrilateral):
               
    