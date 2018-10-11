'''
Created on Oct 10, 2018

Tarea 2 - Ingeniería de Software I

Universidad Simón Bolívar

Autores: Javier Vivas - 12-11067
         Giacomo Tosone - 14-11085
         
'''
import unittest
from Tarea import *

class Test(unittest.TestCase):


    def setUp(self):
        self.t = Trabajador("Name","M","1/1/1940",800,0)


    def tearDown(self):
        pass


    def testTarea1(self):
        self.assertEqual("Merece pension 1", self.t.pension(self.t.sexo,self.t.fechaNac,self.t.cantiSem,self.t.actIns), "Error")
    
    def testTarea2(self):
        self.t =  Trabajador("Name","F","1/1/1960",400,0)
        self.assertEqual("No merece pension", self.t.pension(self.t.sexo,self.t.fechaNac,self.t.cantiSem,self.t.actIns), "Error")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
