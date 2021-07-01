import xml.etree.ElementTree as ET #imports the ElementTree module, defining the references to it as ET for easier call backs
import sys #imports the sys module
#view functions were created to help debug and show the structure of the XML
def view_recipes():
    tree = ET.parse('recipes.xml')
    recipes = tree.getroot()

    for recipe in recipes:
        print(recipe.tag, recipe.attrib)
        for ingredient in recipe.iter('ingredient'):
            print(ingredient.attrib, ingredient.text)
        for effect_group in recipe.iter('effect_group'):
            for passive_effect in effect_group.iter('passive_effect'):
                print(passive_effect.attrib, passive_effect.text)
# view_recipes()

def view_items():
    tree = ET.parse('items.xml')
    items = tree.getroot()

    for item in items:
        print()
        print(item.attrib)
        for property in item.iter('property'):
            print(property.attrib)
        for effect_group in item.iter('effect_group'):
            for passive_effect in effect_group.iter('passive_effect'):
                print(passive_effect.attrib)
            for triggered_effect in effect_group.iter('triggered_effect'):
                for requirement in triggered_effect.iter('requirement'):
                    print(triggered_effect.attrib)
                    print(requirement.attrib)
# view_items()

def view_materials():
    tree = ET.parse('materials.xml')
    materials = tree.getroot()
    for material in materials:
        print()
        print(material.attrib)
        for property in material.iter('property'):
            print(property.attrib)
# view_materials()
# end of view functions were created to help debug and show the structure of the XML
#import_items function will bring in the items.xml file
def import_items():
    tree = ET.parse('items.xml') #fetches file and parses using elementTree
    items = tree.getroot() #defines the root element of the file

    itemType = input("Search for item type (apparel, ammo, book, drink, drug, food, gun, medical, melee, mod, resource, thrown, vehicle): ") #asks user for input and give examples of common items
    itemIndex = 0 #starts assigning items an index number for easier user selection
    for item in items:
        if itemType in item.get('name'): #loop will take all item names pairing them with an index number and displaying them for the user
            print(("Item ID: {} \t Item Name: {}".format(itemIndex, item.get('name'))))
        itemIndex += 1 #adds on another digit going through the loop for the index number

    propertyIndex = 0 #starts assigning properties an index number for easier user selection
    itemId = int(input("Enter Item ID for what item would you like to get: "))
    for itemProperties in items[itemId].iter('property'): #loop will take all item properties pairing them with an index number and displaying them for the user
        print(("Item Property ID: {} \t Item Tag: {} \n\t {} ".format(propertyIndex, itemProperties.tag, list(itemProperties.items()))))
        propertyIndex += 1 #adds on another digit going through the loop for the index number

    effect_groupIndex = 0 #starts assigning effect_groups an index number for easier user selection
    itemProperties = int(input("Which property would you like to edit? "))
    for effect_group in items[itemId][itemProperties].iter('effect_group'):
        passive_effectIndex = 0
        for passive_effect in effect_group.iter('passive_effect'):
            print(("Item Property ID: {} \t Item Tag: {} \n\t {} ".format(passive_effectIndex, passive_effect.tag(), list(passive_effect.items()))))
        passive_effectIndex += 1
        triggered_effectIndex = 0
        for triggered_effect in effect_group.iter('triggered_effect'):
            print(("Item Property ID: {} \t Item Tag: {} \n\t {} ".format(triggered_effectIndex, triggered_effect.tag(), list(triggered_effect.items()))))
        triggered_effectIndex += 1
        effect_groupIndex += 1
    itemName = input("Which entry do you want to edit? ")
    itemValue = input("Change the {} entry to : ".format(itemName))
    items[itemId][itemProperties].set(itemName, itemValue)
    print("Updated Property {} with the value {}".format(itemName, items[itemId][itemProperties].get(itemName)))
    newItemXML = input("Enter in new filename: ")
    tree.write(newItemXML)
    print("{} will be created on exit".format(newItemXML))

#import_items function will bring in the materials.xml file
def import_materials():
    tree = ET.parse('materials.xml')
    materials = tree.getroot()

    materialType = input("Search for material type (melee, metal, parts, resource, wood): ")
    materialIndex = 0
    for material in materials:
        if materialType in material.get('id'):
            print(("Material ID: {} \t Material Name: {}".format(materialIndex, material.get('id'))))
        materialIndex += 1

    propertyIndex = 0
    materialId = int(input("Enter Item ID for what item would you like to get: "))
    for materialProperties in materials[materialId].iter('property'):
        print(("Material Property ID: {} \t Material Tag: {} \n\t {} ".format(propertyIndex, materialProperties.tag, list(materialProperties.items()))))
        propertyIndex += 1

    materialName = input("Which entry do you want to edit? ")
    materialValue = input("Change the {} entry to : ".format(materialName))
    materials[materialId][materialProperties].set(materialName, materialValue)
    print("Updated Property {} with the value {}".format(materialName, materials[materialId][materialProperties].get(materialName)))
    newMaterialXML = input("Enter in new filename: ")
    tree.write(newMaterialXML)
    print("{} will be created on exit".format(newMaterialXML))

#import_items function will bring in the recipes.xml file
def import_recipes():
    tree = ET.parse('recipes.xml')
    recipes = tree.getroot()

    recipeType = input("Search for item type (ammo, apparel, armor, book, drink, drug, food, gun, medical, melee, mod, resource, thrown, tool, vehicle): ")
    recipeIndex = 0
    for recipe in recipes:
        if recipeType in recipe.get('name'):
            print(("Item ID: {} \t Item Name: {}".format(recipeIndex, recipe.get('name'))))
        recipeIndex += 1

    propertyIndex = 0
    recipeId = int(input("Enter Item ID for what item would you like to get: "))
    for recipeProperties in recipes[recipeId].iter('ingredient'):
        print(("Recipe Property ID: {} \t Recipe Tag: {} \n\t {} ".format(propertyIndex, recipeProperties.tag, list(recipeProperties.items()))))
        propertyIndex += 1

    effect_groupIndex = 0
    recipeProperties = int(input("Which property would you like to edit? "))
    for effect_group in recipes[recipeId][recipeProperties].iter('effect_group'):
        passive_effectIndex = 0
        for passive_effect in effect_group.iter('passive_effect'):
            print(("Recipe Property ID: {} \t Recipe Tag: {} \n\t {} ".format(passive_effectIndex, passive_effect.tag(), list(passive_effect.items()))))
        passive_effectIndex += 1
        triggered_effectIndex = 0
        for triggered_effect in effect_group.iter('triggered_effect'):
            for requirement in triggered_effect.iter('requirement'):
                print(("Recipe Property ID: {} \t Recipe Tag: {} \n\t {} ".format(triggered_effectIndex, triggered_effect.tag(), list(triggered_effect.items(), list(requirement.items())))))
        triggered_effectIndex += 1
        effect_groupIndex += 1
    recipeName = input("Which entry do you want to edit? ")
    recipeValue = input("Change the {} entry to : ".format(recipeName))
    recipes[recipeId][recipeProperties].set(recipeName, recipeValue)
    print("Updated Property {} with the value {}".format(recipeName, recipes[recipeId][recipeProperties].get(recipeName)))
    newRecipeXML = input("Enter in new filename: ")
    tree.write(newRecipeXML)
    print("{} will be created on exit".format(newRecipeXML))
#main function to run the program
if __name__ == "__main__":
    while (True):
        #read user input
        workingFile = int(input("Enter 1 for Items or 2 for Materials or 3 for Recipes. 0 will exit the program: "))

        if workingFile == 1:
            print("Now parsing Items.XML....")
            import_items()
        elif workingFile == 2:
            print("Now parsing Materials.XML....")
            import_materials()
        elif workingFile == 3:
            print("Now parsing Recipes.XML....")
            import_recipes()
        elif workingFile == 0:
            sys.exit("Exiting program")
        else:
            print("Please enter 1, 2 or 3!")
