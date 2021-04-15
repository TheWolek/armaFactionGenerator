import json


def generateFaction(FacNameClass, FacName, Author, FacSide):
    config = """
    class CfgPatches
    {{
        class {FacNameClass}
        {{
            units[]= {{
                "{FacNameClass}_f_squadleader",
                "{FacNameClass}_f_soldier",
                "{FacNameClass}_f_mg",
                "{FacNameClass}_f_at",
                "{FacNameClass}_f_mark",
                "{FacNameClass}_f_medic"
            }};
            weapons[]={{}};
            requiredVersion = 0.1;
            requiredAddons[] = {{}};
            author = "{Author}";
        }};
    }};
    class CfgAddons
    {{
        class PreLoadAddons
        {{
            class {FacNameClass}
            {{
                list[] = {{
                    "{FacNameClass}"
                }};
            }};
        }};
    }};
    class cfgFactionClasses
    {{
        class {FacNameClass}_faction
        {{
            displayName = "{FacName}";
            priority = 3;
            side = {side};
            icon = "";
        }};
    }};
    class cfgVehicleClasses
    {{
        class {FacNameClass}_Men
        {{
            displayName = "Men";
        }};
    }};
    class CfgVehicles
    {{
        class O_Soldier_base_F;
        class I_Soldier_base_F;
        class B_Soldier_base_F;
        class C_man_1;
    """

    return config.format(FacNameClass=FacNameClass, Author=Author, FacName=FacName, side=FacSide)


def generateMags(Amount, Class):
    mags = ""
    for i in range(Amount):
        mags = mags + '"' + Class + '",'
    mags = mags + '"' + Class + '"'

    return mags


def generateSoldierCFG(type, Fac, base, unit):
    classNames = {"SL": "_f_sqadlleader", "soldier": "_f_soldier",
                  "AT": "_f_at", "MG": "_f_mg", "MRK": "_f_mrk", "MED": "_f_medic"}
    icons = {"SL": "iconManLeader", "soldier": "iconMan", "AT": "iconManAT",
             "MG": "iconManMG", "MRK": "iconManRecon", "MED": "iconManMedic"}

    displayName = type[1]
    className = classNames[type[0]]
    icon = icons[type[0]]
    FacSide = Fac["side"]
    FacNameClass = Fac["variable"]

    # WEAPONS
    weapons = ''
    weapons = weapons + unit[type[0]]["weapon"]["class"]
    if (type[0] == "AT"):
        weapons = weapons + '",' + '"' + \
            unit[type[0]]["launcher"]["class"]

    # MAGS
    mags = generateMags(
        unit[type[0]]["weapon"]["magazineCount"], unit[type[0]]["weapon"]["magazine"])

    if (type[0] == "AT"):
        mags = mags + "," + generateMags(
            unit[type[0]]["launcher"]["magazineCount"], unit[type[0]]["launcher"]["magazine"])

    if (type[0] == "SL"):
        mags = mags + "," + generateMags(
            unit[type[0]]["weapon"]["GL_magazineCount"], unit[type[0]]["weapon"]["GL_magazine"])

    # ITEMS
    if (type[0] == "MED"):
        items = """{{"{vest}", "{headgear}", "{nvg}", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio","FirstAidKit","FirstAidKit", "Medikit"}}"""
    else:
        items = """{{"{vest}", "{headgear}", "{nvg}", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio","FirstAidKit","FirstAidKit"}}"""

    items = items.format(
        vest=unit[type[0]]["vest"], headgear=unit[type[0]]["headgear"], nvg=unit["nvg"])

    # COMBINE
    config = """
        class {FacNameClass}{className} : {base}
        {{
            _generalMacro = "{FacNameClass}{className}";
            scope = 2;
            scopecurator = 2;
            side = {side};
            displayName = "{displayName}";
            faction = {FacNameClass}_faction;
            vehicleClass = "{FacNameClass}_Men";
            icon = "{icon}";
            nakedUniform = "U_BasicBody";
            uniformClass = "{uniform}";
            backpack = "{backpack}";
            linkedItems[] = {items};
            respawnLinkedItems[] = {items};
            weapons[] = {{"{weapons}","Binocular"}};
            respawnweapons[] = {{"{weapons}","Binocular"}};
            magazines[] = {{{mags},"HandGrenade","HandGrenade"}};
            Respawnmagazines[] = {{{mags},"HandGrenade","HandGrenade"}};
        }};
    """

    config = config.format(FacNameClass=FacNameClass, className=className,
                           base=base, side=FacSide, displayName=displayName, icon=icon, uniform=unit["uniform"], backpack=unit[type[0]]["backpack"], items=items, weapons=weapons, mags=mags)

    return config


def generateGroups(FacSide, FacNameClass, FacName, riflemanAmount, MGAmount, ATAmount, MRKAmount, MedAmount):
    sideName = ""
    restOfUnits = ""
    sides = ["EAST", "WEST", "GUER"]
    sideName = sides[FacSide]

    restOfUnits = generateUnits(
        FacNameClass, FacSide, riflemanAmount, MGAmount, ATAmount, MRKAmount, MedAmount)

    config = """
    class CfgGroups
    {{
        class {sideName}
        {{
            name = "Custom Group";
            side = {side};
            class {FacNameClass} {{
                name="{FacName}";
                class Infantry
                {{
                    name="Custom Infantry Groups";
                    class {FacNameClass}_g_inf
                    {{
                        name = "Infantry Squad";
                        side= {side};
                        faction= "{FacNameClass}";
                        class Unit0
                        {{
                            side = {side};
                            vehicle = "{FacNameClass}_f_Squadleader";
                            rank = "CORPORAL";
                            position[] = {{ 0, 0, 0 }};
                        }};
                        {restOfUnits}
                    }};
                }};
            }};
        }};
                        
    }};
    """

    config = config.format(sideName=sideName, side=FacSide, FacName=FacName,
                           FacNameClass=FacNameClass, restOfUnits=restOfUnits)

    return config


def generateUnits(FacNameClass, FacSide, riflemanAmount, MGAmount, ATAmount, MRKAmount, MedAmount):
    counter = 1
    pos1 = 5
    pos2 = -5
    units = ""
    if riflemanAmount != 0:
        for i in range(riflemanAmount):
            patternRifleman = """
                        class Unit{counter}
                        {{
                            side = {side};
                            vehicle = "{FacNameClass}_f_Soldier";
                            rank = "PRIVATE";
                            position[] = {{ {pos1}, {pos2}, 0 }};
                        }};
            """

            patternRifleman = patternRifleman.format(
                counter=counter, side=FacSide, FacNameClass=FacNameClass, pos1=pos1, pos2=pos2)

            if counter % 2 == 0:
                pos2 = pos2 - 5
                pos1 = pos1 - 5

            counter += 1
            units = units + patternRifleman
            pos1 = pos1 * -1

    if MGAmount != 0:
        for i in range(MGAmount):
            patternMg = """
                        class Unit{counter}
                        {{
                            side = {side};
                            vehicle = "{FacNameClass}_f_mg";
                            rank = "PRIVATE";
                            position[] = {{ {pos1}, {pos2}, 0 }};
                        }};
            """

            patternMg = patternMg.format(
                counter=counter, side=FacSide, FacNameClass=FacNameClass, pos1=pos1, pos2=pos2)

            if counter % 2 == 0:
                pos2 = pos2 - 5
                pos1 = pos1 - 5

            counter += 1
            units = units + patternMg
            pos1 = pos1 * -1

    if ATAmount != 0:
        for i in range(ATAmount):
            patternAT = """
                        class Unit{counter}
                        {{
                            side = {side};
                            vehicle = "{FacNameClass}_f_at";
                            rank = "PRIVATE";
                            position[] = {{ {pos1}, {pos2}, 0 }};
                        }};
            """

            patternAT = patternAT.format(
                counter=counter, side=FacSide, FacNameClass=FacNameClass, pos1=pos1, pos2=pos2)

            if counter % 2 == 0:
                pos2 = pos2 - 5
                pos1 = pos1 - 5

            counter += 1
            units = units + patternAT
            pos1 = pos1 * -1

    if MRKAmount != 0:
        for i in range(MRKAmount):
            patternMRK = """
                        class Unit{counter}
                        {{
                            side = {side};
                            vehicle = "{FacNameClass}_f_mark";
                            rank = "PRIVATE";
                            position[] = {{ {pos1}, {pos2}, 0 }};
                        }};
            """

            patternMRK = patternMRK.format(
                counter=counter, side=FacSide, FacNameClass=FacNameClass, pos1=pos1, pos2=pos2)

            if counter % 2 == 0:
                pos2 = pos2 - 5
                pos1 = pos1 - 5

            counter += 1
            units = units + patternMRK
            pos1 = pos1 * -1

    if MedAmount != 0:
        for i in range(MedAmount):
            patternMed = """
                        class Unit{counter}
                        {{
                            side = {side};
                            vehicle = "{FacNameClass}_f_medic";
                            rank = "PRIVATE";
                            position[] = {{ {pos1}, {pos2}, 0 }};
                        }};
            """

            patternMed = patternMed.format(
                counter=counter, side=FacSide, FacNameClass=FacNameClass, pos1=pos1, pos2=pos2)

            if counter % 2 == 0:
                pos2 = pos2 - 5
                pos1 = pos1 - 5

            counter += 1
            units = units + patternMed
            pos1 = pos1 * -1

    return units


def main():

    with open("config.json", "r") as f:
        data = json.load(f)

    faction = data["faction"]
    unit = data["unit"]
    group = data["group"]
    bases = ["O_Soldier_base_F", "B_Soldier_base_F",
             "I_Soldier_base_F", "C_man_1"]
    base = bases[faction["side"]]

    CFG_faction = generateFaction(
        faction["variable"], faction["name"], faction["author"], faction["side"])

    CFG_SL = generateSoldierCFG(
        ["SL", "Squad Leader"], faction, base, unit)

    CFG_soldier = generateSoldierCFG(
        ["soldier", "soldier"], faction, base, unit)

    CFG_AT = generateSoldierCFG(
        ["AT", "Rifleman AT"], faction, base, unit)

    CFG_MG = generateSoldierCFG(
        ["MG", "Machine Gunner"], faction, base, unit)

    CFG_MRK = generateSoldierCFG(
        ["MRK", "Marksman"], faction, base, unit)

    CFG_MED = generateSoldierCFG(
        ["MED", "Medic"], faction, base, unit)

    CFG_groups = generateGroups(
        faction["side"], faction["variable"], faction["name"], group["riflemanAmount"], group["MGAmount"], group["ATAmount"], group["MRKAmount"], group["MedAmount"])

    CFG_final = CFG_faction + CFG_SL + CFG_soldier + \
        CFG_AT + CFG_MG + CFG_MRK + CFG_MED + "};" + CFG_groups

    # print(CFG_final)

    with open("faction/config.cpp", "w") as f:
        f.write(CFG_final)


if __name__ == "__main__":
    main()
