# Look at init or Items.py for more information on imports
from typing import Dict, TYPE_CHECKING
import logging

from .Types import LocData

if TYPE_CHECKING:
    from . import Frickbears3World

def get_selected_ending_name(world: "Frickbears3World") -> str:
    options = world.options

    if options.GoalEnding == 1:
        return "Complete Slacker Ending"
    elif options.GoalEnding == 2:
        return "Complete Good Ending"
    elif options.GoalEnding == 3:
        return "Complete Evil Ending"
    elif options.GoalEnding == 4:
        return "Complete Money Ending"
    elif options.GoalEnding == 5:
        return "Complete Ultimate Ending"

# This is used by ap and in Items.py
# Theres a multitude of reasons to need to grab how many locations there are
def get_total_locations(world: "Frickbears3World") -> int:
    # This is the total that we'll keep updating as we count how many locations there are
    total = 0
    for name in location_table:
        # If the location is valid though, count it
        if is_valid_location(world, name):
            total += 1

    return total

def get_location_names() -> Dict[str, int]:
    # This is just a fancy way of getting all the names and data in the location table and making a dictionary thats {name, code}
    # If you have dynamic locations then you want to add them to the dictionary as well
    names = {name: data.ap_code for name, data in location_table.items()}

    return names

# The check to make sure the location is valid
# I know it looks like the same as when we counted it but thats because this is an example
# Things get complicated fast so having a back up is nice
def is_valid_location(world: "Frickbears3World", name) -> bool:
    if name == "Complete Slacker Ending":
        if get_selected_ending_name(world) == name:
            return True
        else:
            return False
    elif name == "Complete Good Ending":
        if get_selected_ending_name(world) == name:
            return True
        else:
            return False
    elif name == "Complete Evil Ending":
        if get_selected_ending_name(world) == name:
            return True
        else:
            return False
    elif name == "Complete Money Ending":
        if get_selected_ending_name(world) == name:
            return True
        else:
            return False
    elif name == "Complete Ultimate Ending":
        if get_selected_ending_name(world) == name:
            return True
        else:
            return False
    else:
        return True
    
def dep_is_valid_location(world: "Frickbears3World", name) -> bool:
    return True

# You might need more functions as well so be liberal with them
# My advice, if you are about to type the same thing in a second time, turn it into a function
# Even if you only do it once you can turn it into a function too for organization

# Heres where you do the next fun part of listing out all those locations
# Its a lot
# My advice, zone out for half an hour listening to music and hope you wake up to a completed list
frickbears3_locations = {
    # Salvaging Animatronics
    "Salvage Withered Freddy": LocData(19875001, "Salvage1"),  
    "Salvage Withered Bonnie": LocData(19875002, "Salvage1"),
    "Salvage Withered Chica": LocData(19875003, "Salvage1"),
    "Salvage Withered Foxy": LocData(19875004, "Salvage1"),
    "Salvage Golden Freddy": LocData(19875005, "Salvage1"),
    "Salvage Endoskeleton": LocData(19875006, "Salvage1"),
    "Salvage Springtrap": LocData(19875007, "Salvage1"),
    "Salvage Toy Freddy": LocData(19875008, "Salvage2"),
    "Salvage Toy Bonnie": LocData(19875009, "Salvage2"),
    "Salvage Toy Chica": LocData(19875010, "Salvage2"),
    "Salvage Mangle": LocData(19875011, "Salvage2"),
    "Salvage JJ": LocData(19875012, "Salvage2"),
    "Salvage RWQFSFASXC": LocData(19875013, "Salvage2"),
    "Salvage Lefty": LocData(19875014, "Salvage2"),
    "Salvage The Phantoms": LocData(19875015, "Salvage3"),
    "Salvage Helpy": LocData(19875016, "Salvage3"),
    "Salvage Shadow Freddy": LocData(19875017, "Salvage3"),
    "Salvage Mr. Hippo": LocData(19875018, "Salvage3"),
    "Salvage Music Man": LocData(19875019, "Salvage3"),
    "Salvage Malhare": LocData(19875020, "Salvage3"),
    "Salvage Scrap Baby": LocData(19875021, "Salvage3"),
    "Salvage Plushtrap": LocData(19875022, "Salvage4"),
    "Salvage Nightmare Fredbear": LocData(19875023, "Salvage4"),
    "Salvage Nightmare BB": LocData(19875024, "Salvage4"),
    "Salvage Nightmarionne": LocData(19875025, "Salvage4"),
    "Salvage Dreadbear": LocData(19875026, "Salvage4"),
    "Salvage Twisted Wolf": LocData(19875027, "Salvage4"),
    "Salvage Molten Freddy": LocData(19875028, "Salvage4"),
    "Salvage Circus Baby": LocData(19875029, "Salvage5"),
    "Salvage Funtime Freddy": LocData(19875030, "Salvage5"),
    "Salvage Funtime Foxy": LocData(19875031, "Salvage5"),
    "Salvage Ballora": LocData(19875032, "Salvage5"),
    "Salvage Lolbit": LocData(19875033, "Salvage5"),
    "Salvage LolzHax": LocData(19875034, "Salvage5"),
    "Salvage Coffee": LocData(19875035, "Backdoor"),
    "Salvage Chipper": LocData(19875036, "Backdoor"),
    "Salvage Animdude": LocData(19875037, "Backdoor"),
    "Salvage Sparky": LocData(19875038, "Backdoor"),
    "Salvage Candy": LocData(19875039, "Backdoor"),
    "Salvage Popgoes": LocData(19875040, "Backdoor"),
    "Salvage Rodney": LocData(19875041, "Backdoor"),

    # Purchasing Upgrades
    "Purchase AP Item #1": LocData(19875042, "Salvage1"),
    "Purchase AP Item #2": LocData(19875043, "Salvage1"),
    "Purchase AP Item #3": LocData(19875044, "Salvage1"),
    "Purchase AP Item #4": LocData(19875045, "Salvage1"),
    "Purchase AP Item #5": LocData(19875046, "Salvage1"),
    "Purchase AP Item #6": LocData(19875047, "Salvage1"),
    "Purchase AP Item #7": LocData(19875048, "Salvage1"),
    "Purchase AP Item #8": LocData(19875049, "Salvage1"),
    "Purchase AP Item #9": LocData(19875050, "Salvage1"),
    "Purchase AP Item #10": LocData(19875051, "Salvage1"),
    "Purchase AP Item #11": LocData(19875052, "Salvage1"),
    "Purchase AP Item #12": LocData(19875053, "Salvage1"),
    "Purchase AP Item #13": LocData(19875054, "Salvage1"),
    "Purchase AP Item #14": LocData(19875055, "Salvage1"),
    "Purchase AP Item #15": LocData(19875056, "Salvage1"),
    "Purchase AP Item #16": LocData(19875057, "Salvage1"),
    "Purchase AP Item #17": LocData(19875058, "Salvage1"),
    "Purchase AP Item #18": LocData(19875059, "Salvage1"),
    "Purchase AP Item #19": LocData(19875060, "Salvage1"),
    "Purchase AP Item #20": LocData(19875061, "Salvage1"),
    "Purchase AP Item #21": LocData(19875062, "Salvage1"),
    "Purchase AP Item #22": LocData(19875063, "Salvage1"),
    "Purchase AP Item #23": LocData(19875064, "Salvage1"),
    "Purchase AP Item #24": LocData(19875065, "Salvage1"),
    "Purchase AP Item #25": LocData(19875066, "Salvage1"),
    "Purchase AP Item #26": LocData(19875067, "Salvage1"),
    "Purchase AP Item #27": LocData(19875068, "Salvage1"),
    "Purchase AP Item #28": LocData(19875069, "Salvage1"),
    "Purchase AP Item #29": LocData(19875070, "Salvage1"),
    "Purchase AP Item #30": LocData(19875071, "Salvage1"),
    "Purchase AP Item #31": LocData(19875072, "Salvage1"),
    "Purchase AP Item #32": LocData(19875073, "Salvage1"),
    "Purchase AP Item #33": LocData(19875074, "Salvage1"),
    "Purchase AP Item #34": LocData(19875075, "Salvage1"),
    "Purchase AP Item #35": LocData(19875076, "Salvage1"),
    "Purchase AP Item #36": LocData(19875077, "Salvage1"),
    "Purchase AP Item #37": LocData(19875078, "Salvage1"),
    "Purchase AP Item #38": LocData(19875079, "Salvage1"),
    "Purchase AP Item #39": LocData(19875080, "Salvage1"),
    "Purchase AP Item #40": LocData(19875081, "Salvage1"),
    "Purchase AP Item #41": LocData(19875082, "Salvage1"),
    "Purchase AP Item #42": LocData(19875083, "Salvage1"),

    # Misc
    "Pickup Item in Parts and Services": LocData(19875084, "Salvage1"),
    "Complete BB's Quiz": LocData(19875085, "Salvage2"),
    "Hi-Score on Chomping with Chica": LocData(19875086, "Salvage1"),
    "Hi-Score on Puppet Patrol": LocData(19875087, "Salvage2"),
    "Hi-Score on Hare's Pairs": LocData(19875088, "Salvage3"),
    "Hi-Score on Pirate Plunder": LocData(19875089, "Salvage4"),
    "Hi-Score on Circus Sorter": LocData(19875090, "Salvage5"),

    "Complete Slacker Ending": LocData(19875091, "Salvage4"),
    "Complete Good Ending": LocData(19875092, "Salvage4"),
    "Complete Evil Ending": LocData(19875093, "Salvage4"),
    "Complete Money Ending": LocData(19875094, "Salvage5"),
    "Complete Ultimate Ending": LocData(19875095, "Salvage4")

    # Victory goals
   # "Complete Slacker Ending": LocData(19875091, "Salvage 4"),
    #"Complete Good Ending": LocData(19875092, "Salvage 4"),
    #"Complete Evil Ending": LocData(19875093, "Salvage 4"),
    #"Complete Money Ending": LocData(19875094, "Salvage 5"),
    #"Complete Ultimate Ending": LocData(19875095, "Salvage 4")

}

# Like in Items.py, breaking up the different locations to help with organization and if something special needs to happen to them
event_locations = {
    "Testing ma shit": LocData(19875096, "Salvage 1")
}

# Also like in Items.py, this collects all the dictionaries together
# Its important to note that locations MUST be bigger than progressive item count and should be bigger than total item count
# Its not here because this is an example and im not funny enough to think of more locations
# But important to note
location_table = {
    **frickbears3_locations,
    **event_locations
}