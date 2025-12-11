# ========================
# PART 1: IMPORTS & CONSTANTS 
# ========================

import random


# ========================
# PART 2: Display Menu
# ========================

def menu():
    print("______________________Random Character Generator______________________\n")
    print("            This is a random character generator that will            \n")
    print("          create a character with the following information:          \n")
    print("              Home Region, Home City, Physical Features,              \n")
    print("                    Gender, Race, Stats, and Name                     \n\n")
    print("               Would you like to create a new character?              \n")

    user_choice = input("                                 Y/N: ")
    while user_choice.upper() not in ("Y", "N"):
        print("              That is not a valid input. Please Try Again.")
        user_choice = input("                                 Y/N: ")
    return user_choice


# ========================
# PART 3: WORLD BACKGROUND & REGIONS
# ========================

# Define the four regions with their themes, allowed races, and major cities

REGIONS = {
    "Borealans": {
        "theme": "Frozen tundra / taiga, harsh winters, long days (northern / Nordic)",
        "races": ["Human", "Orc", "Dwarf"],
        "cities": ["Hinterborne", "Frostmoor", "Drakkenstone"]
    },
    "Tropicanis": {
        "theme": "Southern tropics, rainforest, very humid, lots of life",
        "races": ["Human", "Saurian", "Halfling"],
        "cities": ["Everspring", "Doradel", "Calthos", "Langrisha", "Hambshala", "Lavayon"]
    },
    "Selvarossa": {
        "theme": "Island culture (Oceania-like)",
        "races": ["Human", "Aelf", "Faerie"],
        "cities": ["Bellariva", "Castrovivo", "Vetricella", "Castanera", "Rovella", "Forcillia"]
    },
    "Verdanian": {
        "theme": "Frontier world (colonial frontier America feel)",
        "races": ["Centaur", "Dwarf", "Aelf", "Orc"],
        "cities": ["Thistleton", "Skylorne", "Thornfell", "Redhook"]
    }
}

# List of possible genders
GENDERS = ["Male", "Female", "Nonbinary"]


# Randomly choose a region, race, city, and gender for the character
def generate_background():
    # pick a random region
    region_name = random.choice(list(REGIONS.keys()))
    region_info = REGIONS[region_name]
    
    # pick a race from that region
    race = random.choice(region_info["races"])
    
    # pick a city
    city = random.choice(region_info["cities"])
    
    # pick a gender
    gender = random.choice(GENDERS)
    
    # put it all together
    background = {
        "region": region_name,
        "city": city,
        "race": race,
        "gender": gender
    }
    
    return background


# ========================
# PART 4: PHYSICAL CHARACTERISTICS
# ========================

# Define height ranges for each race (stored as min and max in inches)
RACE_HEIGHT_RANGES = {
    "Human": (58, 78),      # 4'10" to 6'6"
    "Orc": (70, 90),        # 5'10" to 7'6"
    "Dwarf": (48, 65),      # 4'0" to 5'5"
    "Saurian": (54, 72),    # 4'6" to 6'0"
    "Halfling": (42, 58),   # 3'6" to 4'10"
    "Aelf": (67, 82),       # 5'7" to 6'10"
    "Faerie": (36, 54),     # 3'0" to 4'6"
    "Centaur": (72, 108)    # 6'0" to 9'0"
}

# Define weight ranges for each race (stored as min and max in pounds)
RACE_WEIGHT_RANGES = {
    "Human": (80, 400),
    "Orc": (250, 600),
    "Dwarf": (200, 400),
    "Saurian": (150, 300),
    "Halfling": (40, 150),
    "Aelf": (120, 200),
    "Faerie": (30, 100),
    "Centaur": (1000, 2500)
}

# Define hair color options for each race
RACE_HAIR_COLORS = {
    "Human": ["Black", "Brown", "Red", "Blonde", "Gray"],
    "Orc": ["Black"],
    "Dwarf": ["Black", "Brown", "Red", "Blonde", "Gray"],
    "Saurian": ["None"],  # Saurians don't have hair
    "Halfling": ["Black", "Brown", "Red", "Blonde", "Gray"],
    "Aelf": ["Blonde", "White", "Silver", "Copper", "Black"],
    "Faerie": ["Black", "Brown", "Red", "Orange", "Yellow", "Green", "Blue", "Purple"],
    "Centaur": ["Brown", "White", "Black", "Gray", "Auburn"]
}

# Define eye color options for each race
RACE_EYE_COLORS = {
    "Human": ["Blue", "Brown", "Green", "Hazel", "Amber"],
    "Orc": ["Black", "Brown", "Red"],
    "Dwarf": ["Black", "Brown"],
    "Saurian": ["Purple", "Red", "Black"],
    "Halfling": ["Blue", "Brown", "Green", "Hazel", "Amber"],
    "Aelf": ["Blue", "Brown", "Green", "Hazel", "Amber", "Lilac", "Red"],
    "Faerie": ["Gold", "Red", "Green", "Blue", "Magenta"],
    "Centaur": ["Blue", "Brown", "Green", "Hazel", "Amber"]
}


# Convert inches to feet and inches format like "5'11\""
def convert_inches_to_feet_inches(total_inches):
    feet = total_inches // 12
    inches = total_inches % 12
    height_string = str(feet) + "'" + str(inches) + '"'
    return height_string


# Generate physical traits (height, weight, hair color, eye color) based on race
def generate_physical_traits(race):
    # get height range
    min_height_inches, max_height_inches = RACE_HEIGHT_RANGES[race]
    
    # pick random height
    height_inches = random.randint(min_height_inches, max_height_inches)
    
    # convert to feet and inches
    height_string = convert_inches_to_feet_inches(height_inches)
    
    # get weight range
    min_weight, max_weight = RACE_WEIGHT_RANGES[race]
    
    # pick random weight
    weight = random.randint(min_weight, max_weight)
    
    # get hair colors
    hair_colors = RACE_HAIR_COLORS[race]
    
    # pick hair color
    hair_color = random.choice(hair_colors)
    
    # get eye colors
    eye_colors = RACE_EYE_COLORS[race]
    
    # pick eye color
    eye_color = random.choice(eye_colors)
    
    # return everything
    physical_traits = {
        "height": height_string,
        "weight": weight,
        "hair_color": hair_color,
        "eye_color": eye_color
    }
    
    return physical_traits


# ========================
# PART 5: STATS GENERATOR (DICE MECHANICS)
# ========================

# Roll one die with the given number of sides
def roll_die(sides):
    result = random.randint(1, sides)
    return result


# Roll multiple dice and return a list of results
def roll_dice(number_of_dice, sides):
    dice_results = []
    for i in range(number_of_dice):
        result = roll_die(sides)
        dice_results.append(result)
    return dice_results


# Roll Strength: roll 4d6, drop lowest, sum remaining three
def roll_strength():
    dice_rolls = roll_dice(4, 6)
    dice_rolls.sort()
    dice_rolls.pop(0)  # remove lowest
    total = sum(dice_rolls)
    return total


# Roll Logic: roll 3d6, reroll 1s until all are 2+, then sum
def roll_logic():
    dice_rolls = roll_dice(3, 6)
    
    # reroll 1s
    for i in range(len(dice_rolls)):
        while dice_rolls[i] == 1:
            dice_rolls[i] = roll_die(6)
    
    total = sum(dice_rolls)
    return total


# Roll Agility: roll 5d6, drop highest, sum remaining four, cap at 18
def roll_agility():
    dice_rolls = roll_dice(5, 6)
    dice_rolls.sort()
    dice_rolls.pop()  # remove highest
    total = sum(dice_rolls)
    if total > 18:
        total = 18
    return total


# Roll Intellect: roll 2d6 and add 6
def roll_intellect():
    rolls = roll_dice(2, 6)
    total = sum(rolls) + 6
    return total


# Roll Toughness: roll 4d6, reroll 1s, drop lowest, sum remaining three
def roll_toughness():
    dice_rolls = roll_dice(4, 6)
    
    # reroll 1s
    for i in range(len(dice_rolls)):
        while dice_rolls[i] == 1:
            dice_rolls[i] = roll_die(6)
    
    dice_rolls.sort()
    dice_rolls.pop(0)  # remove lowest
    total = sum(dice_rolls)
    return total


# Roll Charm: roll 1d20, subtract 2, clamp to 3-18 range
def roll_charm():
    result = roll_die(20)
    total = result - 2
    
    if total < 3:
        total = 3
    if total > 18:
        total = 18
    
    return total


# Generate all six stats using the dice rules
def generate_stats():
    strength = roll_strength()
    logic = roll_logic()
    agility = roll_agility()
    intellect = roll_intellect()
    toughness = roll_toughness()
    charm = roll_charm()
    
    stats = {
        "Strength": strength,
        "Logic": logic,
        "Agility": agility,
        "Intellect": intellect,
        "Toughness": toughness,
        "Charm": charm
    }
    
    return stats


# ========================
# PART 6: NAME GENERATOR 
# ========================

def name_generator(region, race, gender): #generate the names of the species
    file_name = None  # initialize variable

    #humans
    if race == "Human":
        if gender == "Male":
            file_name = region.lower() + "_male_human_names.txt"
        else:
            file_name = region.lower() + "_female_human_names.txt"

    #Dwarves
    elif race == "Dwarf":
        if gender == "Male":
            file_name = "male_dwarven_names.txt"
        else:
            file_name = "female_dwarven_names.txt"

    #orcs
    elif race == "Orc":
        file_name = "northern_orc_first_names.txt"

    #Halflings
    elif race == "Halfling":
        if gender == "Male":
            file_name = "male_halfling_names.txt"
        else:
            file_name = "female_halfling_names.txt"

    #ealves
    elif race == "Aelf":
        if gender == "Male":
            file_name = "male_aelven_names.txt"
        else:
            file_name = "female_aelven_names.txt"

    #Faeries
    elif race == "Faerie":
        file_name = "faerie_first_names.txt"

    #Centaurs
    elif race == "Centaur":
        if gender == "Male":
            file_name = "male_centaur_names.txt"
        else:
            file_name = "female_centaur_names.txt"

    #Saurians
    elif race == "Saurian":
        file_name = "saurian_first_names.txt"

    #If no file was matched raise an error
    if file_name is None:
        raise ValueError(f"No name file found for race: {race}, gender: {gender}, region: {region}")

    #Open first name file
    with open(file_name, "r") as f:
        first_name = random.choice(f.readlines()).strip()

    #Determine last name
    last_name = ""
    if race in ["Human", "Orc", "Aelf", "Faerie", "Saurian", "Halfling"]:
        if race == "Human":
            last_file = region.lower() + "_human_last_names.txt"
        elif race == "Orc":
            last_file = "northern_orc_last_names.txt"
        elif race == "Halfling":
            last_file = "halfling_last_names.txt"
        elif race == "Aelf":
            last_file = "aelven_last_names.txt"
        elif race == "Faerie":
            last_file = "faerie_last_names.txt"
        elif race == "Saurian":
            last_file = "saurian_last_names.txt"

        with open(last_file, "r") as f:
            last_name = random.choice(f.readlines()).strip()

    #Return either "First Last" or just "First" if last_name is empty
    return f"{first_name} {last_name}".strip()

def generate_character():
    background = generate_background()
    physical_traits = generate_physical_traits(background["race"])
    stats = generate_stats()
    name = name_generator(background["region"], background["race"], background["gender"])
    
    character = {
        "name": name,
        "region": background["region"],
        "city": background["city"],
        "race": background["race"],
        "gender": background["gender"],
        "height": physical_traits["height"],
        "weight": physical_traits["weight"],
        "hair_color": physical_traits["hair_color"],
        "eye_color": physical_traits["eye_color"],
        "stats": stats
    }
    
    return character


# ========================
# PART 7: USER INTERFACE (MAIN PROGRAM)
# ========================

# Print a character profile
def print_character(character):
    print("========================================")
    print("Name: " + character["name"])
    print("Region: " + character["region"])
    print("City of Origin: " + character["city"])
    print("Race: " + character["race"])
    print("Gender: " + character["gender"])
    print("Physical Description:")
    print("  Height: " + character["height"])
    print("  Weight: " + str(character["weight"]) + " lbs")
    print("  Hair Color: " + character["hair_color"])
    print("  Eye Color: " + character["eye_color"])
    print("Stats:")
    print("  Strength: " + str(character["stats"]["Strength"]))
    print("  Logic: " + str(character["stats"]["Logic"]))
    print("  Agility: " + str(character["stats"]["Agility"]))
    print("  Intellect: " + str(character["stats"]["Intellect"]))
    print("  Toughness: " + str(character["stats"]["Toughness"]))
    print("  Charm: " + str(character["stats"]["Charm"]))
    print("========================================")
    print()



def main():

    user_choice = menu()
    if user_choice.upper() == "N":
        print("Alright, cya next time")
    
    else:   
        #ask for input until we get a valid number
        valid_input = False
        number_of_characters = 0

        while not valid_input:
            user_input = input("How many characters would you like to generate? ")
        
            # check if input is all digits
            if user_input.isdigit():
                number_of_characters = int(user_input)
            
                # check if it's positive
                if number_of_characters > 0:
                    valid_input = True
                else:
                    print("Please enter a positive number (greater than 0).")
            else:
                print("Please enter a valid number.")
    
    
        print()
        print("Generating " + str(number_of_characters) + " character(s)...")
        print()
    
        all_characters = []
        for i in range(number_of_characters):
            char = generate_character()
            all_characters.append(char)
    
        for char in all_characters:
            print_character(char)








main()



