
    class CfgPatches
    {
        class test_var
        {
            units[]= {
                "test_var_f_squadleader",
                "test_var_f_soldier",
                "test_var_f_mg",
                "test_var_f_at",
                "test_var_f_mark",
                "test_var_f_medic"
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
            side = 1;
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
    
        class test_var_f_sqadlleader : B_Soldier_base_F
        {
            _generalMacro = "test_var_f_sqadlleader";
            scope = 2;
            scopecurator = 2;
            side = 1;
            displayName = "Squad Leader";
            faction = test_var_faction;
            vehicleClass = "test_var_Men";
            icon = "iconManLeader";
            nakedUniform = "U_BasicBody";
            uniformClass = "rhs_uniform_mvd_izlom";
            backpack = "";
            linkedItems[] = {"V_PlateCarrierL_CTRG", "H_Cap_headphones", "", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio","FirstAidKit","FirstAidKit"};
            respawnLinkedItems[] = {"V_PlateCarrierL_CTRG", "H_Cap_headphones", "", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio","FirstAidKit","FirstAidKit"};
            weapons[] = {"arifle_Katiba_F_GL","Binocular"};
            respawnweapons[] = {"arifle_Katiba_F_GL","Binocular"};
            magazines[] = {"30Rnd_65x39_caseless_green","30Rnd_65x39_caseless_green","1Rnd_HE_Grenade_shell","1Rnd_HE_Grenade_shell","HandGrenade","HandGrenade"};
            Respawnmagazines[] = {"30Rnd_65x39_caseless_green","30Rnd_65x39_caseless_green","1Rnd_HE_Grenade_shell","1Rnd_HE_Grenade_shell","HandGrenade","HandGrenade"};
        };
    
        class test_var_f_soldier : B_Soldier_base_F
        {
            _generalMacro = "test_var_f_soldier";
            scope = 2;
            scopecurator = 2;
            side = 1;
            displayName = "soldier";
            faction = test_var_faction;
            vehicleClass = "test_var_Men";
            icon = "iconMan";
            nakedUniform = "U_BasicBody";
            uniformClass = "rhs_uniform_mvd_izlom";
            backpack = "";
            linkedItems[] = {"V_PlateCarrierL_CTRG", "H_Cap_headphones", "", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio","FirstAidKit","FirstAidKit"};
            respawnLinkedItems[] = {"V_PlateCarrierL_CTRG", "H_Cap_headphones", "", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio","FirstAidKit","FirstAidKit"};
            weapons[] = {"arifle_Katiba_F","Binocular"};
            respawnweapons[] = {"arifle_Katiba_F","Binocular"};
            magazines[] = {"30Rnd_65x39_caseless_green","30Rnd_65x39_caseless_green","HandGrenade","HandGrenade"};
            Respawnmagazines[] = {"30Rnd_65x39_caseless_green","30Rnd_65x39_caseless_green","HandGrenade","HandGrenade"};
        };
    
        class test_var_f_at : B_Soldier_base_F
        {
            _generalMacro = "test_var_f_at";
            scope = 2;
            scopecurator = 2;
            side = 1;
            displayName = "Rifleman AT";
            faction = test_var_faction;
            vehicleClass = "test_var_Men";
            icon = "iconManAT";
            nakedUniform = "U_BasicBody";
            uniformClass = "rhs_uniform_mvd_izlom";
            backpack = "B_Carryall_mcamo";
            linkedItems[] = {"V_PlateCarrierL_CTRG", "H_Cap_headphones", "", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio","FirstAidKit","FirstAidKit"};
            respawnLinkedItems[] = {"V_PlateCarrierL_CTRG", "H_Cap_headphones", "", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio","FirstAidKit","FirstAidKit"};
            weapons[] = {"arifle_Katiba_F","launch_RPG32_F","Binocular"};
            respawnweapons[] = {"arifle_Katiba_F","launch_RPG32_F","Binocular"};
            magazines[] = {"30Rnd_65x39_caseless_green","30Rnd_65x39_caseless_green","RPG32_F","RPG32_F","HandGrenade","HandGrenade"};
            Respawnmagazines[] = {"30Rnd_65x39_caseless_green","30Rnd_65x39_caseless_green","RPG32_F","RPG32_F","HandGrenade","HandGrenade"};
        };
    
        class test_var_f_mg : B_Soldier_base_F
        {
            _generalMacro = "test_var_f_mg";
            scope = 2;
            scopecurator = 2;
            side = 1;
            displayName = "Machine Gunner";
            faction = test_var_faction;
            vehicleClass = "test_var_Men";
            icon = "iconManMG";
            nakedUniform = "U_BasicBody";
            uniformClass = "rhs_uniform_mvd_izlom";
            backpack = "mg_bag";
            linkedItems[] = {"V_PlateCarrierL_CTRG", "H_Cap_headphones", "", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio","FirstAidKit","FirstAidKit"};
            respawnLinkedItems[] = {"V_PlateCarrierL_CTRG", "H_Cap_headphones", "", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio","FirstAidKit","FirstAidKit"};
            weapons[] = {"MMG_01_hex_F","Binocular"};
            respawnweapons[] = {"MMG_01_hex_F","Binocular"};
            magazines[] = {"150Rnd_93x64_Mag","150Rnd_93x64_Mag","HandGrenade","HandGrenade"};
            Respawnmagazines[] = {"150Rnd_93x64_Mag","150Rnd_93x64_Mag","HandGrenade","HandGrenade"};
        };
    
        class test_var_f_mrk : B_Soldier_base_F
        {
            _generalMacro = "test_var_f_mrk";
            scope = 2;
            scopecurator = 2;
            side = 1;
            displayName = "Marksman";
            faction = test_var_faction;
            vehicleClass = "test_var_Men";
            icon = "iconManRecon";
            nakedUniform = "U_BasicBody";
            uniformClass = "rhs_uniform_mvd_izlom";
            backpack = "";
            linkedItems[] = {"V_PlateCarrierL_CTRG", "H_Cap_headphones", "", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio","FirstAidKit","FirstAidKit"};
            respawnLinkedItems[] = {"V_PlateCarrierL_CTRG", "H_Cap_headphones", "", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio","FirstAidKit","FirstAidKit"};
            weapons[] = {"srifle_GM6_ghex_F","Binocular"};
            respawnweapons[] = {"srifle_GM6_ghex_F","Binocular"};
            magazines[] = {"5Rnd_127x108_Mag","5Rnd_127x108_Mag","HandGrenade","HandGrenade"};
            Respawnmagazines[] = {"5Rnd_127x108_Mag","5Rnd_127x108_Mag","HandGrenade","HandGrenade"};
        };
    
        class test_var_f_medic : B_Soldier_base_F
        {
            _generalMacro = "test_var_f_medic";
            scope = 2;
            scopecurator = 2;
            side = 1;
            displayName = "Medic";
            faction = test_var_faction;
            vehicleClass = "test_var_Men";
            icon = "iconManMedic";
            nakedUniform = "U_BasicBody";
            uniformClass = "rhs_uniform_mvd_izlom";
            backpack = "B_AssaultPack_mcamo_AT";
            linkedItems[] = {"V_PlateCarrierL_CTRG", "H_Cap_headphones", "", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio","FirstAidKit","FirstAidKit", "Medikit"};
            respawnLinkedItems[] = {"V_PlateCarrierL_CTRG", "H_Cap_headphones", "", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio","FirstAidKit","FirstAidKit", "Medikit"};
            weapons[] = {"arifle_Katiba_F","Binocular"};
            respawnweapons[] = {"arifle_Katiba_F","Binocular"};
            magazines[] = {"30Rnd_65x39_caseless_green","30Rnd_65x39_caseless_green","HandGrenade","HandGrenade"};
            Respawnmagazines[] = {"30Rnd_65x39_caseless_green","30Rnd_65x39_caseless_green","HandGrenade","HandGrenade"};
        };
    };
    class CfgGroups
    {
        class WEST
        {
            name = "Custom Group";
            side = 1;
            class test_var {
                name="test";
                class Infantry
                {
                    name="Custom Infantry Groups";
                    class test_var_g_inf
                    {
                        name = "Infantry Squad";
                        side= 1;
                        faction= "test_var";
                        class Unit0
                        {
                            side = 1;
                            vehicle = "test_var_f_Squadleader";
                            rank = "CORPORAL";
                            position[] = { 0, 0, 0 };
                        };
                        
                        class Unit1
                        {
                            side = 1;
                            vehicle = "test_var_f_Soldier";
                            rank = "PRIVATE";
                            position[] = { 5, -5, 0 };
                        };
            
                        class Unit2
                        {
                            side = 1;
                            vehicle = "test_var_f_Soldier";
                            rank = "PRIVATE";
                            position[] = { -5, -5, 0 };
                        };
            
                        class Unit3
                        {
                            side = 1;
                            vehicle = "test_var_f_mg";
                            rank = "PRIVATE";
                            position[] = { 10, -10, 0 };
                        };
            
                        class Unit4
                        {
                            side = 1;
                            vehicle = "test_var_f_at";
                            rank = "PRIVATE";
                            position[] = { -10, -10, 0 };
                        };
            
                        class Unit5
                        {
                            side = 1;
                            vehicle = "test_var_f_mark";
                            rank = "PRIVATE";
                            position[] = { 15, -15, 0 };
                        };
            
                        class Unit6
                        {
                            side = 1;
                            vehicle = "test_var_f_medic";
                            rank = "PRIVATE";
                            position[] = { -15, -15, 0 };
                        };
            
                    };
                };
            };
        };
                        
    };
    