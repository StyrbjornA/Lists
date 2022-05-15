myCharacter = []
nameIndex = 0
ageIndex = 1
levelIndex = 2


def create_character(char_name, char_age, char_level):
    myCharacter.clear()
    myCharacter.append(char_name)
    myCharacter.append(char_age)
    myCharacter.append(char_level)


def display_character():
    print("Name: %s" % myCharacter[nameIndex])
    print("Age: %i" % myCharacter[ageIndex])
    print("Level: %i" % myCharacter[levelIndex])


create_character("Lisa", 12, 1)
display_character()
