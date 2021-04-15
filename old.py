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


CFG_SL = generateSL(faction["side"], faction["variable"], base,
                    unit["uniform"], unit["goggles"], unit["nvg"],
                    unit["SL"]["vest"], unit["SL"]["headgear"], unit["SL"]["backpack"], unit["SL"]["weapon"])

CFG_soldier = generateSoldier(faction["side"], faction["variable"], base,
                              unit["uniform"], unit["goggles"], unit["nvg"],
                              unit["soldier"]["vest"], unit["soldier"]["headgear"], unit["soldier"]["backpack"], unit["soldier"]["weapon"])

CFG_AT = generateAT(faction["side"], faction["variable"], base,
                    unit["uniform"], unit["goggles"], unit["nvg"],
                    unit["AT"]["vest"], unit["AT"]["headgear"], unit["AT"]["backpack"], unit["AT"]["weapon"], unit["AT"]["launcher"])
