'''


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
        #prueba realizada el 11/10/2018, dio correcta en esta fecha 
        self.t =  Trabajador("Name","m","12/10/1958",1000,0)       
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
    def testEdadMinHorasMin2(self):
        #prueba realizada el 10/10/2018, dio correcta en esta fecha
        self.t =  Trabajador("Name","M","10/10/1963",750,20)
        self.assertEqual("Merece pension", self.t.pension(self.t.sexo,self.t.fechaNac,self.t.cantiSem,self.t.actIns), "Error")
    def testCasiEdadMinHorasMin(self):
        #prueba realizada el 10/10/2018, dio correcta en esta fecha
        self.t =  Trabajador("Name","f","10/11/1966",750,12)
        self.assertEqual("No merece pension", self.t.pension(self.t.sexo,self.t.fechaNac,self.t.cantiSem,self.t.actIns), "Error")
    def testEdadMinCasiHorasMin(self):
        #prueba realizada el 10/10/2018, dio correcta en esta fecha
        self.t =  Trabajador("Name","f","10/10/1966",749,12)
        self.assertEqual("No merece pension", self.t.pension(self.t.sexo,self.t.fechaNac,self.t.cantiSem,self.t.actIns), "Error")
    def testCasiEdadMinCasiHorasMin(self):
        #prueba realizada el 10/10/2018, dio correcta en esta fecha
        self.t =  Trabajador("Name","f","27/12/1969",749,20)
        self.assertEqual("No merece pension", self.t.pension(self.t.sexo,self.t.fechaNac,self.t.cantiSem,self.t.actIns), "Error")    
    def testSobreMaxEdad(self):
        #prueba realizada el 10/10/2018, dio correcta en esta fecha
        self.t =  Trabajador("Name","f","11/10/1895",2000,0)
        self.assertEqual("Edad invalida", self.t.pension(self.t.sexo,self.t.fechaNac,self.t.cantiSem,self.t.actIns), "Error")     
    def testMaxEdad(self):
        #prueba realizada el 10/10/2018, dio correcta en esta fecha
        self.t =  Trabajador("Name","f","11/10/1896",2000,0)
        self.assertEqual("Merece pension", self.t.pension(self.t.sexo,self.t.fechaNac,self.t.cantiSem,self.t.actIns), "Error")
    def testMaxEdadMinHora(self):
        #prueba realizada el 10/10/2018, dio correcta en esta fecha
        self.t =  Trabajador("Name","f","11/10/1896",750,0)
        self.assertEqual("Merece pension", self.t.pension(self.t.sexo,self.t.fechaNac,self.t.cantiSem,self.t.actIns), "Error")
    def testMaxEdadCasiHoraMin(self):
        #prueba realizada el 10/10/2018, dio correcta en esta fecha
        self.t =  Trabajador("Name","f","11/10/1896",749,0)
        self.assertEqual("No merece pension", self.t.pension(self.t.sexo,self.t.fechaNac,self.t.cantiSem,self.t.actIns), "Error")
    def testPruebaMaliciaH(self):
        #prueba realizada el 10/10/2018, dio correcta en esta fecha
        self.t =  Trabajador("Name","f","11/10/1896",-20,30)
        self.assertEqual("Error de negativo", self.t.pension(self.t.sexo,self.t.fechaNac,self.t.cantiSem,self.t.actIns), "Error")
    def testPruebaMaliciaHi(self):
        #prueba realizada el 10/10/2018, dio correcta en esta fecha
        self.t =  Trabajador("Name","f","11/10/1896",749,-15)
        self.assertEqual("Error de negativo", self.t.pension(self.t.sexo,self.t.fechaNac,self.t.cantiSem,self.t.actIns), "Error")
    def testPruebaMaliciaFecha(self):
        
        self.t =  Trabajador("Name","f","11/10/3450",1500,10)
        self.assertEqual("No ha nacido", self.t.pension(self.t.sexo,self.t.fechaNac,self.t.cantiSem,self.t.actIns), "Error")
    def testPruebaMaliciaSexo(self):
        
        self.t =  Trabajador("Name","W","11/10/1930",1500,10)
        self.assertEqual("Sexo invalido", self.t.pension(self.t.sexo,self.t.fechaNac,self.t.cantiSem,self.t.actIns), "Error")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()