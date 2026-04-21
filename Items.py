# So the goal here is to have a catalog of all the items in your game
# To correctly generate a games items they need to be bundled in a list
# A list in programming terms is anything in square brackets [] to put it simply

# When a list is described its described as a list of x where x is the type of variable within it
# IE: ["apple", "pear", "grape"] is a list of strings (anything inside "" OR '' are considered strings)

# Logging = output. How you'll figure out whats going wrong
import logging

# Built in AP imports
from BaseClasses import Item, ItemClassification

# These come from the other files in this example. If you want to see the source ctrl + click the name
# You can also do that ctrl + click for any functions to see what they do
from .Types import ItemData, ChapterType, Frickbears3Item, chapter_type_to_name
from .Locations import get_total_locations
from typing import List, Dict, TYPE_CHECKING

# This is just making sure nothing gets confused dw about what its doing exactly
if TYPE_CHECKING:
    from . import Frickbears3World

# If you're curious about the -> List[Item] that is a syntax to make sure you return the correct variable type
# In this instance we're saying we only want to return a list of items
# You'll see a bunch of other examples of this in other functions
# It's main purpose is to protect yourself from yourself

def returnEndingName(world: "Frickbears3World"):
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
    else:
        raise Exception

def create_itempool(world: "Frickbears3World") -> List[Item]:
    # This is the empty list of items. You'll add all the items in the game to this list
    options = world.options
    itempool: List[Item] = []

    for item in item_table:
        data = item_table[item]
        if options.GoalEnding == 1:
            if item == "Talbert's Files":
                continue
        for x in range(data.count):
            itempool.append(create_item(world, item))

    # In this function is where you would remove any starting items that you add in options such as starting chapter
    # This is also the place you would add dynamic amounts of items from options
    # I can point to Sly Cooper and the Thievious Raccoonus since I did that

    # This is a good place to grab anything you need from options

    # For this example I'll make it so there is a starting chapter
    # We loop through all the chapters in the my_chapter section
    
    # It's up to you and how you want things organized but I like to deal with victory here
    # This creates your win item and then places it at the "location" where you win
    victory = create_item(world, "Victory")

    world.multiworld.get_location(returnEndingName(world), world.player).place_locked_item(victory)

    # Then junk items are made
    # Check out the create_junk_items function for more details
    itempool += create_junk_items(world, get_total_locations(world) - len(itempool) - 1)

    return itempool

# This is a generic function to create a singular item
def create_item(world: "Frickbears3World", name: str) -> Item:
    data = item_table[name]
    return Frickbears3Item(name, data.classification, data.ap_code, world.player)

# Another generic function. For creating a bunch of items at once!
def create_multiple_items(world: "Frickbears3World", name: str, count: int,
                          item_type: ItemClassification = ItemClassification.progression) -> List[Item]:
    data = item_table[name]
    itemlist: List[Item] = []

    for i in range(count):
        itemlist += [Frickbears3Item(name, item_type, data.ap_code, world.player)]

    return itemlist

# Finally, where junk items are created
def create_junk_items(world: "Frickbears3World", count: int) -> List[Item]:
    trap_chance = 0
    junk_pool: List[Item] = []
    junk_list: Dict[str, int] = {}
    trap_list: Dict[str, int] = {}

    # This grabs all the junk items and trap items
    for name in item_table.keys():
        # Here we are getting all the junk item names and weights
        ic = item_table[name].classification
        if ic == ItemClassification.filler:
            junk_list[name] = junk_weights.get(name)

        # This is for traps if your randomization includes it
        # It also grabs the trap weights from the options page

    # Where all the magic happens of adding the junk and traps randomly
    # AP does all the weight management so we just need to worry about how many are created
    for i in range(count):
        if trap_chance > 0 and world.random.randint(1, 100) <= trap_chance:
            junk_pool.append(world.create_item(
                world.random.choices(list(trap_list.keys()), weights=list(trap_list.values()), k=1)[0]))
        else:
            junk_pool.append(world.create_item(
                world.random.choices(list(junk_list.keys()), weights=list(junk_list.values()), k=1)[0]))

    return junk_pool

# Time for the fun part of listing all of the items
# Watch out for overlap with your item codes
# These are just random numbers dont trust them PLEASE
# I've seen some games that dynamically add item codes such as DOOM as well
frickbears_items = {
    # Animatronics
    "Withered Freddy": ItemData(19870001, ItemClassification.progression, 1),
    "Withered Bonnie": ItemData(19870002, ItemClassification.progression, 1),
    "Withered Chica": ItemData(19870003, ItemClassification.progression, 1),
    "Withered Foxy": ItemData(19870004, ItemClassification.progression, 1),
    "Golden Freddy": ItemData(19870005, ItemClassification.progression, 1),
    "Endoskeleton": ItemData(19870006, ItemClassification.progression, 1),
    "Springtrap": ItemData(19870007, ItemClassification.progression, 1),
    "Toy Freddy": ItemData(19870008, ItemClassification.progression, 1),
    "Toy Bonnie": ItemData(19870009, ItemClassification.progression, 1),
    "Toy Chica": ItemData(19870010, ItemClassification.progression, 1),
    "Mangle": ItemData(19870011, ItemClassification.progression, 1),
    "JJ": ItemData(19870012, ItemClassification.progression, 1),
    "RWQFSFASXC": ItemData(19870013, ItemClassification.progression, 1),
    "Lefty": ItemData(19870014, ItemClassification.progression, 1),
    "The Phantoms": ItemData(19870015, ItemClassification.progression, 1),
    "Helpy": ItemData(19870016, ItemClassification.progression, 1),
    "Shadow Freddy": ItemData(19870017, ItemClassification.progression, 1),
    "Mr. Hippo": ItemData(19870018, ItemClassification.progression, 1),
    "Music Man": ItemData(19870019, ItemClassification.progression, 1),
    "Malhare": ItemData(19870020, ItemClassification.progression, 1),
    "Scrap Baby": ItemData(19870021, ItemClassification.progression, 1),
    "Plushtrap": ItemData(19870022, ItemClassification.progression, 1),
    "Nightmare Fredbear": ItemData(19870023, ItemClassification.progression, 1),
    "Nightmare BB": ItemData(19870024, ItemClassification.progression, 1),
    "Nightmarionne": ItemData(19870025, ItemClassification.progression, 1),
    "Dreadbear": ItemData(19870026, ItemClassification.progression, 1),
    "Twisted Wolf": ItemData(19870027, ItemClassification.progression, 1),
    "Molten Freddy": ItemData(19870028, ItemClassification.progression, 1),
    "Circus Baby": ItemData(19870029, ItemClassification.progression, 1),
    "Funtime Freddy": ItemData(19870030, ItemClassification.progression, 1),
    "Funtime Foxy": ItemData(19870031, ItemClassification.progression, 1),
    "Ballora": ItemData(19870032, ItemClassification.progression, 1),
    "Lolbit": ItemData(19870033, ItemClassification.progression, 1),
    "LolzHax": ItemData(19870034, ItemClassification.progression, 1),
    "Coffee": ItemData(19870035, ItemClassification.progression, 1),
    "Chipper": ItemData(19870036, ItemClassification.progression, 1),
    "Animdude": ItemData(19870037, ItemClassification.progression, 1),
    "Sparky": ItemData(19870038, ItemClassification.progression, 1),
    "Candy": ItemData(19870039, ItemClassification.progression, 1),
    "Popgoes": ItemData(19870040, ItemClassification.progression, 1),
    "Rodney": ItemData(19870041, ItemClassification.progression, 1),

    # Upgrades
    "Progressive Overcharge": ItemData(19870042, ItemClassification.useful, 3),
    "Progressive Mini Multiplier": ItemData(19870043, ItemClassification.useful, 3),
    "Progressive Employee Discount": ItemData(19870044, ItemClassification.useful, 2),
    "Progressive Backdoor Trading": ItemData(19870045, ItemClassification.progression, 3),
    "Progressive Cam Radar": ItemData(19870046, ItemClassification.useful, 2),
    "Progressive Superfan": ItemData(19870047, ItemClassification.useful, 2),
    "Progressive Headstart": ItemData(19870048, ItemClassification.useful, 3),
    "Progressive Overstock": ItemData(19870049, ItemClassification.useful, 2),
    "Progressive Early Investment": ItemData(19870050, ItemClassification.useful, 4),
    "Progressive Felix's Loan": ItemData(19870051, ItemClassification.useful, 3),
    "Progressive Fuzzy Dice": ItemData(19870052, ItemClassification.useful, 2),
    "Progressive Power AC": ItemData(19870053, ItemClassification.useful, 2),
    "Progressive Bear Change": ItemData(19870054, ItemClassification.useful, 2),
    "Progressive Mask Upgrade": ItemData(19870055, ItemClassification.useful, 2),
    "Progressive Retina Burner": ItemData(19870056, ItemClassification.useful, 2),
    "Mangle Cartridge": ItemData(19870057, ItemClassification.useful, 1),
    "Cupcake Cartridge": ItemData(19870058, ItemClassification.useful, 1),
    "Animdude Cartridge": ItemData(19870059, ItemClassification.useful, 1),
    "Spawnkiller": ItemData(19870060, ItemClassification.useful, 1),
    "Talbert's Files": ItemData(19870061, ItemClassification.progression, 1),

    # Misc
    "Hatchet": ItemData(19870062, ItemClassification.progression, 1),
    "Parts & Services Key": ItemData(19870063, ItemClassification.progression, 1),
    "Gift Box": ItemData(19870064, ItemClassification.progression, 5),
    "Victory": ItemData(19870065, ItemClassification.progression, 0)
}

# I like to split up the items so that its easier to look at and since sometimes you only need to look at one specific type of list
# An example of that is in create_itempool where I simulated having a starting chapter
# In the way that I made items, I added a way to specify how many of an item should exist
# That's why junk has a 0 since how many are created is in the create_junk_items
# There is a better way of doing this but this is my jank
junk_items = {
    # Junk
    "$25": ItemData(19870066, ItemClassification.filler, 0),

    # Traps
    "Random Bonus Animatronic": ItemData(19870067, ItemClassification.trap, 0)
}

# Junk weights is just how often an item will be chosen when junk is being made
# Bigger item = more likely to show up
junk_weights = {
    "$25": 40
}

# This makes a really convenient list of all the other dictionaries
# (fun fact: {} is a dictionary)
item_table = {
    **frickbears_items,
    **junk_items
}