# I spent way too long doing this before I actually decided to just use the api
'''types = [("normal", ["rock", "steel"], [], ["ghost"]), 
         ("fire", ["fire", "water", "rock", "dragon"], ["grass", "ice", "bug", "steel"], []),
         ("water", ["water", "grass", "dragon"], ["fire, ground, rock"], []),
         ("electric", ["electric", "grass"], ["water", "flying"], ["ground"]),
         ("grass", ["fire", "grass", "poison", "flying", "bug"], ["water", "ground", "rock"], []),
         ("ice", ["fire", "water", "ice", "steel"], ["grass", "ground", "flying", "dragon"]),
         ("fighting", ["poison", "flying", "psychic", "bug", "fairy"], ["normal", "ice", "rock", "dark", "steel"], ["ghost"]),
         ("poison", ["poison", "ground", "rock", "ghost"], ["grass", "fairy"], ["steel"]),
         ("ground", ["grass", "bug"], ["fire", "electric", "poison", "rock", "steel"], ["flying"]),
         ()]'''

import requests
import json

#Handle a get request and return an error if there is an exception
def get(url):
    try:
        req = requests.get(url)

    except requests.exceptions.RequestException:
        return False

    return req.json()

def getMultiplier(pokeType, enemyType, typeData):
    #Loop through every type
    for i in range(len(typeData)):
        #If the type in the database matches the typed type
        if pokeType == typeData[i]["name"]:
            
            #Get type damage information and check if it's 
            typeDamage = get(typeData[i]["url"])
            if typeDamage is False:
                return False

            typeDamage = typeDamage["damage_relations"]
            foundType = False

            #Loop through every item and check if the name matches the enemy name
            for i in typeDamage["half_damage_to"]:
                if enemyType in i["name"]:
                    return .5
                    foundType = True

            for i in typeDamage["double_damage_to"]:
                if enemyType in i["name"]:
                    return 2
                    foundType = True

            for i in typeDamage["no_damage_to"]:
                if enemyType in i["name"]:
                    return 0
                    foundType = True
            
            if not foundType:
                return 1
    
def getTypeData():    
    #Base url for the API
    baseUrl = "https://pokeapi.co/api/v2/type/"

    #Gets all the different types in json
    typeData = get(baseUrl)
    
    #If there was a connection error
    if typeData is False:
        return False
    
    return typeData["results"];



#Try connecting to pokeapi
print("Accessing type data...")
typeData = getTypeData()

#While typeData is invalid offer to retry to connect to pokeapi.
while typeData is False:
    print("Error connecting to pokeapi. Check your connection")
    input("Press any key to try again.")
    print("")
    typeData = getTypeData()
print("Done.")

#Store all the pokemon names in a separate variable
typeNames = []
for t in typeData:
    typeNames.append(t["name"])

print("Welcome to Tomas' amazing pokeprogram thing v1.0\n")

#Main loop
while True:
    #Gets input
    pokeType = input("Enter pokemon type being used: ").lower()
    #If the pokemon name isn't valid re run the loop
    if pokeType not in typeNames:
        print("Invalid type\n")
        continue
    
    enemyType = input("Enter pokemon type of enemy: ").lower()
    if enemyType not in typeNames:
        print("Invalid type\n")
        continue
    
    multiplier = getMultiplier(pokeType, enemyType, typeData)
    
    if multiplier is False:
        print("\nError connecting to pokeapi. Check internet connection.")
        input("Press any key to try again.")
        print("")
        continue
    
    print("Pokemon deals: x" + str(multiplier) + " damage\n")
    
    
