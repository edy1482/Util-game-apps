import pandas as pd
import argparse

# This script takes in the pokemon types in your party and outputs two things:
# 1. The type advantages that your party has, e.g. if you have a water pokemon then you have a type advantage against fire
# This output should show a list of each type advantage from each type entered, e.g. Water -> Fire, Rock, Ground
#

# Load the csv into a DataFrame object
pathname = "chart.csv"
df = pd.read_csv(pathname)
# Grab all pokemon types
all_types = set(df.columns)
all_types.remove("Attacking")

# This returns a dictionary of the type matchups for a particular attacker type
def types_match_ups(type: str):
    # index = df.index.get_loc(type)
    # output = df.iloc[index]
    matchups = df[df["Attacking"] == type].to_dict()
    matchups.pop("Attacking")
    for key,val in matchups.items():
        matchups[key] = list(val.values())[0] # There is only one item, as there is only one row
    return matchups

# This returns a type advantage or disadvantage based on the bool
def type_ad_vantage(type: str, advantage: bool):
    d = types_match_ups(type)
    output = []
    for key, val in d.items():
        if advantage and val == 2:
            output.append(key)
    return output

def type_advantage_set(ltypes):
    output = []
    for type in ltypes: 
        output += type_ad_vantage(type)
    return set(output)

def missing_types(type_set):
    return all_types - type_set

def main():
    test = ["Grass", "Dark", "Psychic", "Fairy", "Fighting", "Ghost", "Flying", "Fire", "Ground", "Dragon", "Flying", "Electric"]
    test_set = type_advantage_set(test)
    print(test_set)
    print(missing_types(test_set))

if __name__ == "__main__":
    main()