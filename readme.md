# Arma Faction Generator

#### Requires python 3.9.4 or newer and PBO Manager

### Edit config.JSON file, filling the value on right side or leave empty string

## Remember not to remove or add anything beyond quotes on the right side!

### In unit section you can leave empty strings. Then the unit will not receive the specifed item

### After filling json file, open folder with this script, shift+rmb and select open Powershell here. and type:

```
py generator.py
```

### Script will output config.cpp file into faction folder. Pack faction folder into PBO and throw it into @wtf/addons folder. Then add @wtf as a local mod in A3 launcher and run the game.

### JSON file explained:

```
{
    "faction":{
        "name": "test", // here put your faction name
        "variable": "test_var", //this is your custom faction variable, it is up to you
        "side": 0, //side of faction, 0 - OPFOR, 1 - BLU, 2 - IND, 3 - CIV
        "author": "TheWolek" //self explanatory
    },

    "unit": {
        "uniform": "rhs_uniform_mvd_izlom", //class of uniform. Each unit will get this specified uniform
        "goggles": "", //class of googles, as well for each unit
        "nvg": "", //class of NVG, also for everyone
        "SL": { //SquadLeader cfg
            "vest": "V_PlateCarrierL_CTRG", //class of vest, vest can be diffrent for each unit
            "headgear": "H_Cap_headphones", //class of headgear, also can be diffrent
            "backpack": "", // class of backpack, as well it can be diffrent for everyone
            "weapon": { //weapon section
                "class": "arifle_Katiba_GL_F", //class of a rifle (primary weapon)
                "magazine": "30Rnd_65x39_caseless_green", //class of primary weapon mag
                "magazineCount": 1, //number of primary weapon mags. Unit automaticly will receive +1 mag
                "GL_magazine": "1Rnd_HE_Grenade_shell", //class of GL magazine, this option is only available for SL
                "GL_magazineCount": 1 //number of GL magazines. Unit automaticly will receive +1 mag
            }
        },
        "soldier": { //soldier cfg
            "vest": "V_PlateCarrierL_CTRG",
            "headgear": "H_Cap_headphones",
            "backpack": "",
            "weapon": {
                "class": "arifle_Katiba_F",
                "magazine": "30Rnd_65x39_caseless_green",
                "magazineCount": 1
            }
        },
        "AT": { //at cfg
            "vest": "V_PlateCarrierL_CTRG",
            "headgear": "H_Cap_headphones",
            "backpack": "B_Carryall_mcamo",
            "weapon": {
                "class": "arifle_Katiba_F",
                "magazine": "30Rnd_65x39_caseless_green",
                "magazineCount": 1
            },
            "launcher": { //here you can specify what launcher will they have, similar as the weapon section
                "class": "launch_RPG32_F",
                "magazine": "RPG32_F",
                "magazineCount": 1
            }
        },
        "MG": { //mg cfg
            "vest": "V_PlateCarrierL_CTRG",
            "headgear": "H_Cap_headphones",
            "backpack": "B_Carryall_mcamo",
            "weapon": {
                "class": "MMG_01_hex_F",
                "magazine": "150Rnd_93x64_Mag",
                "magazineCount": 1
            }
        },
        "MRK": { //marksman cfg
            "vest": "V_PlateCarrierL_CTRG",
            "headgear": "H_Cap_headphones",
            "backpack": "",
            "weapon": {
                "class": "srifle_GM6_ghex_F",
                "magazine": "5Rnd_127x108_Mag",
                "magazineCount": 1
            }
        },
        "MED": { //medic cfg
            "vest": "V_PlateCarrierL_CTRG",
            "headgear": "H_Cap_headphones",
            "backpack": "B_AssaultPack_mcamo_AT",
            "weapon": {
                "class": "arifle_Katiba_F",
                "magazine": "30Rnd_65x39_caseless_green",
                "magazineCount": 1
            }
        }
    },

    "group": { //this is group section. Here you can specify amount and type of soldiers in group. Group will be always generated with one SL.
        "riflemanAmount": 2,
        "MGAmount": 1,
        "ATAmount": 1,
        "MRKAmount": 1,
        "MedAmount": 1
    }
}
```
