def GenerateBandName():
    print("Welcome to the Band Name Generator.")
    street = input("What's the name of the city you grew up in?\n")
    pet = input("What's your pet's name?\n")
    print("Your band name could be " + street + "'s" +" " + pet)
    try_again=input("Wanna try again? y/n \n")
    if try_again=="y":
        GenerateBandName()
    else:
        quit()
GenerateBandName()