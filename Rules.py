from worlds.generic.Rules import add_rule
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import Frickbears3World

# This is the last big thing to do (at least for me)
# This is where you add item
# These are omega simplified rules
# There are a ton of different ways you can add rules from amoount of items you need to optional items
# Theres also difficulty options and a bunch others
# Id suggest going through a bunch of different ap worlds and seeing how they do the rules
# Even better if its a game you know a lot about and can tell what you need to get to certain locations
def quotaRequirement(world: "Frickbears3World"):
    options = world.options
    return options.Difficulty


def set_rules(world: "Frickbears3World"):
    player = world.player
    options = world.options

    # Salvage Access
    add_rule(world.multiworld.get_entrance("Salvage1 -> Salvage2", player),
             lambda state: state.has_from_list(["Withered Freddy","Withered Bonnie","Withered Chica", "Withered Foxy", "Golden Freddy", "Endoskeleton"], player, count=quotaRequirement(world)))
    add_rule(world.multiworld.get_entrance("Salvage2 -> Salvage3", player),
             lambda state: state.has_from_list(["Toy Freddy","Toy Bonnie","Toy Chica", "Mangle", "JJ", "RWQFSFASXC"], player, count=quotaRequirement(world)))
    add_rule(world.multiworld.get_entrance("Salvage3 -> Salvage4", player),
             lambda state: state.has_from_list(["The Phantoms","Helpy","Mr. Hippo", "Music Man", "Shadow Freddy", "Malhare"], player, count=quotaRequirement(world)))
    add_rule(world.multiworld.get_entrance("Salvage4 -> Salvage5", player),
             lambda state: state.has_from_list(["Plushtrap","Nightmare Fredbear","Nightmare BB", "Nightmarionne", "Twisted Wolf", "Dreadbear"], player, count=quotaRequirement(world)) and state.has("Talbert's Files", player))
    add_rule(world.multiworld.get_entrance("Salvage1 -> Backdoor", player),
             lambda state: state.has("Progressive Backdoor Trading", player))
    
    # Victory Conditions
    if options.GoalEnding == 1:
        add_rule(world.multiworld.get_location("Complete Slacker Ending", player),
                lambda state: state.has_from_list(["Plushtrap","Nightmare Fredbear","Nightmare BB", "Nightmarionne", "Twisted Wolf", "Dreadbear"], player, count=quotaRequirement(world)))
    elif options.GoalEnding == 2:
        add_rule(world.multiworld.get_location("Complete Good Ending", player),
                lambda state: state.has_from_list(["Plushtrap","Nightmare Fredbear","Nightmare BB", "Nightmarionne", "Twisted Wolf", "Dreadbear"], player, count=quotaRequirement(world)) and state.has("Gift Box", player, count=4))
    elif options.GoalEnding == 3:
        add_rule(world.multiworld.get_location("Complete Evil Ending", player),
                lambda state: state.has_from_list(["Plushtrap","Nightmare Fredbear","Nightmare BB", "Nightmarionne", "Twisted Wolf", "Dreadbear"], player, count=quotaRequirement(world)) and state.has_all(["Springtrap", "Lefty", "Scrap Baby", "Molten Freddy", "Hatchet", "Parts & Services Key"], player))
    elif options.GoalEnding == 4:
        add_rule(world.multiworld.get_location("Complete Money Ending", player),
                lambda state: state.has_from_list(["Circus Baby","Funtime Freddy","Funtime Foxy", "Ballora", "Lolbit", "LolzHax"], player, count=quotaRequirement(world)))
    elif options.GoalEnding == 5:
        add_rule(world.multiworld.get_location("Complete Ultimate Ending", player),
                lambda state: state.has_from_list(["Plushtrap","Nightmare Fredbear","Nightmare BB", "Nightmarionne", "Twisted Wolf", "Dreadbear"], player, count=quotaRequirement(world)) and state.has("Gift Box", player, count=4) and state.has_all(["Springtrap", "Lefty", "Scrap Baby", "Molten Freddy", "Hatchet", "Parts & Services Key"], player) and state.has("Talbert's Files", player))
    
    # Animatronic Salvage requirements
    add_rule(world.multiworld.get_location("Salvage Withered Freddy", player),
            lambda state: state.has("Withered Freddy", player))
    add_rule(world.multiworld.get_location("Salvage Withered Bonnie", player),
            lambda state: state.has("Withered Bonnie", player))
    add_rule(world.multiworld.get_location("Salvage Withered Chica", player),
            lambda state: state.has("Withered Chica", player))
    add_rule(world.multiworld.get_location("Salvage Withered Foxy", player),
            lambda state: state.has("Withered Foxy", player))
    add_rule(world.multiworld.get_location("Salvage Golden Freddy", player),
            lambda state: state.has("Golden Freddy", player))
    add_rule(world.multiworld.get_location("Salvage Endoskeleton", player),
            lambda state: state.has("Endoskeleton", player))
    add_rule(world.multiworld.get_location("Salvage Springtrap", player),
            lambda state: state.has_all(["Springtrap", "Hatchet"], player))
    add_rule(world.multiworld.get_location("Salvage Toy Freddy", player),
            lambda state: state.has("Toy Freddy", player))
    add_rule(world.multiworld.get_location("Salvage Toy Bonnie", player),
            lambda state: state.has("Toy Bonnie", player))
    add_rule(world.multiworld.get_location("Salvage Toy Chica", player),
            lambda state: state.has("Toy Chica", player))
    add_rule(world.multiworld.get_location("Salvage Mangle", player),
            lambda state: state.has("Mangle", player))
    add_rule(world.multiworld.get_location("Salvage JJ", player),
            lambda state: state.has("JJ", player))
    add_rule(world.multiworld.get_location("Salvage RWQFSFASXC", player),
            lambda state: state.has("RWQFSFASXC", player))
    add_rule(world.multiworld.get_location("Salvage Lefty", player),
            lambda state: state.has_all(["Lefty", "Parts & Services Key"], player))
    add_rule(world.multiworld.get_location("Salvage The Phantoms", player),
            lambda state: state.has("The Phantoms", player))
    add_rule(world.multiworld.get_location("Salvage Helpy", player),
            lambda state: state.has("Helpy", player))
    add_rule(world.multiworld.get_location("Salvage Mr. Hippo", player),
            lambda state: state.has("Mr. Hippo", player))
    add_rule(world.multiworld.get_location("Salvage Music Man", player),
            lambda state: state.has("Music Man", player))
    add_rule(world.multiworld.get_location("Salvage Shadow Freddy", player),
            lambda state: state.has("Shadow Freddy", player))
    add_rule(world.multiworld.get_location("Salvage Malhare", player),
            lambda state: state.has("Malhare", player))
    add_rule(world.multiworld.get_location("Salvage Scrap Baby", player),
            lambda state: state.has("Scrap Baby", player))
    add_rule(world.multiworld.get_location("Salvage Plushtrap", player),
            lambda state: state.has("Plushtrap", player))
    add_rule(world.multiworld.get_location("Salvage Nightmare Fredbear", player),
            lambda state: state.has("Nightmare Fredbear", player))
    add_rule(world.multiworld.get_location("Salvage Nightmare BB", player),
            lambda state: state.has("Nightmare BB", player))
    add_rule(world.multiworld.get_location("Salvage Nightmarionne", player),
            lambda state: state.has("Nightmarionne", player))
    add_rule(world.multiworld.get_location("Salvage Twisted Wolf", player),
            lambda state: state.has("Twisted Wolf", player))
    add_rule(world.multiworld.get_location("Salvage Dreadbear", player),
            lambda state: state.has("Dreadbear", player))
    add_rule(world.multiworld.get_location("Salvage Molten Freddy", player),
            lambda state: state.has("Molten Freddy", player))
    add_rule(world.multiworld.get_location("Salvage Circus Baby", player),
            lambda state: state.has("Circus Baby", player))
    add_rule(world.multiworld.get_location("Salvage Funtime Freddy", player),
            lambda state: state.has("Funtime Freddy", player))
    add_rule(world.multiworld.get_location("Salvage Funtime Foxy", player),
            lambda state: state.has("Funtime Foxy", player))
    add_rule(world.multiworld.get_location("Salvage Ballora", player),
            lambda state: state.has("Ballora", player))
    add_rule(world.multiworld.get_location("Salvage Lolbit", player),
            lambda state: state.has("Lolbit", player))
    add_rule(world.multiworld.get_location("Salvage LolzHax", player),
            lambda state: state.has("LolzHax", player))

    #add_rule(world.multiworld.get_entrance("The Sewer -> Big Hole in the Floor", player),
    #         lambda state: state.has("A cute rat") and state.has("Estrogen") and state.has("Testosterone"))
    
    # Victory condition rule!
    world.multiworld.completion_condition[player] = lambda state: state.has("Victory", player)