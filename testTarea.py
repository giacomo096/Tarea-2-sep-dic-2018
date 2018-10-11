'''
Created on Oct 10, 2018

@author: giacomo
'''
import unittest
from Tarea import *

class Test(unittest.TestCase):


    def setUp(self):
        self.t = Trabajador("Name","M","1/1/1940",800,0)


    def tearDown(self):
        pass


    def testTarea1(self):
        self.assertEqual("Merece pension", self.t.pension(self.t.sexo,self.t.fechaNac,self.t.cantiSem,self.t.actIns), "Error")
    
    def testTarea2(self):
        self.t =  Trabajador("Name","F","1/1/1960",400,0)
        self.assertEqual("No merece pension", self.t.pension(self.t.sexo,self.t.fechaNac,self.t.cantiSem,self.t.actIns), "Error")
    
    def testTarea3(self):
        self.t =  Trabajador("Name","m","1/1/1960",750,0)
        self.assertEqual("No merece pension", self.t.pension(self.t.sexo,self.t.fechaNac,self.t.cantiSem,self.t.actIns), "Error")
    def testEdadMin(self):
        self.t =  Trabajador("Name","m","10/10/1958",1000,0)
        self.assertEqual("Merece pension", self.t.pension(self.t.sexo,self.t.fechaNac,self.t.cantiSem,self.t.actIns), "Error")  
    def testCasiEdadMin(self):
        #prueba realizada el 10/10/2018, dio correcta en esta fecha 
        self.t =  Trabajador("Name","m","11/10/1958",1000,0)       
        self.assertEqual("No merece pension", self.t.pension(self.t.sexo,self.t.fechaNac,self.t.cantiSem,self.t.actIns), "Error") 
    def testHorasMin(self):
        self.t =  Trabajador("Name","f","10/10/1938",750,0)
        self.assertEqual("Merece pension", self.t.pension(self.t.sexo,self.t.fechaNac,self.t.cantiSem,self.t.actIns), "Error")
    def testEdadMin2(self):
        #prueba realizada el 10/10/2018, dio correcta en esta fecha
        self.t =  Trabajador("Name","f","10/10/1962",900,4)
        self.assertEqual("Merece pension", self.t.pension(self.t.sexo,self.t.fechaNac,self.t.cantiSem,self.t.actIns), "Error")
    def testEdadMinHorasMin(self):
        #prueba realizada el 10/10/2018, dio correcta en esta fecha
        self.t =  Trabajador("Name","f","10/10/1961",750,8)
        self.assertEqual("Merece pension", self.t.pension(self.t.sexo,self.t.fechaNac,self.t.cantiSem,self.t.actIns), "Error")
        
        
         
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()