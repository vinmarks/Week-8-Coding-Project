#############################################
## Script Name: Week 8 - Coding Project.py
## Title: Week Eight Coding Assignment
## Author: Vincent Marks
## Date: 12MAR23
#############################################

##Imports
from os import system, name
from time import sleep as sl
import json


## Globals
carInventory = []
newListForLoad = []

#Class
class Car:
    def __init__(self, make, model, vin, mileage, price, features):
        self.make = make
        self.model = model
        self.vin = vin
        self.mileage = mileage
        self.price = price
        self.features = features
    def printCar(self):
        return " Make: {} \n Model: {} \n VIN: {} \n Mileage: {} \n Price: {} \n Features:{} \n".format(self.make, self.model, self.vin, self.mileage, self.price, self.features) 
class ANSI:
    def background(code):
        return "\33[{code}m".format(code=code)
 
    def styleText(code):
        return "\33[{code}m".format(code=code)
 
    def colorText(code):
        return "\33[{code}m".format(code=code)
    
# Color Alterations
# Old School Blue and White Output
menuColor = ANSI.background(44) + ANSI.styleText(1) + ANSI.colorText(37)   
# Functions
def clearScreen():
        if name == 'nt':
            system('cls')
        else:
            system('clear')
def printMenu():
    clearScreen()
    print("Welcome to Stock-O-Matic '96")
    print('===========================\n')
    print(menuColor + '1. Add a Vehicle to Inventory')
    print(menuColor + '2. Edit a Listed Vehicle')
    print(menuColor + '3. Delete a Vehicle from Inventory')
    print(menuColor + '4. Display Vehicles') 
    print(menuColor + '5. Save Data')
    print(menuColor + '6. Load Data')
def addCar():
    clearScreen()
    print('Add a New Vehical to Inventory ')
    input('Press Enter to Continue: ')
    clearScreen()
    make = input('Make of Vehicle: ')
    model = input('Model of Vehicle: ')
    ### Excpetion Handling for non-integer inputs for VIN, Mileage, and Price
    try:
        vin = int(input('VIN of Vehicle: '))
    except ValueError:
        vin = int(input('\nNot a Number. \n\nPlease enter a numerical value for VIN: '))
    try:
        mileage = int(input('Mileage of Vehicle: '))
    except ValueError:
        mileage = int(input('\nnot a Number. \n\nPlease enter a numerical value for Mileage of Vehicle: '))
    try:    
        price = float(input('Price of Vehicle: '))
    except ValueError:
        price = float(input('\nNot a Number. \n\nPlease enter a numerical value for Price of Vehicle: '))
    entry = input('3 notable features of Vehicle: \n')
    features = []
    while len(features) != 3:
        features.append(entry)
        entry = input()
    global carInventory
    car = Car(make, model, vin, mileage, price, features)
    carInventory.append(car)
def deleteCar():
    clearScreen()
    global carInventory
    found = False
    index = None
    carIdent = int(input('Enter VIN: '))
    for car in carInventory:
        if (carIdent == car.vin):
            print('An Entry Exists for this VIN')
            sl(2)
            found = True
            index = carInventory.index(car)
        if found:
            clearScreen()
            input('Press Enter to Delete: ')
            del(carInventory[index])
            clearScreen()
            input('Requested Vehicle Has Been Removed from Inverntory \n Press Enter: ')
        else:
            input('No Entry Exists for Entered VIN \n\n Press Enter: ')
def editCar():
    clearScreen()
    global carInventory
    found = False
    index = None
    carIdent = int(input('Enter VIN: '))
    for car in carInventory:
        if (carIdent == car.vin):
            found = True
            index = carInventory.index(car)
        if found:
            print('Car was found!')
            print('You are permitted to change Make, Model, and Price Without Creating a New Entry')
            input('Press Enter to Edit: ')
            clearScreen()
            carInventory[index]
            updateMake = input('Update Make: ')
            car.make = updateMake 
            updateModel = input('Update Model: ')
            car.model = updateModel
            updatePrice = input('Update Price: ')
            car.price = updatePrice
            input('Vehicle Entry Has Been Updated \n Returning to Main Menu')
        else:
            print('Vehicle was not found. Returning to Main Menu.')
    sl(3)           
def printCar():
    clearScreen()
    print('Inventory: ')
    print('=====================')
    for car in carInventory:
        print(Car.printCar(car))
    if len(carInventory) == 0:
        print('The Inventory is Currently Empty \nNothing to Display')
    input('Press enter to continue: ')
def obj_dict(obj):
    return obj.__dict__
def saveData():
    clearScreen()
    saveFile = input('Enter Name of File to Save To: ')
    print('Saving data to', saveFile, 'via json.dumps()')
    sl(3)
    with open(saveFile, 'w') as fo:
        fo.write(json.dumps(carInventory, default=obj_dict))
    print('Save Succesful!')
    print('Data Saved to', saveFile)
    input('Press Enter to Return to Main Menu: ')
def loadData():
    clearScreen()
    #FileDoesNotExist Excpetion
    ## the desired file is dataflie.json. Enter any other name to loop through exception
    try:
        loadFile = input('Please Enter File Name: ')
        with open(loadFile, 'r') as fi:
            data = json.load(fi)
            for car in data:
                carObj = Car(car['make'], car['model'], car['vin'], car['mileage'], car['price'], car['features'])
                newListForLoad.append(carObj)
        for car in newListForLoad:
            carInventory.append(car)
            print('Saved Vehicle Data Entries to be Loaded: ')
            print('=====================')
            for y in car.__dict__:
                if type(car.__dict__[y]) is dict:
                    for z in car.__dict__[y].keys():
                        print(z, car.__dict__[y][z])
                else:
                    print(y, car.__dict__[y])
    except FileNotFoundError:
        print('File not Found')
        fileName = input('Enter File Name:')
        with open(fileName, 'r') as fi:
            data = json.load(fi)
            for car in data:
                carObj = Car(car['make'], car['model'], car['vin'], car['mileage'], car['price'], car['features'])
                newListForLoad.append(carObj)
        for car in newListForLoad:
            carInventory.append(car)
            print('Saved Vehicle Data Entries to be Loaded: ')
            print('=====================')
            for y in car.__dict__:
                if type(car.__dict__[y]) is dict:
                    for z in car.__dict__[y].keys():
                        print(z, car.__dict__[y][z])
                else:
                    print(y, car.__dict__[y])
    ## FileIsEmpty Exception
    except json.decoder.JSONDecodeError:
        print('The Selected File is Empty')
        input('Press Enter to Return to Main Menu: ')
        printMenu()
    finally:
        print('===================')
        input('Press Enter: ')
        clearScreen()
        print('Saved Vehicle Data was Loaded Into Car Inventory')        
        input('Press Enter to Continue: ')
def main():
    clearScreen()
    printMenu()
    prompt = '\nWhat would you like to do? '
    entry = 0 
    while prompt != '8':
        printMenu()
        selection = input(prompt)
        if selection == '1':
            addCar()
        elif selection == '2':
            editCar()
        elif selection == '3':
            deleteCar()
        elif selection == '4':
            printCar()
        elif selection == '5':
            saveData()
        elif selection == '6':
            loadData()    
        else:
            print('goodbye')



main()