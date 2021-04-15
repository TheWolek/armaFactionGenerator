
    class CfgPatches
    {
        class test_var
        {
            units[]= {
                "test_var_f_Squadleader",
                "test_var_f_Soldier",
                "test_var_f_mg",
                "test_var_f_at",
                "test_var_f_mark"
            };
            weapons[]={};
            requiredVersion = 0.1;
            requiredAddons[] = {};
            author = "TheWolek";
        };
    };
    class CfgAddons
    {
        class PreLoadAddons
        {
            class test_var
            {
                list[] = {
                    "test_var"
                };
            };
        };
    };    
    class cfgFactionClasses
    {
        class test_var_faction
        {
            displayName = "test";
            priority = 3;
            side = 0;
            icon = "";
        };
    };
    class cfgVehicleClasses
    {
        class test_var_Men
        {
            displayName = "Men";
        };
    };
    
    class CfgVehicles
    {
        class O_Soldier_base_F;
        class I_Soldier_base_F;
        class B_Soldier_base_F;
        class C_man_1;

        class test_var_f_Squadleader : C_man_1 
        {
            _generalMacro = "test_var_f_Squadleader"; 
            scope = 2;
            scopecurator = 2;
            side = 0;
            displayName = "Squad Leader";
            faction = test_var_faction; 
            vehicleClass = "test_var_Men";
            icon = "iconManLeader";
            nakedUniform = "U_BasicBody";  
            modelSides[] = {0,1,2};
            uniformClass = "TRYK_U_pad_hood_Blk";
            backpack = "";
            linkedItems[] = {"V_PlateCarrierL_CTRG", "H_Cap_headphones", "", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio"}; 
            respawnLinkedItems[] = {"V_PlateCarrierL_CTRG", "H_Cap_headphones", "", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio"};
            weapons[] = {"arifle_Katiba_F","Binocular"};
            respawnweapons[] = {"arifle_Katiba_F","Binocular"};
            magazines[] = {"30Rnd_65x39_caseless_green","30Rnd_65x39_caseless_green","HandGrenade","HandGrenade",};
            Respawnmagazines[] = {"30Rnd_65x39_caseless_green","30Rnd_65x39_caseless_green","HandGrenade","HandGrenade",};
        };
    
        class test_var_f_Soldier : C_man_1 
        {
            _generalMacro = "test_var_f_Soldier"; 
            scope = 2;
            scopecurator = 2;
            side = 0;
            displayName = "Soldier";
            faction = test_var_faction; 
            vehicleClass = "test_var_Men";
            icon = "iconMan";
            nakedUniform = "U_BasicBody";  
            uniformClass = "TRYK_U_pad_hood_Blk";
            backpack = "";
            linkedItems[] = {"V_PlateCarrierL_CTRG", "H_Cap_headphones", "", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio"}; 
            respawnLinkedItems[] = {"V_PlateCarrierL_CTRG", "H_Cap_headphones", "", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio"};
            weapons[] = {"arifle_Katiba_F","Binocular"};
            respawnweapons[] = {"arifle_Katiba_F","Binocular"};
            magazines[] = {"30Rnd_65x39_caseless_green","30Rnd_65x39_caseless_green","HandGrenade","HandGrenade",};
            Respawnmagazines[] = {"30Rnd_65x39_caseless_green","30Rnd_65x39_caseless_green","HandGrenade","HandGrenade",};
        };
    
        class test_var_f_at : C_man_1 
        {
            _generalMacro = "test_var_f_mg"; 
            scope = 2;
            scopecurator = 2;
            side = 0;
            displayName = "AT Operator";
            faction = test_var_faction; 
            vehicleClass = "test_var_Men";
            icon = "iconManAT";
            nakedUniform = "U_BasicBody";  
            uniformClass = "TRYK_U_pad_hood_Blk";
            backpack = "";
            linkedItems[] = {"V_PlateCarrierL_CTRG", "H_Cap_headphones", "", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio"}; 
            respawnLinkedItems[] = {"V_PlateCarrierL_CTRG", "H_Cap_headphones", "", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio"};
            weapons[] = {"arifle_Katiba_F", "launch_RPG32_F","Binocular"};
            respawnweapons[] = {"arifle_Katiba_F", "launch_RPG32_F","Binocular"};
            magazines[] = {"30Rnd_65x39_caseless_green","30Rnd_65x39_caseless_green","RPG32_F","RPG32_F","HandGrenade","HandGrenade",};
            Respawnmagazines[] = {"30Rnd_65x39_caseless_green","30Rnd_65x39_caseless_green", "RPG32_F","RPG32_F","HandGrenade","HandGrenade",};
        };
    
        class test_var_f_mg : C_man_1 
        {
            _generalMacro = "test_var_f_mg"; 
            scope = 2;
            scopecurator = 2;
            side = 0;
            displayName = "Machine Gunner";
            faction = test_var_faction; 
            vehicleClass = "test_var_Men";
            icon = "iconManMG";
            nakedUniform = "U_BasicBody";  
            uniformClass = "TRYK_U_pad_hood_Blk";
            backpack = "";
            linkedItems[] = {"V_PlateCarrierL_CTRG", "H_Cap_headphones", "", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio"}; 
            respawnLinkedItems[] = {"V_PlateCarrierL_CTRG", "H_Cap_headphones", "", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio"};
            weapons[] = {"MMG_01_hex_F","Binocular"};
            respawnweapons[] = {"MMG_01_hex_F","Binocular"};
            magazines[] = {"150Rnd_93x64_Mag","150Rnd_93x64_Mag","HandGrenade","HandGrenade",};
            Respawnmagazines[] = {"150Rnd_93x64_Mag","150Rnd_93x64_Mag","HandGrenade","HandGrenade",};
        };
    
        class test_var_f_mark : C_man_1 
        {
            _generalMacro = "test_var_f_mark"; 
            scope = 2;
            scopecurator = 2;
            side = 0;
            displayName = "Marksman";
            faction = test_var_faction; 
            vehicleClass = "test_var_Men";
            icon = "iconManRecon";
            nakedUniform = "U_BasicBody";  
            uniformClass = "TRYK_U_pad_hood_Blk";
            backpack = "";
            linkedItems[] = {"V_PlateCarrierL_CTRG", "H_Cap_headphones", "", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio"}; 
            respawnLinkedItems[] = {"V_PlateCarrierL_CTRG", "H_Cap_headphones", "", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio"};
            weapons[] = {"srifle_GM6_ghex_F","Binocular"};
            respawnweapons[] = {"srifle_GM6_ghex_F","Binocular"};
            magazines[] = {"5Rnd_127x108_Mag","HandGrenade","HandGrenade",};
            Respawnmagazines[] = {"5Rnd_127x108_Mag","HandGrenade","HandGrenade",};
        };
    };
    class CfgGroups
    {
        class EAST
        {
            name = "Custom Group";
            side = 0;
            class test_var {
                name="test";
                class Infantry
                {
                    name="Custom Infantry Groups";
                    class test_var_g_inf
                    {
                        name = "Infantry Squad";
                        side= 0;
                        faction= "test_var";
                        class Unit0
                        {
                            side = 0;
                            vehicle = "test_var_f_Squadleader";
                            rank = "CORPORAL";
                            position[] = { 0, 0, 0 };
                        };
                        
                        class Unit1
                        {
                            side = 0;
                            vehicle = "test_var_f_Soldier";
                            rank = "PRIVATE";
                            position[] = { 5, -5, 0 };
                        };
            
                        class Unit2
                        {
                            side = 0;
                            vehicle = "test_var_f_Soldier";
                            rank = "PRIVATE";
                            position[] = { -5, -5, 0 };
                        };
            
                        class Unit3
                        {
                            side = 0;
                            vehicle = "test_var_f_mg";
                            rank = "PRIVATE";
                            position[] = { 10, -10, 0 };
                        };
            
                        class Unit4
                        {
                            side = 0;
                            vehicle = "test_var_f_at";
                            rank = "PRIVATE";
                            position[] = { -10, -10, 0 };
                        };
            
                        class Unit5
                        {
                            side = 0;
                            vehicle = "test_var_f_mark";
                            rank = "PRIVATE";
                            position[] = { 15, -15, 0 };
                        };
            
                    };
                };
            };
        };
                        
    };
    