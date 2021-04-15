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
    """

    return config.format(FacNameClass=FacNameClass, Author=Author, FacName=FacName, side=FacSide)


def generateMags(Amount, Class):
    mags = ""
    for i in range(Amount):
        mags = mags + '"' + Class + '",'
    mags = mags + '"' + Class + '"'

    return mags


def generateSL(FacSide, FacNameClass, base, uniform, goggles, nvg, vest, headgear, backpack, weapon):
    mags = generateMags(weapon["magazineCount"], weapon["magazine"])
    GLmags = generateMags(weapon["GL_magazineCount"], weapon["GL_magazine"])
    weaponC = weapon["class"]

    config = """
        class {FacNameClass}_f_squadleader : {base} 
        {{
            _generalMacro = "{FacNameClass}_f_squadleader"; 
            scope = 2;
            scopecurator = 2;
            side = {side};
            displayName = "Squad Leader";
            faction = {FacNameClass}_faction; 
            vehicleClass = "{FacNameClass}_Men";
            icon = "iconManLeader";
            nakedUniform = "U_BasicBody";  
            uniformClass = "{uniform}";
            backpack = "{backpack}";
            linkedItems[] = {{"{vest}", "{headgear}", "{nvg}", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio","FirstAidKit","FirstAidKit"}}; 
            respawnLinkedItems[] = {{"{vest}", "{headgear}", "{nvg}", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio","FirstAidKit","FirstAidKit"}};
            weapons[] = {{"{weapon}","Binocular"}};
            respawnweapons[] = {{"{weapon}","Binocular"}};
            magazines[] = {{{mags},{GLmags},"HandGrenade","HandGrenade"}};
            Respawnmagazines[] = {{{mags},{GLmags},"HandGrenade","HandGrenade"}};
        }};
    """

    config = config.format(FacNameClass=FacNameClass, base=base, side=FacSide,
                           uniform=uniform, backpack=backpack, vest=vest, headgear=headgear, nvg=nvg, weapon=weaponC, mags=mags, GLmags=GLmags)

    return config


def generateSoldier(FacSide, FacNameClass, base, uniform, goggles, nvg, vest, headgear, backpack, weapon):
    mags = generateMags(weapon["magazineCount"], weapon["magazine"])
    weaponC = weapon["class"]

    config = """
        class {FacNameClass}_f_soldier : {base} 
        {{
            _generalMacro = "{FacNameClass}_f_soldier"; 
            scope = 2;
            scopecurator = 2;
            side = {side};
            displayName = "Soldier";
            faction = {FacNameClass}_faction; 
            vehicleClass = "{FacNameClass}_Men";
            icon = "iconMan";
            nakedUniform = "U_BasicBody";  
            uniformClass = "{uniform}";
            backpack = "{backpack}";
            linkedItems[] = {{"{vest}", "{headgear}", "{nvg}", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio","FirstAidKit","FirstAidKit"}}; 
            respawnLinkedItems[] = {{"{vest}", "{headgear}", "{nvg}", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio","FirstAidKit","FirstAidKit"}};
            weapons[] = {{"{weapon}","Binocular"}};
            respawnweapons[] = {{"{weapon}","Binocular"}};
            magazines[] = {{{mags},"HandGrenade","HandGrenade"}};
            Respawnmagazines[] = {{{mags},"HandGrenade","HandGrenade"}};
        }};
    """
    config = config.format(FacNameClass=FacNameClass, base=base, side=FacSide,
                           uniform=uniform, backpack=backpack, vest=vest, headgear=headgear, nvg=nvg, weapon=weaponC, mags=mags)

    return config


def generateAT(FacSide, FacNameClass, base, uniform, goggles, nvg, vest, headgear, backpack, weapon, launcher):
    mags = generateMags(weapon["magazineCount"], weapon["magazine"])
    ATmags = generateMags(
        launcher["magazineCount"], launcher["magazine"])
    weaponC = weapon["class"]
    launcherC = launcher["class"]

    config = """
        class {FacNameClass}_f_at : {base} 
        {{
            _generalMacro = "{FacNameClass}_f_mg"; 
            scope = 2;
            scopecurator = 2;
            side = {side};
            displayName = "AT Operator";
            faction = {FacNameClass}_faction; 
            vehicleClass = "{FacNameClass}_Men";
            icon = "iconManAT";
            nakedUniform = "U_BasicBody";  
            uniformClass = "{uniform}";
            backpack = "{backpack}";
            linkedItems[] = {{"{vest}", "{headgear}", "{nvg}", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio","FirstAidKit","FirstAidKit"}}; 
            respawnLinkedItems[] = {{"{vest}", "{headgear}", "{nvg}", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio","FirstAidKit","FirstAidKit"}};
            weapons[] = {{"{weapon}", "{launcher}","Binocular"}};
            respawnweapons[] = {{"{weapon}", "{launcher}","Binocular"}};
            magazines[] = {{{mags},{ATmags},"HandGrenade","HandGrenade"}};
            Respawnmagazines[] = {{{mags}, {ATmags},"HandGrenade","HandGrenade"}};
        }};
    """
    config = config.format(FacNameClass=FacNameClass, base=base, side=FacSide,
                           uniform=uniform, backpack=backpack, vest=vest, headgear=headgear, nvg=nvg, weapon=weaponC, mags=mags, launcher=launcherC, ATmags=ATmags)

    return config


def generateSoldiers(
    FacSide,
    FacNameClass,
    uniform,
    vest,
    backpack,
    med_backpack,
    at_backpack,
    weapon,
    weaponAmmo,
    weaponAmmoCount,
    SL_weapon,
    SL_weaponGLAmmo,
    SL_weaponGLAmmoCount,
    MG_weapon,
    MG_weaponAmmo,
    MG_weaponAmmoCount,
    nvg,
    mask,
    headgear,
    MRK_weapon,
    MRK_weaponAmmo,
    MRK_weaponAmmoCount,
    launcher,
    launcher_Ammo,
    launcher_AmmoCount
):
    MGmags = ""
    for i in range(MG_weaponAmmoCount):
        MGmags = MGmags + '"' + MG_weaponAmmo + '",'
    MGmags = MGmags + '"' + MG_weaponAmmo + '"'

    MRKmags = ""
    for i in range(MRK_weaponAmmoCount):
        MRKmags = MRKmags + '"' + MRK_weaponAmmo + '",'
    MRKmags = MRKmags + '"' + MRK_weaponAmmo + '"'

    finalConfig = ""
    bases = ["O_Soldier_base_F", "B_Soldier_base_F",
             "I_Soldier_base_F", "C_man_1"]
    base = bases[FacSide]

    MG = """
        class {FacNameClass}_f_mg : {base} 
        {{
            _generalMacro = "{FacNameClass}_f_mg"; 
            scope = 2;
            scopecurator = 2;
            side = {side};
            displayName = "Machine Gunner";
            faction = {FacNameClass}_faction; 
            vehicleClass = "{FacNameClass}_Men";
            icon = "iconManMG";
            nakedUniform = "U_BasicBody";  
            uniformClass = "{uniform}";
            backpack = "{backpack}";
            linkedItems[] = {{"{vest}", "{headgear}", "{nvg}", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio","FirstAidKit","FirstAidKit"}}; 
            respawnLinkedItems[] = {{"{vest}", "{headgear}", "{nvg}", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio","FirstAidKit","FirstAidKit"}};
            weapons[] = {{"{MG_weapon}","Binocular"}};
            respawnweapons[] = {{"{MG_weapon}","Binocular"}};
            magazines[] = {{{MGmags},"HandGrenade","HandGrenade"}};
            Respawnmagazines[] = {{{MGmags},"HandGrenade","HandGrenade"}};
        }};
    """
    MG = MG.format(FacNameClass=FacNameClass, base=base, side=FacSide,
                   uniform=uniform, backpack=backpack, vest=vest, headgear=headgear, nvg=nvg, MG_weapon=MG_weapon, MGmags=MGmags)

    MRK = """
        class {FacNameClass}_f_mark : {base} 
        {{
            _generalMacro = "{FacNameClass}_f_mark"; 
            scope = 2;
            scopecurator = 2;
            side = {side};
            displayName = "Marksman";
            faction = {FacNameClass}_faction; 
            vehicleClass = "{FacNameClass}_Men";
            icon = "iconManRecon";
            nakedUniform = "U_BasicBody";  
            uniformClass = "{uniform}";
            backpack = "{backpack}";
            linkedItems[] = {{"{vest}", "{headgear}", "{nvg}", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio","FirstAidKit","FirstAidKit"}}; 
            respawnLinkedItems[] = {{"{vest}", "{headgear}", "{nvg}", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio","FirstAidKit","FirstAidKit"}};
            weapons[] = {{"{MRK_weapon}","Binocular"}};
            respawnweapons[] = {{"{MRK_weapon}","Binocular"}};
            magazines[] = {{"{MRK_weaponAmmo}","HandGrenade","HandGrenade"}};
            Respawnmagazines[] = {{"{MRK_weaponAmmo}","HandGrenade","HandGrenade"}};
        }};
    """
    MRK = MRK.format(FacNameClass=FacNameClass, base=base, side=FacSide,
                     uniform=uniform, backpack=backpack, vest=vest, headgear=headgear, nvg=nvg, MRK_weapon=MRK_weapon, MRK_weaponAmmo=MRK_weaponAmmo)

    Medic = """
        class {FacNameClass}_f_medic : {base} 
        {{
            _generalMacro = "{FacNameClass}_f_medic"; 
            scope = 2;
            scopecurator = 2;
            side = {side};
            displayName = "Medic";
            faction = {FacNameClass}_faction; 
            vehicleClass = "{FacNameClass}_Men";
            icon = "iconMan";
            nakedUniform = "U_BasicBody";  
            uniformClass = "{uniform}";
            backpack = "{backpack}";
            linkedItems[] = {{"{vest}", "{headgear}", "{nvg}", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio","FirstAidKit","FirstAidKit","Medikit"}}; 
            respawnLinkedItems[] = {{"{vest}", "{headgear}", "{nvg}", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio","FirstAidKit","FirstAidKit","Medikit"}};
            weapons[] = {{"{weapon}","Binocular"}};
            respawnweapons[] = {{"{weapon}","Binocular"}};
            magazines[] = {{{mags},"HandGrenade","HandGrenade"}};
            Respawnmagazines[] = {{{mags},"HandGrenade","HandGrenade"}};
        }};
    """
    Medic = Medic.format(FacNameClass=FacNameClass, base=base, side=FacSide,
                         uniform=uniform, backpack=med_backpack, vest=vest, headgear=headgear, nvg=nvg, weapon=weapon, mags=mags)

    finalConfig = finalConfig + SL + Soldier + AT + MG + MRK + Medic
    finalConfig = finalConfig + "};"

    return finalConfig


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

    CFG_SL = generateSL(faction["side"], faction["variable"], base,
                        unit["uniform"], unit["goggles"], unit["nvg"],
                        unit["SL"]["vest"], unit["SL"]["headgear"], unit["SL"]["backpack"], unit["SL"]["weapon"])

    CFG_soldier = generateSoldier(faction["side"], faction["variable"], base,
                                  unit["uniform"], unit["goggles"], unit["nvg"],
                                  unit["soldier"]["vest"], unit["soldier"]["headgear"], unit["soldier"]["backpack"], unit["soldier"]["weapon"])

    CFG_AT = generateAT(faction["side"], faction["variable"], base,
                        unit["uniform"], unit["goggles"], unit["nvg"],
                        unit["AT"]["vest"], unit["AT"]["headgear"], unit["AT"]["backpack"], unit["AT"]["weapon"], unit["AT"]["launcher"])

    # print(CFG_SL)
    # print(CFG_soldier)
    print(CFG_AT)

    # CFG_soldiers = generateSoldiers(faction["side"], faction["variable"],
    #                                 unit["uniform"], unit["vest"], unit["backpack"], unit["med_backpack"], unit["at_backpack"], unit["weapon"]["class"], unit["weapon"]["magazine"], unit["weapon"]["magazineCount"], unit["SL_weapon"]["class"], unit["SL_weapon"]["GL_magazine"], unit["SL_weapon"]["GL_magazineCount"], unit["MG_weapon"]["class"], unit["MG_weapon"]["magazine"], unit["MG_weapon"]["magazineCount"], unit["nvg"], unit["goggles"], unit["headgear"], unit["MRK_weapon"]["class"], unit["MRK_weapon"]["magazine"], unit["MRK_weapon"]["magazineCount"], unit["launcher"]["class"], unit["launcher"]["magazine"], unit["launcher"]["magazineCount"])

    # CFG_groups = generateGroups(
    #     faction["side"], faction["variable"], faction["name"], group["riflemanAmount"], group["MGAmount"], group["ATAmount"], group["MRKAmount"], group["MedAmount"])

    # CFG = CFG_faction + CFG_soldiers + CFG_groups

    # with open("../new/config.cpp", "w") as f:
    #     f.write(CFG)


if __name__ == "__main__":
    main()
