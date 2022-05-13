# -*- coding: utf-8 -*-
"""
Created on Thu May  5 23:06:16 2022

@author: aleia
"""

import time
from random import randint

#Estructuras necesarias

class State:
    def __init__(self, title = "", options = []):
         self.title = title
         self.options = options
    def set_title(self, newTitle):
        self.title = newTitle
    def set_value_in_list(self, newValue, index):
        self.options[index] = newValue

class Exercise:
    def __init__(self, tipoDeEjercicio, numReps, LimMin, LimMax, timePos):
         self.tipoDeEjercicio = tipoDeEjercicio
         self.numReps = numReps
         self.LimMin = LimMin
         self.LimMax = LimMax
         self.timePos = timePos
         self.listToShow = [" Type: " + availableExercises[tipoDeEjercicio],
                            " Repetitions: " + str(numReps),
                            " Min. Angle: " + str(LimMin),
                            " Max. Angle: " + str(LimMax),
                            " Time: " + str(timePos)]
         
class Routine:
    def __init__(self, ejercicios = [], pausaEntreEjercicios = 5):
         self.ejercicios = ejercicios
         self.pausa = pausaEntreEjercicios
    def add_exercise(self, ejercicio):
        self.ejercicios.append(ejercicio)
    def set_pause(self, pausa):
        self.pausa = pausa
    
    
  

#Funciones por ahora implementadas
def numCar(palabra):
    print(len(palabra))


def mostrarEnPantalla(fila1, fila2, fila3, fila4):
    print("\n*******Pantalla*******")
    print("***********************")
    print("1: "+ fila1)
    print("2: "+ fila2)
    print("3: "+ fila3)
    print("4: "+ fila4)
    print("***********************")

def selec(opcion):
    return "*" + opcion[1:]

def mostrarOpcionesBotonMas(estado):
    global i
    print("Botón + presionado i: "+ str(i))
    if(i< len(estado.options)-1):
        mostrarEnPantalla(estado.title, "", estado.options[i], 
                          selec(estado.options[i+1]))
        i+=1
                          
def mostrarOpcionesBotonMenos(estado):
    global i
    print("Botón - presionado i: "+ str(i))
    if(i > 0):
        mostrarEnPantalla(estado.title, "", selec(estado.options[i-1]), 
                          estado.options[i])
        i-=1
        
def mostrarOpcionInicial(estado):
    global i
    mostrarEnPantalla(estado.title, "", selec(estado.options[i]),
                              estado.options[i+1])

def moverBarraPosHorizontal(): #Se comprueba primero si ya se está en esa posición
    mostrarEnPantalla("Moviendo barra a", " posición ", "horizontal...", "") 
    time.sleep(5) #Aquí iría la activación del motor correspondiente junto a la lectura del encoder
    mostrarEnPantalla("Barra en", " posición ", "horizontal", "")
    time.sleep(3)
    
def moverBarraPosVertical(): #Se comprueba primero si ya se está en esa posición
    mostrarEnPantalla("Moviendo barra a", " posición ", "vertical...", "") 
    time.sleep(5) #Aquí iría la activación del motor correspondiente junto a la lectura del encoder
    mostrarEnPantalla("Barra en", " posición ", "vertical", "")
    time.sleep(3)
    
def leerEncoder(encoder, a):
    if a == 0:
        value = randint(-80, -10)
    elif a == 1:
        value = randint(10, 80)
    return value

def loadDefaultValues():
    global reps, minAngle, maxAngle, timeInPosition
    reps = defaultReps
    minAngle = defaultMinAngle
    maxAngle = defaultMaxAngle
    timeInPosition = defaultTimeInPosition
    CONFIG_EXERCISE.set_value_in_list(" Repetitions: "+ str(reps), 0)
    CONFIG_EXERCISE.set_value_in_list(" Time: "+ str(timeInPosition), 3)
    CONFIG_EXERCISE.set_value_in_list(" Min. Angle: "+ str(minAngle) , 1)
    CONFIG_EXERCISE.set_value_in_list(" Max. Angle: "+ str(maxAngle) , 2)

#Variables involucradas en el proceso
# i => Itera entre opciones de los estados
# currentState => estado actual
# tipo => guarda el tipo de ejercicio: 0: prono, 1: Flexo, 2: Abad.
# availableExercises => String de tipo
# rutinaCreada
# routineSelected => 0 si es default routine, 1 si es una creada

#Valores default para parámetros de ejercicios en rutina creada

defaultReps = 1
defaultMinAngle = -20
defaultMaxAngle = 20
defaultTimeInPosition = 3
defaultPauseBetweenExercises = 5

#Inicilización de parámetros con valores default en rutina creada

reps = defaultReps
minAngle = defaultMinAngle
maxAngle = defaultMaxAngle
timeInPosition = defaultTimeInPosition
pausaEntreEjercicios = defaultPauseBetweenExercises

#Valores límite para parámetros de ejercicios
maxReps = 50
maxSecs = 100
maxPause = 100

#Variables para encoders (por ahora sólo para pruebas en UI)
encoderBase = 0
encoderDisco = 1

#Creación de estados
HOME = State("--- Welcome ---")
INICIO = State(" Choose an option:", [" Create Routine", " Do default routine"])
CREATE = State(" Add exercise", [" PronoSupination", " FlexoExtension", " Ab-,Adduction", " Begin Routine"])
DO_DEFAULT = State(" Do default routine")
CONFIG_EXERCISE = State("", [" Repetitions: " + str(reps), " Min. Angle: " + str(minAngle), " Max. Angle: " + str(maxAngle), " Time: " + str(timeInPosition) , " Exercise Ready"])
REPETITIONS = State()
MIN_ANGLE = State()
MAX_ANGLE = State()
TIME = State()
EXERCISE_READY = State()
BEGIN_ROUTINE = State(" Begin routine", [" Check Routine first", " Do routine now", " Set pause betw. ex.", " Set as default rout."])
CHECK_ROUTINE = State() # noch nicht
DO_ROUTINE_NOW = State() # noch nicht
SET_PAUSE = State()
SET_AS_DEFAULT = State()

availableExercises = ["PronoSup.", "FlexoExt.", "Ab-,Adduc."]



#Instancia para la rutina por defecto
rutinaDefault = Routine()
#Ejercicios cargados en la rutina por defecto
ejercicio1Default = Exercise(0, 5, -45, 45, 5)
ejercicio2Default = Exercise(1, 5, -30, 30, 5)
ejercicio3Default = Exercise(2, 5, -20, 20, 5)
#Añadir ejercicios default a la rutina default
rutinaDefault.add_exercise(ejercicio1Default)
rutinaDefault.add_exercise(ejercicio2Default)
rutinaDefault.add_exercise(ejercicio3Default)

#Instancia para la rutina que cree el usuario
rutinaCreada = Routine([], pausaEntreEjercicios)

def main():
    
    currentState = HOME
    while(True): 
        global i, tipo, reps, timeInPosition, minAngle, maxAngle, routineSelected, pausaEntreEjercicios, rutinaCreada, rutinaDefault
        #*************************************************
        if(currentState == HOME):
            mostrarEnPantalla(HOME.title, "", "", "")
            currentState = INICIO
            i = 0
            time.sleep(3)
        
        #*************************************************
        if(currentState == INICIO):
            if(i == 0):
                mostrarOpcionInicial(currentState)            
            boton = input("Pulsa un botón: ")        
            if(boton == "+"):
                mostrarOpcionesBotonMas(currentState)
                
            if(boton == "-"):
                mostrarOpcionesBotonMenos(currentState)               
                        
            if(boton == "e"):
                if(i == 0): currentState = CREATE
                elif(i == 1): currentState = DO_DEFAULT
                else: print("Error en enter de inicio!")                
                i = 0
        #*************************************************    
        if(currentState == CREATE):
            if(i == 0):
                mostrarOpcionInicial(currentState)            
            boton = input("Pulsa un botón: ")        
            if(boton == "+"):
                mostrarOpcionesBotonMas(currentState)
                
            if(boton == "-"):
                mostrarOpcionesBotonMenos(currentState)               
  
            
            if(boton == "e"):
                if( i == 0 or i == 1 or i == 2):
                    tipo = i
                    i = 0
                    currentState = CONFIG_EXERCISE
                elif( i == 3):
                    i = 0
                    currentState = BEGIN_ROUTINE
                else: print(" Error en Create :O")
            
            if(boton == "a"):
                currentState = INICIO
                i = 0
        #*************************************************
        if(currentState == CONFIG_EXERCISE):
            if(i == 0):                
                currentState.set_title("Config. " + availableExercises[tipo]) 
                mostrarOpcionInicial(currentState)   
            boton = input("Pulsa un botón: ")     
            
            if(boton == "+"):
                mostrarOpcionesBotonMas(currentState)
                
            if(boton == "-"):
                mostrarOpcionesBotonMenos(currentState)               

            
            if(boton == "e"):
                if(i == 0): currentState = REPETITIONS
                elif(i == 1): currentState = MIN_ANGLE
                elif(i == 2): currentState = MAX_ANGLE
                elif(i == 3): currentState = TIME
                elif(i == 4): currentState = EXERCISE_READY
                else: print("Error en enter de config exercise!")                
                i = 0
            
            if(boton == "a"):
                currentState = CREATE
                i = 0
                
        #*************************************************
        if(currentState == REPETITIONS):
            if(i == 0):                
                mostrarEnPantalla("    Set number of   ", "     repetitions    ", "", str(reps))
                
            boton = input("Pulsa un botón: ")  
            
            if(boton == "+"):
                if(reps < maxReps):
                    reps += 1 
                    
            if(boton == "-"):
                if(reps > 1):
                    reps -= 1                     

            if(boton == "e"):
                currentState = CONFIG_EXERCISE    
                currentState.set_value_in_list(" Repetitions: "+ str(reps), 0)
            
            if(boton == "a"):
                reps = defaultReps
                currentState = CONFIG_EXERCISE
                currentState.set_value_in_list(" Repetitions: "+ str(reps), 0)
        #*************************************************
        if(currentState == TIME):
            if(i == 0):                
                mostrarEnPantalla("     Set time in    ", "       seconds      ", "", str(timeInPosition ))
                
            boton = input("Pulsa un botón: ")  
            
            if(boton == "+"):
                if(timeInPosition < maxSecs):
                    timeInPosition += 1 
                    
            if(boton == "-"):
                if(timeInPosition() > 1):
                    timeInPosition -= 1 
                    
            if(boton == "e"):
                currentState = CONFIG_EXERCISE   
                currentState.set_value_in_list(" Time: "+ str(timeInPosition), 3)
            
            if(boton == "a"):
                timeInPosition = defaultTimeInPosition
                currentState = CONFIG_EXERCISE
                currentState.set_value_in_list(" Time: "+ str(timeInPosition), 3)
        #*************************************************  
        if(currentState == MIN_ANGLE):
            if(i == 0):  
                if(tipo == 0 or tipo == 1):
                    moverBarraPosVertical()
                    encoder = encoderBase
                elif(tipo == 2):
                    moverBarraPosHorizontal()
                    encoder = encoderDisco
                    
                mostrarEnPantalla("Rotate bar to", "minimum Angle", "Press Enter when", "ready")
               
                
            boton = input("Pulsa un botón: ")  

            if(boton == "e"):
                minAngle = leerEncoder(encoder, 0)
                currentState = CONFIG_EXERCISE    
                currentState.set_value_in_list(" Min. Angle: "+ str(minAngle) , 1)
            
            if(boton == "a"):
                currentState = CONFIG_EXERCISE
                currentState.set_value_in_list(" Min. Angle: "+ str(minAngle) , 1)
        #*************************************************  
        if(currentState == MAX_ANGLE):
            if(i == 0):  
                if(tipo == 0 or tipo == 1):
                    moverBarraPosVertical()
                    encoder = encoderBase
                elif(tipo == 2):
                    moverBarraPosHorizontal()
                    encoder = encoderDisco
                mostrarEnPantalla("Rotate bar to", "minimum Angle", "Press Enter when", "ready")
               
                
            boton = input("Pulsa un botón: ")  

            if(boton == "e"):
                maxAngle = leerEncoder(encoder, 1)
                currentState = CONFIG_EXERCISE    
                currentState.set_value_in_list(" Max. Angle: "+ str(maxAngle) , 2)
            
            if(boton == "a"):
                currentState = CONFIG_EXERCISE 
                currentState.set_value_in_list(" Max. Angle: "+ str(maxAngle) , 2)
        #*************************************************  
        if(currentState == EXERCISE_READY):
            if(minAngle < maxAngle): 
                currentExercise = Exercise(tipo, reps, minAngle, maxAngle, timeInPosition)
                print(currentExercise.listToShow)
                rutinaCreada.add_exercise(currentExercise)
                currentState = CREATE               
                loadDefaultValues()
                mostrarEnPantalla("Exercise", "of", availableExercises[tipo], "added")
                time.sleep(3)
            else:
                mostrarEnPantalla("Max Angle must ", "be greater than ", " Min Angle", "")
                currentState = CONFIG_EXERCISE
        #*************************************************  
        if(currentState == BEGIN_ROUTINE):
            print("Creada: ", rutinaCreada.ejercicios)
            print("Default: ", rutinaDefault.ejercicios)
            if not rutinaCreada.ejercicios: #Si está vacía la lista retorna false
                mostrarEnPantalla("Routine is empty", "", "Please add exercises", "")
                time.sleep(3)
                currentState = CREATE
            else:
                if(i == 0):
                    mostrarOpcionInicial(currentState)            
                boton = input("Pulsa un botón: ")        
                if(boton == "+"):
                    mostrarOpcionesBotonMas(currentState)
                    
                if(boton == "-"):
                    mostrarOpcionesBotonMenos(currentState)               
                
                
                if(boton == "e"):
                    if(i == 0):
                        routineSelected = 1
                        currentState = CHECK_ROUTINE
                    elif( i == 1):
                        i = 0
                        currentState = DO_ROUTINE_NOW
                    elif(i == 2):
                        i = 0
                        currentState = SET_PAUSE
                    elif(i == 3):
                        i = 0
                        currentState = SET_AS_DEFAULT
                    else: print(" Error en Begin routine :O")
                
                if(boton == "a"):
                    i = 0
                    currentState = CREATE
        #*************************************************  
        if(currentState == CHECK_ROUTINE): 
            pass
        #*************************************************  
        if(currentState == DO_ROUTINE_NOW):
            pass
        #*************************************************  
        if(currentState == SET_PAUSE):
            print("Pausa antes: ", rutinaCreada.pausa)
            
            if(i == 0):                
                mostrarEnPantalla("Set pause between", "exercises in seconds", "", str(pausaEntreEjercicios))
                
            boton = input("Pulsa un botón: ")  
            
            if(boton == "+"):
                if(pausaEntreEjercicios < maxPause):
                    pausaEntreEjercicios += 1 
                    
            if(boton == "-"):
                if(pausaEntreEjercicios > 1):
                    pausaEntreEjercicios -= 1 
                    
            if(boton == "e"):
                currentState = BEGIN_ROUTINE   
                rutinaCreada.set_pause(pausaEntreEjercicios)
            
            if(boton == "a"):
                pausaEntreEjercicios = defaultPauseBetweenExercises
                currentState = BEGIN_ROUTINE
            print("Pausa después: ", rutinaCreada.pausa)
        #*************************************************  
        if(currentState == SET_AS_DEFAULT):
            rutinaDefault = rutinaCreada
            mostrarEnPantalla("Routine was set", "", "as default", "")
            time.sleep(3)
            currentState = BEGIN_ROUTINE
                                   
        #*************************************************     
        if(currentState == DO_DEFAULT):
            pass
                
       
if __name__=="__main__":
    main()

    
    
