from typing import List, Dict, Any
from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Choice, OptionGroup, Toggle, Range, Visibility

# If youve ever gone to an options page and seen how sometimes options are grouped
# This is that
def create_option_groups() -> List[OptionGroup]:
    option_group_list: List[OptionGroup] = []
    for name, options in frickbears3_option_groups.items():
        option_group_list.append(OptionGroup(name=name, options=options))

    return option_group_list

class GoalEnding(Choice):
    """
    Determines which ending you need to complete to complete the game.

    Slacker requires making it to the end of night 5 without meeting any other ending criteria
    Good requires collecting all 4 masks in each of the four main salvage locations, you need to receive 4/5 gift boxes for this
    Evil requires salvaging all 4 scrap animatronics in each of the four main salvage locations, you need to receive each of the four as well as a Hatchet and the P&S Key
    Money requires receiving Talbert's Files and completing one more salvage and night at a bonus location
    Ultimate requires all 4 masks, all 4 scrap animatronics, Talbert's Files and a final chat with your old friend

    As a temporary note, Slacker Ending currently causes issues as Talbert's Files will prevent you from completing it, and I haven't been bothered to fully remove all Salvage5 locations/items if Slacker is selected
    """
    display_name = "Goal Ending"
    option_slacker_ending = 1
    option_good_ending = 2
    option_evil_ending = 3
    option_money_ending = 4
    option_ultimate_ending = 5
    default = 1

class Difficulty(Choice):
    """
    Determines which difficulty the game is set to.

    This affects how many salvages you are required to make at each location, as well as AI Levels for animatronics and bosses
    """
    display_name = "Difficulty"
    option_easy = 1
    option_normal = 2
    option_hard = 3
    option_lunatic = 4
    default = 2

class RandomiseSalvages(Toggle):
    """
    This randomises which animatronics can be salvaged where.
    """
    display_name = "Randomise Salvages"

class SalvageArcadeTokenBounty(Range):
    """
    How many cents you are rewarded for each token you get during Salvage Arcade minigames. (This value is not Dollars and will be divided by 100 ingame)
    """
    display_name = "Salvage Arcade Token Bounty"
    range_start = 0
    range_end = 10000

class RandomSalvageSeed(Range):
    """
    This shouldn't be visible, but this is randomised during generation and is passed along to the mod to ensure animatronics are randomised the same every game
    """
    visibility = Visibility.none 
    range_start = 0
    range_end = 999999999999

@dataclass
class Frickbears3Options(PerGameCommonOptions):
    GoalEnding:               GoalEnding
    Difficulty:               Difficulty
    RandomiseSalvages:        RandomiseSalvages
    SalvageArcadeTokenBounty: SalvageArcadeTokenBounty
    RandomSalvageSeed:        RandomSalvageSeed

# This is where you organize your options
# Its entirely up to you how you want to organize it
frickbears3_option_groups: Dict[str, List[Any]] = {
    "General Options": [GoalEnding, Difficulty, RandomiseSalvages]
}