def roll_call_dwarves(dwarves):
    count =1
    for dwarf in dwarves:
        print(f"{count}. {dwarf}")
        count +=1

def summon_captain_planet(planeteer_Calls):
     return [call.capitalize()+"!" for call in planeteer_Calls]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(snacks):
    cheeses = ["cheddar", "gouda", "camembert"]
    for cheese in cheeses:
        if cheese in snacks:
            return cheese
