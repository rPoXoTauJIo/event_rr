# config file

# address and port for listening UDP server
SERVERHOST = 'localhost'  # Symbolic name meaning all available interfaces
SERVERPORT = 8888  # Arbitrary non-privileged port

# address and port for streaming client
CLIENTHOST = 'localhost'  # Symbolic name meaning all available interfaces
CLIENTPORT = 8888  # Arbitrary non-privileged port

DEBUGS_DEFAULT = [
    'file', # debugging in files, set log path first
    #'udp', # UDP debug, sending
    'echo',  # printing debug to server console
    #'ingame' # printing debug ingame
]

# specify on which levels event script will run
MAP_EVENT = [
    ('ramiel', 'gpm_cq', 64), # pure for testing
    ('ramiel', 'gpm_cq', 128),
    ('bamyan', 'gpm_cq', 32),
    ]

MAP_HIDEOUTS = {
    'ramiel' : {
        'gpm_cq' : {
            128 : [
                {
                    'name' : 'hideout_1',
                    'template' : 'fixed_insurgent_hideout',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (-50.832, 25.534, -229.769),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'hideout_2',
                    'template' : 'fixed_insurgent_hideout',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (-29.079, 26.506, -124.421),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'hideout_3',
                    'template' : 'fixed_insurgent_hideout',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (-34.382, 26.785, 12.429),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'hideout_4',
                    'template' : 'fixed_insurgent_hideout',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (77.795, 26.396, 115.703),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'hideout_5',
                    'template' : 'fixed_insurgent_hideout',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (-49.041, 26.498, 178.053),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'hideout_6',
                    'template' : 'fixed_insurgent_hideout',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (73.241, 27.601, 236.625),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'hideout_7',
                    'template' : 'fixed_insurgent_hideout',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : ( 54.153, 28.422, 301.003),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'hideout_8',
                    'template' : 'fixed_insurgent_hideout',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (111.085, 27.080, 358.286),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'hideout_9',
                    'template' : 'fixed_insurgent_hideout',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (17.354, 27.177, 429.175),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'hideout_10',
                    'template' : 'fixed_insurgent_hideout',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (57.655, 25.000, 508.932),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                ]
            }
        }
    }

MAP_OBJECTIVES = {
    'ramiel' : {
        'gpm_cq' : {
            128 : [
                {
                    'name' : 'ammocache_1',
                    'template' : 'ammocache',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (-41.895, 25.1362, -238.107),
                    'rotation' : (0.000, 0.000, 0.000)
                    }, 
                {
                    'name' : 'ammocache_2',
                    'template' : 'ammocache',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (37.1265, 25.1362, 56.8647),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'ammocache_3',
                    'template' : 'ammocache',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (59.3651, 27.931, 306.934),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'ammocache_4',
                    'template' : 'ammocache',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (67.3558, 25.1935, 525.785),
                    'rotation' : (0.000, 0.000, 0.000)
                    }, 
                ]
            }
        }
    }

MAP_SPAWNERS = {
    'ramiel' : {
        'gpm_cq': {
            128 :[
                # US default spawns
                {
                    'name' : 'us_main_jeep1',
                    'template' : 'us_jep_hmmwv',
                    'team' : 2,
                    'delay' : 20,
                    'position' : (-692.033, 24.922, -663.341),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'us_main_jeep2',
                    'template' : 'us_jep_hmmwv',
                    'team' : 2,
                    'delay' : 30,
                    'position' : (-681.662, 24.922, -663.341),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'us_main_jeep3',
                    'template' : 'us_jep_hmmwv_mk19',
                    'team' : 2,
                    'delay' : 30,
                    'position' : (-687.256, 24.922, -663.341),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'us_main_jeep4',
                    'template' : 'us_jep_hmmwv',
                    'team' : 2,
                    'delay' : 30,
                    'position' : (-697.435, 24.922, -663.341),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'us_main_jeep5',
                    'template' : 'us_jep_hmmwv',
                    'team' : 2,
                    'delay' : 30,
                    'position' : (-702.703, 24.922, -663.341),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'us_main_jeep6',
                    'template' : 'us_jep_hmmwv',
                    'team' : 2,
                    'delay' : 60,
                    'position' : (-692.033, 24.922, -653.341),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'us_main_jeep7',
                    'template' : 'us_jep_hmmwv',
                    'team' : 2,
                    'delay' : 60,
                    'position' : (-681.662, 24.922, -653.341),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'us_main_jeep8',
                    'template' : 'us_jep_hmmwv',
                    'team' : 2,
                    'delay' : 60,
                    'position' : (-687.256, 24.922, -653.341),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'us_main_jeep9',
                    'template' : 'us_jep_hmmwv',
                    'team' : 2,
                    'delay' : 60,
                    'position' : (-697.435, 24.922, -653.341),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'us_main_jeep10',
                    'template' : 'us_jep_hmmwv',
                    'team' : 2,
                    'delay' : 60,
                    'position' : (-702.703, 24.922, -653.341),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                # ARF default spawns
                {
                    'name' : 'arf_main_atm1',
                    'template' : 'civ_atm_technical',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (40.809, 26, 523.824),
                    'rotation' : (180.000, 0.000, 0.000)
                    },
                {
                    'name' : 'arf_main_atm2',
                    'template' : 'civ_atm_technical',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (46.8542, 26, 523.824),
                    'rotation' : (180.000, 0.000, 0.000)
                    },
                {
                    'name' : 'arf_main_uralzu23_1',
                    'template' : 'civ_aav_uralzu232',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (97.3817, 26, 513.75),
                    'rotation' : (180.000, 0.000, 0.000)
                    },
                {
                    'name' : 'arf_main_uralzu23_2',
                    'template' : 'civ_aav_uralzu232',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (92.2107, 26, 513.75),
                    'rotation' : (180.000, 0.000, 0.000)
                    },
                {
                    'name' : 'arf_main_ammocar1',
                    'template' : 'civ_jep_techincal_support',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (70.0343, 26, 511.307),
                    'rotation' : (180.000, 0.000, 0.000)
                    },
                {
                    'name' : 'arf_main_ammocar2',
                    'template' : 'civ_jep_techincal_support',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (75.0343, 26, 511.307),
                    'rotation' : (180.000, 0.000, 0.000)
                    },
                {
                    'name' : 'arf_main_techincal1',
                    'template' : 'civ_jep_techincal',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (45.0723, 26, 477.975),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'arf_main_techincal2',
                    'template' : 'civ_jep_techincal',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (45.0723, 26, 473.567),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'arf_main_techincal3',
                    'template' : 'civ_jep_techincal',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (100, 26, 477.975),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'arf_main_techincal4',
                    'template' : 'civ_jep_techincal',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (100, 26, 473.567),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                ]
            }
        },
    'bamyan' : {
        'gpm_cq' : {
            32 :[
                # USMC spawners
                {
                    'name' : 'USA_OS_main_VehicleSpwn_1',
                    'template' : 'us_jep_hmmwv_uparmored',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (1288.271, 47.992, 1161.503),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'USA_OS_main_Humvee2',
                    'template' : 'us_jep_hmmwv_uparmored',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (1229.208, 47.070, 1153.982),
                    'rotation' : (-47.693, 0.000, 0.000)
                    },
                {
                    'name' : 'USA_OS_main_sply1',
                    'template' : 'fixed_supply_crate_us',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (1219.495, 47.893, 1116.552),
                    'rotation' : (39.119, 0.000, 0.000)
                    },
                {
                    'name' : 'USA_OS_main_sply2',
                    'template' : 'fixed_supply_crate_us',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (1235.473, 46.921, 1157.266),
                    'rotation' : (44.181, 0.000, 0.000)
                    },
                {
                    'name' : 'USA_OS_main_sply3',
                    'template' : 'fixed_supply_crate_us',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (1246.846, 46.921, 1175.195),
                    'rotation' : (-49.069, 0.000, 0.000)
                    },
                {
                    'name' : 'USA_OS_main_sply4',
                    'template' : 'fixed_supply_crate_us',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (1274.395, 49.997, 1205.436),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'USA_OS_main_sply5',
                    'template' : 'fixed_supply_crate_us',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (1275.315, 46.921, 1126.203),
                    'rotation' : (31.146, 0.000, 0.000)
                    },
                {
                    'name' : 'USA_OS_main_sply6',
                    'template' : 'fixed_supply_crate_us',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (1298.900, 46.921, 1116.142),
                    'rotation' : (96.634, 0.000, 0.000)
                    },
                {
                    'name' : 'USA_OS_main_sply7',
                    'template' : 'fixed_supply_crate_us',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (1298.371, 46.985, 1137.345),
                    'rotation' : (-167.539, 0.000, 0.000)
                    },
                {
                    'name' : 'USA_OS_main_sply8',
                    'template' : 'fixed_supply_crate_us',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (1216.540, 47.893, 1099.515),
                    'rotation' : (37.470, 0.000, 0.000)
                    },
                {
                    'name' : 'USA_OS_main_FOB',
                    'template' : 'fixed_firebase',
                    'team' : 2,
                    'delay' : 60,
                    'position' : (1243.722, 47.196, 1144.192),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'USA_OS_main_LogiTruckUSA',
                    'template' : 'us_trk_logistics',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (1223.100, 47.893, 1134.893),
                    'rotation' : (-138.616, 0.000, 0.000)
                    },
                # Taliban spawners
                {
                    'name' : 'Taliban_OS_3_sply2',
                    'template' : 'fixed_supply_crate_tal',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (1826.507, 84.441, 448.439),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_OS_1_Vehicle_technical',
                    'template' : 'civ_jep_technical_black',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (593.042, 36.309, 1277.786),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_OS_3_sply_3',
                    'template' : 'fixed_supply_crate_tal',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (1830.948, 82.162, 487.835),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_Vehicle_Zastava_1',
                    'template' : 'civ_jep_zastava900ak',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (601.908, 35.227, 1298.468),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_Vehicle_VBIED',
                    'template' : 'civ_trk_dumpster_bomber',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (586.171, 39.99, 1235.035),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_CP2_Vehicle_Zastava2',
                    'template' : 'civ_jep_zastava900ak',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (1626.689, 33.777, 1838.27),
                    'rotation' : (171.566, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_CP3_Vehicle_Zastava2',
                    'template' : 'civ_jep_zastava900ak',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (1836.855, 84.908, 437.604),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_OS_1_technical_ammo',
                    'template' : 'civ_jep_support',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (581.798, 36.683, 1275.51),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_OS_1_sply_1',
                    'template' : 'fixed_supply_crate_tal',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (582.681, 34.863, 1312.098),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_CP3_Vehicle_Zastava1',
                    'template' : 'civ_jep_zastava900ak',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (1836.605, 84.075, 457.102),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_Vehicle_Zastava_2',
                    'template' : 'civ_jep_zastava900ak',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (580.358, 34.993, 1297.46),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_OS_3_technical_ammo',
                    'template' : 'civ_jep_support',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (1837.315, 84.451, 448.946),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_OS_2_technical_ammo',
                    'template' : 'civ_jep_support',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (1636.724, 33.204, 1844.477),
                    'rotation' : (-174.61, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_CP3_Vehicle_DSHKm',
                    'template' : 'civ_jep_zastava900ak',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (1824.927, 83.943, 457.796),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_CP2_Vehicle_Zastava',
                    'template' : 'civ_jep_zastava900ak',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (1642.06, 35.295, 1826.208),
                    'rotation' : (-174.772, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_CP3_Vehicle_VBIED',
                    'template' : 'civ_trk_dumpster_bomber',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (1826.948, 86.6, 398.444),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_CP2_Vehicle_DSHKm',
                    'template' : 'civ_jep_zastava900ak',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (1630.216, 35.06, 1823.614),
                    'rotation' : (-178.794, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_OS_2_sply_2',
                    'template' : 'fixed_supply_crate_tal',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (1643.892, 37.482, 1806.833),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                ]
            }
        }
    }

MAP_FLAGS = {
    'ramiel' : {
        'gpm_cq' : {
            64 : {
                'cpname_ramiel_aas64_habr_gidr_hq' : (67.3558, 20.0, 525.785)
                }
            },
            128 : {
                'cpname_ramiel_aas128_habr_gidr_hq' : (67.3558, 20.0, 525.785)
            }
        }
    }

MAP_DODS = {
    'bamyan' : {
        'gpm_cq' : {
            32 : {
                'CombatArea_0_AAS32' : {
                    'name' : 'CombatArea_0_AAS32',
                    'create' : False,
                    'team' : 1, # we're changing to team 1
                    #'vehicles' : 4,
                    #'layer' : 4,
                    #'inverted' : 0,
                    #'areapoints' : [
                    #    (2048.000000, -2048.000000),
                    #    (2048.000000, 2048.000000),
                    #    (-2048.000000, 2048.000000),
                    #    (-2048.000000, -2048.000000)
                    #    ]
                    },
                'CombatArea_12_aas_32' : {
                    'name' : 'CombatArea_12_aas_32',
                    'create' : True,
                    'team' : 2,
                    'vehicles' : 4,
                    'layer' : 4,
                    'inverted' : 0,
                    'areapoints' : [
						(1174.676025, 1103.674561),
						(1232.380371, 1055.284668),
						(1245.156982, 1051.126221),
						(1254.905762, 1055.237061),
						(1280.414307, 1087.708496),
						(1294.782227, 1094.130371),
						(1308.346680, 1097.046143),
						(1326.570557, 1107.518555),
						(1337.739502, 1116.192383),
						(1341.638428, 1125.409668),
						(1340.869141, 1133.777832),
						(1339.842041, 1136.473633),
						(1317.634033, 1140.716309),
						(1309.857666, 1161.430176),
						(1296.853271, 1183.943115),
						(1291.420410, 1195.915039),
						(1287.397461, 1205.823730),
						(1281.621094, 1215.468506),
						(1270.386719, 1223.174072),
						(1262.915039, 1222.955811),
						(1249.763184, 1219.809814),
						(1233.890137, 1207.767090),
						(1217.339111, 1189.089355),
						(1211.392822, 1181.513672),
						(1207.733154, 1172.983398),
						(1207.270264, 1159.205566),
						(1179.900635, 1123.102295),
						(1174.063232, 1113.879150),
						(1172.645752, 1109.778809),
						(1172.853760, 1106.407959)
                        ]
                    },
                }
            },
        },
    'ramiel' : {
        'gpm_cq' : {
            128 : {
                'CombatArea_34_Event' : {
                    'name' : 'CombatArea_34_Event',
                    'create' : True,
                    'delete' : False,
                    'modify' : False,
                    'team' : 0,
                    'vehicles' : 4,
                    'layer' : 7,
                    'inverted' : 1, #lets see if we can create new one and invert
                    'areapoints' : [
						(34.882935, 544.660278),
                        (35.332764, 453.216187),
                        (18.687012, 456.151489),
                        (-28.119202, 451.193970),
                        (-31.826843, 383.825928),
                        (17.530273, 382.863647),
                        (17.275757, 343.808228),
                        (24.046509, 338.153809),
                        (22.211426, 316.923096),
                        (19.974731, 291.593262),
                        (-9.523865, 282.461792),
                        (-12.859497, 269.752075),
                        (-13.214111, 262.709961),
                        (-23.508057, 266.501709),
                        (-45.032043, 266.164429),
                        (-61.888916, 264.117432),
                        (-79.115295, 249.624390),
                        (-80.543335, 210.545776),
                        (-79.924377, 193.372559),
                        (-78.761169, 147.066895),
                        (-78.908691, 138.471069),
                        (-78.635986, 124.714966),
                        (-76.637878, 117.230347),
                        (-77.139587, 90.135986),
                        (-81.011780, 69.380005),
                        (-79.099670, 56.914307),
                        (-76.063293, 40.007813),
                        (-76.642456, 20.578857),
                        (-77.830627, 12.644653),
                        (-78.071472, -6.945129),
                        (-80.109680, -10.857117),
                        (-80.291748, -24.611023),
                        (-84.798645, -25.608459),
                        (-84.669861, -58.406067),
                        (-83.170715, -73.385864),
                        (-82.037659, -81.527405),
                        (-83.235901, -100.327209),
                        (-83.184143, -112.795044),
                        (-83.239319, -126.640930),
                        (-80.918823, -140.186768),
                        (-82.258606, -152.771179),
                        (-120.398743, -223.470032),
                        (-122.950806, -232.507324),
                        (-119.833313, -271.236755),
                        (-113.066833, -283.420532),
                        (-118.267212, -298.421326),
                        (-139.362610, -356.073364),
                        (-147.779053, -374.572083),
                        (-172.486755, -361.881592),
                        (-219.846924, -398.428650),
                        (-283.511169, -434.853577),
                        (-338.783264, -459.645264),
                        (-423.378601, -484.498230),
                        (-481.368713, -472.033508),
                        (-516.859192, -480.081482),
                        (-542.060547, -471.701904),
                        (-572.983032, -479.681091),
                        (-643.077148, -489.544861),
                        (-687.249207, -508.761414),
                        (-689.490784, -526.941833),
                        (-671.382935, -555.005066),
                        (-672.173950, -569.781677),
                        (-805.157349, -571.981812),
                        (-805.494141, -644.534241),
                        (-733.431519, -643.389038),
                        (-733.007690, -715.599731),
                        (-1024.000000, -1024.000000),
                        (-1024.000000, 1024.000000),
                        (1024.000000, 1024.000000),
                        (1024.000000, -1024.000000),
                        (-535.610229, -715.199585),
                        (-534.810120, -662.343506),
                        (-525.507446, -661.516724),
                        (-526.182983, -572.360962),
                        (-634.846497, -571.432007),
                        (-635.646484, -555.128906),
                        (-590.456787, -551.162476),
                        (-411.488892, -544.998474),
                        (-291.008118, -513.988098),
                        (-253.176514, -495.932129),
                        (-235.315002, -480.948120),
                        (-221.276062, -487.105957),
                        (-185.687744, -452.994812),
                        (-166.397766, -433.684937),
                        (-137.925659, -428.002319),
                        (-117.697693, -451.603394),
                        (-19.771057, -399.646973),
                        (28.099731, -333.262634),
                        (29.957275, -309.679749),
                        (9.010376, -270.004700),
                        (44.761353, -129.158081),
                        (78.275146, -52.068970),
                        (78.388672, -6.393555),
                        (89.049194, 32.277466),
                        (155.811890, 32.009277),
                        (155.950073, 88.015015),
                        (139.119751, 100.903564),
                        (142.012939, 163.262329),
                        (138.153320, 173.247437),
                        (137.134155, 191.233398),
                        (118.245361, 215.466797),
                        (120.208862, 251.442383),
                        (124.784668, 308.319702),
                        (124.401367, 387.239380),
                        (138.225830, 386.781494),
                        (140.851929, 399.506592),
                        (141.566162, 417.996582),
                        (140.630005, 444.560181),
                        (106.121582, 457.259155),
                        (106.303955, 544.588135),
                        ]
                    },
                'CombatArea_36_Preparation' : {
                    'name' : 'CombatArea_36_Preparation',
                    'create' : False,
                    'modify' : False,
                    'delete' : False,
                    'team' : 0,
                    'vehicles' : 4,
                    'layer' : 7,
                    'inverted' : 1,
                    'areapoints' : [
                        (-180.868530, -357.887512),
                        (-131.831909, -383.654602),
                        (-41.863281, -318.514587),
                        (21.301880, -301.445618),
                        (29.133423, -357.279785),
                        (-82.844788, -511.182434),
                        (-604.347839, -565.059082),
                        (-685.952881, -539.255249),
                        (-697.035034, -514.880920),
                        (-678.240356, -452.514038),
                        ]
                    },
                }
            },
        },
    }















