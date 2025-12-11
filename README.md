Fantasy Character Generator (Excel-Based)

A Python program that generates fully random NPC characters for a custom fantasy world. It uses regional lore, race-based traits, dice-rolled stats, and Excel-loaded name data via openpyxl.

Features

Regions: Borealans, Tropicanis, Selvarossa, Verdanian

Races: Human, Orc, Dwarf, Aelf, Faerie, Saurian, Halfling, Centaur

Physical Traits: Height, weight, hair color, eye color (race-specific)

Stats: Strength, Logic, Agility, Intellect, Toughness, Charm

Generated using tabletop-style dice mechanics

Names: Loaded from an Excel workbook (first + last when appropriate)

How It Works

Loads name data from Python Character Generator.xlsx using openpyxl.

Randomly selects region, race, city, and gender.

Generates physical traits using race-defined ranges.

Rolls stats using custom dice rules.

Builds and prints a formatted character profile.

Requirements

Python 3

openpyxl (pip install openpyxl)

The Excel file in the same directory
