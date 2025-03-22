import pandas as pd

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
    matchups = df[df["Attacking"] == type].to_dict()
    matchups.pop("Attacking")
    for key,val in matchups.items():
        matchups[key] = list(val.values())[0] # There is only one item, as there is only one row
    return matchups

# This returns a list of type advantages or disadvantages based on the bool
def type_advantage(type: str, advantage: bool) -> list:
    d = types_match_ups(type)
    output = []
    for key, val in d.items():
        if advantage and val > 1:
            output.append(key)
        elif not advantage and val < 1:
            output.append(key)
    return output

def type_advantage_set(l_types: list) -> set:
    output = []
    for type in l_types: 
        output += type_advantage(type, True)
    return set(output)

# Testing
def main():
    pass

if __name__ == "__main__":
    main()