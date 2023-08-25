def roll_call_dwarves(list):
    for count, element in enumerate(list, 1):
        print(f"{count}. {element}")

def summon_captain_planet(list):
    return [f"{element.title()}!" for element in list]

def long_planeteer_calls(list):
    over_four_bool_list = [len(element)>4 for element in list]
    return any(over_four_bool_list)

def find_the_cheese(list):
    cheese_types = ["cheddar", "gouda", "camembert"]
    for food in list:
        if food in cheese_types:
            return food
    else:
        return None
