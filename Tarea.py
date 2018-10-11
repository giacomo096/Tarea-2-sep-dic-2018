'''

Created on Oct 10, 2018

Tarea 2 - Ingenieria de Software I

Universidad Simon Bolivar

Autores: Javier Vivas - 12-11067
         Giacomo Tosone - 14-11085

'''
import datetime

class Trabajador():
    '''
    classdocs
    '''

    '''
    @param nombre: Indica el nombre de la persona
    @param sexo: Indica el sexo de la persona
    @param fechaNac: Indica la fecha de nacimiento de la persona
    @param cantiSem: Indica la cantidad de semanas trabajadas cotizadas
    @param actIns: Indica la cantidad de años trabajando en ambientes insalubres
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
            return("No ha nacido")
        if (now.year - int(anoNac)) > 122:
            return("Edad invalida")
    
        if cantiSem < 0:
            return("Error de negativo")
    
        if actIns < 0:
            return("Error de negativo")
    
        #Fin de casos borde
    
        edadActual = now.year - int(anoNac)
    
        if int(mesNac) > now.month:
            edadActual = edadActual - 1
    
        if int(mesNac) == now.month:
            if int(diaNac) > now.day:
                edadActual = edadActual - 1
    
        #Calculo para determinar si merece pension en caso de ser masculino el sexo
    
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
    
        #Calculo para determinar si merece pension en caso de ser femenino el sexo
    
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
    
