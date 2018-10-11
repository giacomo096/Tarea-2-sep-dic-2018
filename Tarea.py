'''
Created on Oct 10, 2018


'''
import datetime

class Trabajador():
    '''
    classdocs
    '''


    def __init__(self, nombre, sexo, fechaNac, cantiSem, actIns ):
        self.nombre = nombre
        self.sexo = sexo
        self.fechaNac = fechaNac
        self.cantiSem = cantiSem
        self.actIns = actIns  
     
     
    def pension(self, sexo, fechaNac, cantiSem, actIns):  

        now = datetime.datetime.now()
    
        fecha = fechaNac.split("/")
        diaNac = fecha[0]
        mesNac = fecha[1]
        anoNac = fecha[2]
    
        #Inicio de casos borde
        if int(anoNac) > now.year:
            return("Ano invalido")
        if (now.year - int(anoNac)) > 122:
            return("Edad invalida")
    
        if cantiSem < 0:
            return("La cantidad de semanas trabajadas no puede ser negativa")
    
        if actIns < 0:
            return("La cantidad de anos trabajando en actividades insalubres no puede ser negativa")
    
        #Fin de los casos borde
    
        edadActual = now.year - int(anoNac)
    
        if int(mesNac) > now.month:
            edadActual = edadActual - 1
    
        if int(mesNac) == now.month:
            if int(diaNac) > now.day:
                edadActual = edadActual - 1
    
        if (sexo == "M") | (sexo == "m"):
            if actIns == 0:
                if edadActual >= 60:
                    if cantiSem >= 750:
                        return("Merece pension")
        
            if actIns > 0:
                if cantiSem >= 750:
                    if (actIns % 4) == 0:
                        if actIns <= 20:
                            edadAcep = 60 - (actIns / 4)
    
                            if edadActual >= edadAcep:
                                return("Merece pension")
    
                        if actIns > 20:
                            edadAcep = 60 - 5
    
                            if edadActual >= edadAcep:
                                return("Merece pension")
    
                    if (actIns % 4) != 0:
                        if actIns < 20:
                            actIns = (actIns - (actIns % 4)) / 4
                            edadAcep = 60 - actIns
    
                            if edadActual >= edadAcep:
                                return("Merece pension")
    
                        if actIns > 20:
                            edadAcep = 60 - 5
    
                            if edadActual >= edadAcep:
                                return("Merece pension")
    
            return("No merece pension")
    
        if (sexo == "F") | (sexo == "f"):
            if actIns == 0:
                if edadActual >= 55:
                    if cantiSem >= 750:
                        return("Merece pension")
        
            if actIns > 0:
                if cantiSem >= 750:
                    if (actIns % 4) == 0:
                        if actIns <= 20:
                            edadAcep = 55 - (actIns / 4)
    
                            if edadActual >= edadAcep:
                                return("Merece pension")
    
                        if actIns > 20:
                            edadAcep = 55 - 5
    
                            if edadActual >= edadAcep:
                                return("Merece pension")
    
                    if (actIns % 4) != 0:
                        if actIns < 20:
                            actIns = (actIns - (actIns % 4)) / 4
                            edadAcep = 55 - actIns
    
                            if edadActual >= edadAcep:
                                return("Merece pension")
    
                        if actIns > 20:
                            edadAcep = 55 - 5
    
                            if edadActual >= edadAcep:
                                return("Merece pension")
    
            return("No merece pension")
    
        else:
            return("Sexo invalido")
    
    #pension("m","4/11/1950",750,0)                    
    