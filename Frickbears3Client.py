from __future__ import annotations
import os
import sys
import asyncio
import shutil
import platform

import ModuleUpdate
ModuleUpdate.update()

import Utils

plat = platform.platform()
if "Linux" in plat:
    path = os.path.expandvars("$HOME/.wine/drive_c/users/$USER/AppData/Local/Frickbears3")
elif "Windows" in plat:
    path = os.path.expandvars(r"%LOCALAPPDATA%\Frickbears3")
else:
    raise Exception(f"Platform {plat} not supported")

if __name__ == "__main__":
    Utils.init_logging("Frickbears3Client", exception_logger="Client")

from NetUtils import NetworkItem, ClientStatus
from CommonClient import gui_enabled, logger, get_base_parser, ClientCommandProcessor, \
    CommonContext, server_loop

def salvageID_to_locID(salvageID: int) -> int:
    salArray = [0,0,0,0,19875005,19875006,19875008,19875009,19875010,19875011,19875001,19875002,19875003,19875004,0,19875012,0,19875017,19875013,19875015,19875007,19875022,19875023,19875024,19875025,19875033,19875029,19875030,19875031,19875032,19875016,19875019,19875018,19875014,19875028,19875021,19875027,19875020,19875026,19875034,19875035,19875036,19875037,19875038,19875039,19875040,19875041]
    return salArray[salvageID]

def shopID_to_locID(shopID: int) -> int:
    base = 19875000
    return (base+shopID)

def salvUpgradeID_to_locID(salvUpgradeID: int) -> int:
    base = 19874908
    return (base+salvUpgradeID)

def itemIDCount_to_upgradeID(itemID: int, count: int) -> float:
    Overcharge = [0,0.0,1.0,2.0]
    MiniMultipler = [0,3.0,4.0,5.0]
    EmployDiscount = [0,6.0,7.0]
    BackdoorTrade = [0,8.0,9.0,10.0]
    CamRadar = [0,11.0,12.0]
    Superfan = [0,13.0,14.0]
    Headstart = [0,15.0,16.0,17.0]
    Overstock = [0,18.0,19.0]
    Investment = [0,20.0,21.0,22.0,23.0]
    Loan = [0,24.0,25.0,26.0]
    MangleCart = [0,27.0]
    CupcakeCart = [0,28.0]
    AnimdudeCart = [0,29.0]
    FuzzyDice = [0,30.0,31.0]
    PowerAC = [0,32.0,33.0]
    BearChange = [0,34.0,35.0]
    MaskUpgr = [0,36.0,37.0]
    Retina = [0,38.0,39.0]
    Spawnkiller = [0,40.0]
    Talbert = [0,41.0]
    Hatchet = [0,91.0]
    PnSKey = [0,92.0]
    try:
        if itemID == 19870042:
            return Overcharge[count]
        elif itemID == 19870043:
            return MiniMultipler[count]
        elif itemID == 19870044:
            return EmployDiscount[count]
        elif itemID == 19870045:
            return BackdoorTrade[count]
        elif itemID == 19870046:
            return CamRadar[count]
        elif itemID == 19870047:
            return Superfan[count]
        elif itemID == 19870048:
            return Headstart[count]
        elif itemID == 19870049:
            return Overstock[count]
        elif itemID == 19870050:
            return Investment[count]
        elif itemID == 19870051:
            return Loan[count]
        elif itemID == 19870057:
            return MangleCart[count]
        elif itemID == 19870058:
            return CupcakeCart[count]
        elif itemID == 19870059:
            return AnimdudeCart[count]
        elif itemID == 19870052:
            return FuzzyDice[count]
        elif itemID == 19870053:
            return PowerAC[count]
        elif itemID == 19870054:
            return BearChange[count]
        elif itemID == 19870055:
            return MaskUpgr[count]
        elif itemID == 19870056:
            return Retina[count]
        elif itemID == 19870060:
            return Spawnkiller[count]
        elif itemID == 19870061:
            return Talbert[count]
        elif itemID == 19870062:
            return Hatchet[count]
        elif itemID == 19870063:
            return PnSKey[count]
    except:
        itemIDCount_to_upgradeID(itemID, count-1)
    
def insertSeedInFrickbears(self):
    frickSeed = self.frickSlotData["options"]["RandomSalvageSeed"]
    frickRngSalvage = self.frickSlotData["options"]["RandomiseSalvages"]
    frickTokenBounty = self.frickSlotData["options"]["SalvageArcadeTokenBounty"]
    frickRecordSave = open(os.path.expandvars(f"{path}/records2-13-25.wario"))
    frickRecordStr = frickRecordSave.read()
    frickRecordSave.close()
    if frickRecordStr.find('"_ArchipelagoSeed":') > -1:
           frickEdit = frickRecordStr.partition('"_ArchipelagoSeed":')
           frickEdit2 = frickEdit[2].partition(',"_Playtime"')
           newFrickSeed = '"_ArchipelagoSeed":' + str(frickSeed)
           frickRecordSave = open(os.path.expandvars(f"{path}/records2-13-25.wario"), "w")
           frickRecordSave.write(frickEdit[0]+newFrickSeed+frickEdit2[1]+frickEdit2[2])
           frickRecordSave.close()
    else:
        logger.error("Save Data for _ArchipelagoSeed not found, cannot set seed")
    frickRecordSave = open(os.path.expandvars(f"{path}/records2-13-25.wario"))
    frickRecordStr = frickRecordSave.read()
    frickRecordSave.close()
    if frickRecordStr.find('"_RandomSalvages":') > -1:
           frickEdit = frickRecordStr.partition('"_RandomSalvages":')
           frickEdit2 = frickEdit[2].partition(',"_UnlockFlags"')
           newFrickSeed = '"_RandomSalvages":' + str(frickRngSalvage)
           frickRecordSave = open(os.path.expandvars(f"{path}/records2-13-25.wario"), "w")
           frickRecordSave.write(frickEdit[0]+newFrickSeed+frickEdit2[1]+frickEdit2[2])
           frickRecordSave.close()
    else:
        logger.error("Save Data for _RandomSalvages not found, cannot set seed")
    frickRecordSave = open(os.path.expandvars(f"{path}/records2-13-25.wario"))
    frickRecordStr = frickRecordSave.read()
    frickRecordSave.close()
    if frickRecordStr.find('"_MoneyPerToken":') > -1:
           frickEdit = frickRecordStr.partition('"_MoneyPerToken":')
           frickEdit2 = frickEdit[2].partition(',"_UnlockedAnimatronics"')
           newFrickSeed = '"_MoneyPerToken":' + str(float(int(frickTokenBounty)/100))
           frickRecordSave = open(os.path.expandvars(f"{path}/records2-13-25.wario"), "w")
           frickRecordSave.write(frickEdit[0]+newFrickSeed+frickEdit2[1]+frickEdit2[2])
           frickRecordSave.close()
    else:
        logger.error("Save Data for _MoneyPerToken not found, cannot set seed")
    frickRecordSave.close()


class Frickbears3ClientCommandProcessor(ClientCommandProcessor):
    def _cmd_resync(self):
        """Manually refreshes the seed in frickbears"""
        pass
      #  insertSeedInFrickbears(self)


class Frickbears3Context(CommonContext):
    command_processor: int = Frickbears3ClientCommandProcessor
    game = "Five Nights at Frickbear's 3"
    items_handling = 0b111  # full remote

    def __init__(self, server_address, password):
        super(Frickbears3Context, self).__init__(server_address, password)
        self.send_index: int = 0
        self.syncing = False
        self.awaiting_bridge = False
        self.frickSlotData = None
        self.allowSending = False
        # self.game_communication_path: files go in this path to pass data between us and the actual game
        if "localappdata" in os.environ:
            self.game_communication_path = os.path.expandvars(r"%localappdata%/Frickbears3/savedata2-13-25.wario")
        else:
            # not windows. game is an exe so let's see if wine might be around to run it
            if "WINEPREFIX" in os.environ:
                wineprefix = os.environ["WINEPREFIX"]
            elif shutil.which("wine") or shutil.which("wine-stable"):
                wineprefix = os.path.expanduser("~/.wine") # default root of wine system data, deep in which is app data
            else:
                msg = "Frickbears3Client couldn't detect system type. Unable to infer required game_communication_path"
                logger.error("Error: " + msg)
                Utils.messagebox("Error", msg, error=True)
                sys.exit(1)
            self.game_communication_path = os.path.join(
                wineprefix,
                "drive_c",
                os.path.expandvars("users/$USER/Local Settings/Application Data/ChecksFinder"))

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(Frickbears3Context, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    async def connection_closed(self):
        await super(Frickbears3Context, self).connection_closed()
        for root, dirs, files in os.walk(self.game_communication_path):
            for file in files:
                if file.find("obtain") <= -1:
                    os.remove(root + "/" + file)

    @property
    def endpoints(self):
        if self.server:
            return [self.server]
        else:
            return []

    async def shutdown(self):
        await super(Frickbears3Context, self).shutdown()
        for root, dirs, files in os.walk(self.game_communication_path):
            for file in files:
                if file.find("obtain") <= -1:
                    os.remove(root+"/"+file)

    def on_package(self, cmd: str, args: dict):
        if cmd in {"Connected"}:
            self.frickSlotData = args["slot_data"]
            self.allowSending = True
            insertSeedInFrickbears(self)
            if not os.path.exists(self.game_communication_path):
                os.makedirs(self.game_communication_path)
            #for ss in self.checked_locations:
            #    filename = f"send{ss}"
            #    with open(os.path.join(self.game_communication_path, filename), 'w') as f:
            #        f.close()
        #if cmd in {"ReceivedItems"}:
        #    start_index = args["index"]
        #    if start_index != len(self.items_received):
        #        for item in args['items']:
        #            filename = f"AP_{str(NetworkItem(*item).location)}PLR{str(NetworkItem(*item).player)}.item"
        #            with open(os.path.join(self.game_communication_path, filename), 'w') as f:
        #                f.write(str(NetworkItem(*item).item))
        #                f.close()

       # if cmd in {"RoomUpdate"}:
          #  if "checked_locations" in args:
           #     for ss in self.checked_locations:
             #       filename = f"send{ss}"
              #      with open(os.path.join(self.game_communication_path, filename), 'w') as f:
              #          f.close()

    def run_gui(self):
        """Import kivy UI system and start running it as self.ui_task."""
        from kvui import GameManager

        class Frickbears3Manager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago Frickbears3 Client"

        self.ui = Frickbears3Manager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")


async def game_watcher(ctx: Frickbears3Context):
    while not ctx.exit_event.is_set():
        if ctx.syncing == True:
            sync_msg = [{'cmd': 'Sync'}]
            if ctx.locations_checked:
                sync_msg.append({"cmd": "LocationChecks", "locations": list(ctx.locations_checked)})
            await ctx.send_msgs(sync_msg)
            ctx.syncing = False
        sending = []
        victory = False
        file1 = open(os.path.expandvars(f"{path}/savedata2-13-25.wario"))
        file = file1.read()
        file1.close()
        if ctx.allowSending:
            if ctx.frickSlotData["options"]["RandomiseSalvages"] == 1:
                if file.find('_Upgrades":') > -1:
                    pt1 = file.partition('_Upgrades":[')
                    pt2 = pt1[2].partition('],"_Deaths"')
                    bought = pt2[0].split(",")
                    for x in bought:
                        if x == '':
                            continue
                        if int(float(x)) >= 93 and int(float(x)) <= 133:
                            sending.append(salvUpgradeID_to_locID(int(float(x))))
            else:
                if file.find('_Salvages":') > -1:
                    pt1 = file.partition('_Salvages":[')
                    pt2 = pt1[2].partition('],"_Masks"')
                    salvaged = pt2[0].split(",")
                    for x in salvaged:
                        if salvageID_to_locID(int(float(x))) != 0:
                            sending.append(salvageID_to_locID(int(float(x))))
            if file.find('_Upgrades":') > -1:
                pt1 = file.partition('_Upgrades":[')
                pt2 = pt1[2].partition('],"_Deaths"')
                bought = pt2[0].split(",")
                for x in bought:
                    if x == '':
                        continue
                    if int(float(x)) >= 42 and int(float(x)) <= 90:
                        sending.append(shopID_to_locID(int(float(x))))
            if file.find('_CanContinue":false') > -1:
                if file.find('Route":0') > -1:
                    sending.append(19875091)
                elif file.find('Route":2') > -1:
                    sending.append(19875092)
                elif file.find('Route":3') > -1:
                    sending.append(19875093)
                elif file.find('Route":1') > -1:
                    sending.append(19875094)
                elif file.find('Route":4') > -1:
                    sending.append(19875095)
        ctx.locations_checked = sending
        message = [{"cmd": 'LocationChecks', "locations": sending}]

        itemArray = []
        itemCountArray = []
        upgrades = []
        for x in ctx.items_received:
            if x[0] >= 19870042 and x[0] <= 19870063:
                if itemArray.count(x[0]) == 0:
                    itemArray.append(x[0])
                    itemCountArray.append(1)
                else:
                    itemCountArray[itemArray.index(x[0])] += 1
            if x[0] == 19870065:
                victory = True
        for x in range(len(itemArray)):
            upgrades.append(itemIDCount_to_upgradeID(itemArray[x],itemCountArray[x]))

        for x in ctx.checked_locations:
            if x >= 19875042 and x <= 19875083:
                upgrades.append(x-19875000)

        file1 = open(os.path.expandvars(f"{path}/savedata2-13-25.wario"))
        saveData = file1.read()
        file1.close()
        saveData1 = saveData.partition('"_Upgrades":[')
        saveData2 = saveData.partition('],"_Deaths"')
        upgradesStr = "["
        for x in range(len(upgrades)):
            if x != 0:
                upgradesStr += ","+str(upgrades[x])
            else:
                upgradesStr += str(upgrades[x])
        newUpgradeData = '"_Upgrades":' + upgradesStr
        if saveData2[2].find('_SaveRecent":true') > -1:
            file1 = open(os.path.expandvars(f"{path}/savedata2-13-25.wario"),"w")
            fuckitweball = saveData2[2].partition('_SaveRecent":true}')
            file1.write(saveData1[0]+newUpgradeData+saveData2[1]+fuckitweball[0]+'_SaveRecent":false}')
            file1.close()

        await ctx.send_msgs(message)
        if not ctx.finished_game and victory:
            await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
            ctx.finished_game = True
        await asyncio.sleep(0.1)


def main():
    async def _main(args):
        ctx = Frickbears3Context(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        progression_watcher = asyncio.create_task(
            game_watcher(ctx), name="Frickbears3ProgressionWatcher")

        await ctx.exit_event.wait()
        ctx.server_address = None

        await progression_watcher

        await ctx.shutdown()

    import colorama

    parser = get_base_parser(description="Frickbears3 Client, for text interfacing.")

    args, rest = parser.parse_known_args()
    colorama.init()
    asyncio.run(_main(args))
    colorama.deinit()

if __name__ == "__main__":
    main()
