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
    #('ramiel', 'gpm_cq', 64), # pure for testing
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

'''
MAP_SPAWNPOINTS = { # not working, spawns aren't networkable
    'bamyan' : {
        'gpm_cq' : {
            32 :[
                {
                    'name' : 'cpname_bamyan_aas32_opformain_2_0',
                    'delete' : True,
                    'cpid' : 310,
                    'team' : 1,
                    'position' : (-1871.244, 1.024, 1937.06),
                    'rotation' : (-173.301, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_usmain_1_0',
                    'delete' : True,
                    'cpid' : 301,
                    'team' : 1,
                    'position' : (-1207.865, 93.981, -1999.086),
                    'rotation' : (-77.274, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_1_0',
                    'delete' : True,
                    'cpid' : 310,
                    'team' : 1,
                    'position' : (-1904.734, 1.024, 1914.375),
                    'rotation' : (89.952, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_3_0',
                    'delete' : True,
                    'cpid' : 310,
                    'team' : 1,
                    'position' : (-1898.508, 1.024, 1945.381),
                    'rotation' : (-174.618, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_usmain_2_0',
                    'delete' : True,
                    'cpid' : 301,
                    'team' : 1,
                    'position' : (-1208.548, 93.981, -2016.996),
                    'rotation' : (-86.379, 0.0, 0.0)
                    },
                
                ]
            }
        }
    }
'''

MAP_SPAWNERS = {
    'ramiel' : {
        'gpm_cq': {
            128 :[
                # US default spawns
                {
                    'name' : 'cpname_ramiel_aas128_usmain_hmmwv_0',
                    'delete' : False,
                    'template' : 'us_jep_hmmwv',
                    'team' : 2,
                    'delay' : 600,
                    'position' : (-640.291, 26.000, -654.993),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_usmain_hmmwv_1',
                    'delete' : False,
                    'template' : 'us_jep_hmmwv',
                    'team' : 2,
                    'delay' : 600,
                    'position' : (-640.339, 26.000, -648.535),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_usmain_hmmwv_2',
                    'delete' : False,
                    'template' : 'us_jep_hmmwv_mk19',
                    'team' : 2,
                    'delay' : 600,
                    'position' : (-643.765, 26.000, -648.608),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_usmain_hmmwv_3',
                    'delete' : False,
                    'template' : 'us_jep_hmmwv',
                    'team' : 2,
                    'delay' : 600,
                    'position' : (-647.249, 26.000, -655.122),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_usmain_hmmwv_4',
                    'delete' : False,
                    'template' : 'us_jep_hmmwv',
                    'team' : 2,
                    'delay' : 600,
                    'position' : (-647.297, 26.000, -648.665),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_usmain_hmmwv_5',
                    'delete' : False,
                    'template' : 'us_jep_hmmwv',
                    'team' : 2,
                    'delay' : 600,
                    'position' : (-651.151, 26.000, -648.747),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_usmain_hmmwv_6',
                    'delete' : False,
                    'template' : 'us_jep_hmmwv',
                    'team' : 2,
                    'delay' : 600,
                    'position' : (-653.719, 26.000, -655.258),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_usmain_hmmwv_7',
                    'delete' : False,
                    'template' : 'us_jep_hmmwv',
                    'team' : 2,
                    'delay' : 600,
                    'position' : (-659.606, 26.000, -655.333),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_usmain_hmmwv_8',
                    'delete' : False,
                    'template' : 'us_jep_hmmwv',
                    'team' : 2,
                    'delay' : 600,
                    'position' : (-662.583, 26.000, -649.083),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_usmain_hmmwv_9',
                    'delete' : False,
                    'template' : 'us_jep_hmmwv',
                    'team' : 2,
                    'delay' : 600,
                    'position' : (-656.599, 26.000, -648.798),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_usmain_hmmwv_mk19_0',
                    'delete' : False,
                    'template' : 'us_jep_hmmwv_uparmored_mk19',
                    'team' : 2,
                    'delay' : 600,
                    'position' : (-628.403, 26.000, -633.676),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_usmain_hmmwv_mk19_1',
                    'delete' : False,
                    'template' : 'us_jep_hmmwv_uparmored_mk19',
                    'team' : 2,
                    'delay' : 600,
                    'position' : (-624.692, 26.000, -633.736),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                # ARF default spawns
                {
                    'name' : 'arf_main_atm1',
                    'delete' : False,
                    'template' : 'civ_atm_technical',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (40.809, 26, 523.824),
                    'rotation' : (180.000, 0.000, 0.000)
                    },
                {
                    'name' : 'arf_main_atm2',
                    'delete' : False,
                    'template' : 'civ_atm_technical',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (46.8542, 26, 523.824),
                    'rotation' : (180.000, 0.000, 0.000)
                    },
                {
                    'name' : 'arf_main_uralzu23_1',
                    'delete' : False,
                    'template' : 'civ_aav_uralzu232',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (97.3817, 26, 513.75),
                    'rotation' : (180.000, 0.000, 0.000)
                    },
                {
                    'name' : 'arf_main_uralzu23_2',
                    'delete' : False,
                    'template' : 'civ_aav_uralzu232',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (92.2107, 26, 513.75),
                    'rotation' : (180.000, 0.000, 0.000)
                    },
                {
                    'name' : 'arf_main_ammocar1',
                    'delete' : False,
                    'template' : 'civ_jep_techincal_support',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (70.0343, 26, 511.307),
                    'rotation' : (180.000, 0.000, 0.000)
                    },
                {
                    'name' : 'arf_main_ammocar2',
                    'delete' : False,
                    'template' : 'civ_jep_techincal_support',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (75.0343, 26, 511.307),
                    'rotation' : (180.000, 0.000, 0.000)
                    },
                {
                    'name' : 'arf_main_techincal1',
                    'delete' : False,
                    'template' : 'civ_jep_techincal',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (45.0723, 26, 477.975),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'arf_main_techincal2',
                    'delete' : False,
                    'template' : 'civ_jep_techincal',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (45.0723, 26, 473.567),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'arf_main_techincal3',
                    'delete' : False,
                    'template' : 'civ_jep_techincal',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (100, 26, 477.975),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'arf_main_techincal4',
                    'delete' : False,
                    'template' : 'civ_jep_techincal',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (100, 26, 473.567),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                # Default spawners, deleting
                {
                    'name' : 'cpname_ramiel_aas128_habr_gidr_hq_acv',
                    'delete' : True,
                    'template' : 'arf_acv_technical',
                    'team' : 1,
                    'delay' : 30,
                    'position' : (-434.807, 25.561, 585.825),
                    'rotation' : (90.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_160th_jeep2',
                    'delete' : True,
                    'template' : 'us_jep_hmmwv',
                    'team' : 2,
                    'delay' : 600,
                    'position' : (-681.662, 24.922, -663.341),
                    'rotation' : (18.774, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_10th_apc2',
                    'delete' : True,
                    'template' : 'fr_apc_vbci',
                    'team' : 2,
                    'delay' : 99999,
                    'position' : (-663.333, 25.0, -606.06),
                    'rotation' : (48.766, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_160th_crate',
                    'delete' : True,
                    'template' : 'fixed_supply_crate_us',
                    'team' : 2,
                    'delay' : 10,
                    'position' : (-556.409, 25.0, -656.401),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_crew5_ammo',
                    'delete' : True,
                    'template' : 'ammocache',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (-510.286, 29.28, 188.861),
                    'rotation' : (90.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_habr_gidr_hq_ammo1',
                    'delete' : True,
                    'template' : 'ammocache',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (83.105, 25.0, 492.553),
                    'rotation' : (90.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_crew3_ammo',
                    'delete' : True,
                    'template' : 'ammocache',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (-798.903, 29.281, 753.191),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_mosque2_rally',
                    'delete' : True,
                    'template' : 'rallypoint_arf_placeable',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (-357.975, 25.0, 420.629),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_mosque1_rally',
                    'delete' : True,
                    'template' : 'rallypoint_arf_placeable',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (251.686, 33.78, 348.532),
                    'rotation' : (84.279, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_habr_gidr_hq_spawn',
                    'delete' : True,
                    'template' : 'rallypoint_arf_placeable',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (-35.399, 25.0, 228.185),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_habr_gidr_hq_ammo5',
                    'delete' : True,
                    'template' : 'ammocache',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (80.379, 30.975, 808.549),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_habr_gidr_hq_jeep6',
                    'delete' : True,
                    'template' : 'civ_jep_car',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (-426.699, 25.0, 609.527),
                    'rotation' : (-180.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_crew7_ammo',
                    'delete' : True,
                    'template' : 'ammocache',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (-227.732, 28.569, 349.682),
                    'rotation' : (-135.306, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_usmain_helo1',
                    'delete' : True,
                    'template' : 'us_the_mh6',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (-328.938, 25.0, -636.964),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_habr_gidr_hq_mortar3',
                    'delete' : True,
                    'template' : 'mortar_team1',
                    'team' : 1,
                    'delay' : 1200,
                    'position' : (-568.174, 24.96, 2562.838),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_habr_gidr_hq_bike3',
                    'delete' : True,
                    'template' : 'civ_bik_dirtbike',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (-501.962, 25.0, 611.714),
                    'rotation' : (29.476, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_160th_tank',
                    'delete' : True,
                    'template' : 'fr_apc_vab',
                    'team' : 2,
                    'delay' : 99999,
                    'position' : (-685.489, 25.0, -628.714),
                    'rotation' : (46.872, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_habr_gidr_hq_jeep3',
                    'delete' : True,
                    'template' : 'civ_aav_uralzu232',
                    'team' : 1,
                    'delay' : 600,
                    'position' : (-491.092, 25.0, 578.76),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_crew8_ammo',
                    'delete' : True,
                    'template' : 'ammocache',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (-503.754, 29.429, 252.449),
                    'rotation' : (90.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_city5_rally',
                    'delete' : True,
                    'template' : 'rallypoint_arf_placeable',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (-945.856, 25.03, 410.563),
                    'rotation' : (101.712, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_160th_helo7_0',
                    'delete' : True,
                    'template' : 'us_the_uh60_soar',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (-580.718, 25.0, -670.87),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_10th_jeep5',
                    'delete' : True,
                    'template' : 'us_jep_hmmwv',
                    'team' : 2,
                    'delay' : 600,
                    'position' : (-702.703, 24.922, -663.557),
                    'rotation' : (20.24, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_crew10_jeep1',
                    'delete' : True,
                    'template' : 'us_jep_hmmwv',
                    'team' : 2,
                    'delay' : 99999,
                    'position' : (30.726, 25.0, 432.36),
                    'rotation' : (96.038, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_160th_acv',
                    'delete' : True,
                    'template' : 'us_acv_stryker',
                    'team' : 2,
                    'delay' : 1,
                    'position' : (-508.864, 25.58, -647.829),
                    'rotation' : (-180.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_habr_gidr_hq_bike4',
                    'delete' : True,
                    'template' : 'civ_bik_dirtbike',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (-501.801, 25.0, 615.612),
                    'rotation' : (30.191, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_habr_gidr_hq_repairdepot',
                    'delete' : True,
                    'template' : 'vehicle_depot_tal',
                    'team' : 1,
                    'delay' : 1,
                    'position' : (-478.798, 25.0, 622.616),
                    'rotation' : (90.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_city2_ammo',
                    'delete' : True,
                    'template' : 'ammocache',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (779.942, 21.458, -305.615),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_city4_car',
                    'delete' : True,
                    'template' : 'civ_jep_car_blue',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (82.879, 30.975, 829.592),
                    'rotation' : (-111.847, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_deltaforce_crate2',
                    'delete' : True,
                    'template' : 'fixed_supply_crate_us',
                    'team' : 2,
                    'delay' : 10,
                    'position' : (-300.174, 25.0, -653.157),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_10th_jeep4',
                    'delete' : True,
                    'template' : 'us_jep_hmmwv',
                    'team' : 2,
                    'delay' : 600,
                    'position' : (-697.435, 24.922, -663.476),
                    'rotation' : (20.586, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_habr_gidr_hq_jeep5',
                    'delete' : True,
                    'template' : 'civ_jep_car_black',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (-430.824, 25.0, 608.847),
                    'rotation' : (162.17, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_habr_gidr_hq_bike1',
                    'delete' : True,
                    'template' : 'civ_bik_dirtbike',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (-493.819, 25.0, 578.803),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_habr_gidr_hq_mortar2',
                    'delete' : True,
                    'template' : 'mortar_team1',
                    'team' : 1,
                    'delay' : 1200,
                    'position' : (-782.23, 24.96, 2631.58),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_blackhawk2_spawn2',
                    'delete' : True,
                    'template' : 'rallypoint_arf_placeable',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (-32.843, 25.019, 249.076),
                    'rotation' : (-178.489, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_habr_gidr_hq_ammo1_0',
                    'delete' : True,
                    'template' : 'ammocache',
                    'team' : 1,
                    'delay' : 10,
                    'position' : (-456.467, 25.0, 583.509),
                    'rotation' : (180.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_160th_helo3',
                    'delete' : True,
                    'template' : 'us_the_uh60_soar',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (-599.177, 25.0, -669.998),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_habr_gidr_hq_ammo2_0',
                    'delete' : True,
                    'template' : 'ammocache',
                    'team' : 1,
                    'delay' : 10,
                    'position' : (-464.483, 25.0, 620.703),
                    'rotation' : (-90.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_10th_crate2',
                    'delete' : True,
                    'template' : 'fixed_supply_crate_us',
                    'team' : 2,
                    'delay' : 10,
                    'position' : (-689.634, 24.922, -680.999),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_crew12_jeep3',
                    'delete' : True,
                    'template' : 'us_jep_hmmwv_uparmored_mk19',
                    'team' : 2,
                    'delay' : 99999,
                    'position' : (36.438, 25.0, 435.326),
                    'rotation' : (86.533, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_deltaforce_crate',
                    'delete' : True,
                    'template' : 'fixed_supply_crate_us',
                    'team' : 2,
                    'delay' : 10,
                    'position' : (-364.004, 25.0, -643.047),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_160th_jeep3',
                    'delete' : True,
                    'template' : 'us_jep_hmmwv',
                    'team' : 2,
                    'delay' : 600,
                    'position' : (-687.256, 24.922, -663.52),
                    'rotation' : (21.355, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_160th_depot',
                    'delete' : True,
                    'template' : 'vehicle_depot_us',
                    'team' : 2,
                    'delay' : 30,
                    'position' : (-719.592, 25.0, -585.962),
                    'rotation' : (-90.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_city5_ammo',
                    'delete' : True,
                    'template' : 'ammocache',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (-937.971, 25.185, 408.474),
                    'rotation' : (41.886, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_10th_crate',
                    'delete' : True,
                    'template' : 'fixed_supply_crate_us',
                    'team' : 2,
                    'delay' : 10,
                    'position' : (-727.645, 25.0, -665.829),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_usmain_helo6',
                    'delete' : True,
                    'template' : 'us_the_mh6',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (-310.522, 25.0, -636.971),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_crew12_cache',
                    'delete' : True,
                    'template' : 'fixed_supply_crate_us',
                    'team' : 2,
                    'delay' : 99999,
                    'position' : (51.709, 25.01, 440.336),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_crew14_ammo',
                    'delete' : True,
                    'template' : 'ammocache',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (-160.681, 33.391, 414.344),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_crew4_ammo',
                    'delete' : True,
                    'template' : 'ammocache',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (-902.315, 33.421, 665.834),
                    'rotation' : (-180.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_habr_gidr_hq_spg',
                    'delete' : True,
                    'template' : 'civ_atm_technical',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (-421.085, 25.0, 596.528),
                    'rotation' : (83.425, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_10th_apc1',
                    'delete' : True,
                    'template' : 'fr_apc_vbci',
                    'team' : 2,
                    'delay' : 99999,
                    'position' : (-675.288, 25.0, -617.879),
                    'rotation' : (46.872, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_crew11_jeep1',
                    'delete' : True,
                    'template' : 'us_jep_hmmwv',
                    'team' : 2,
                    'delay' : 99999,
                    'position' : (44.634, 25.0, 434.05),
                    'rotation' : (86.533, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_habr_gidr_hq_bike2',
                    'delete' : True,
                    'template' : 'civ_bik_dirtbike',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (-502.288, 25.0, 607.706),
                    'rotation' : (32.479, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_crew11_cache',
                    'delete' : True,
                    'template' : 'fixed_supply_crate_us',
                    'team' : 2,
                    'delay' : 99999,
                    'position' : (-88.748, 29.113, 106.099),
                    'rotation' : (90.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_crew1_ammo',
                    'delete' : True,
                    'template' : 'ammocache',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (-730.793, 33.391, 512.536),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_habr_gidr_hq_mortar1',
                    'delete' : True,
                    'template' : 'mortar_team1',
                    'team' : 1,
                    'delay' : 1200,
                    'position' : (-622.97, 24.96, 2686.124),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_habr_gidr_hq_ammo2',
                    'delete' : True,
                    'template' : 'ammocache',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (-30.164, 25.0, 236.698),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_mosque2_crate',
                    'delete' : True,
                    'template' : 'ammocache',
                    'team' : 1,
                    'delay' : 10,
                    'position' : (-373.231, 25.218, 432.545),
                    'rotation' : (-180.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_city2_car',
                    'delete' : True,
                    'template' : 'civ_jep_car',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (776.414, 21.458, -286.483),
                    'rotation' : (154.332, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_160th_jeep1',
                    'delete' : True,
                    'template' : 'us_jep_hmmwv_mk19',
                    'team' : 2,
                    'delay' : 600,
                    'position' : (-692.033, 24.922, -663.698),
                    'rotation' : (18.848, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_crew2_ammo',
                    'delete' : True,
                    'template' : 'ammocache',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (-666.689, 29.328, 732.089),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_crew15_ammo',
                    'delete' : True,
                    'template' : 'ammocache',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (-624.837, 25.127, 445.746),
                    'rotation' : (-90.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_habr_gidr_hq_mortar4',
                    'delete' : True,
                    'template' : 'mortar_team1',
                    'team' : 1,
                    'delay' : 1200,
                    'position' : (-671.26, 24.96, 2647.892),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_habr_gidr_hq_jeep1',
                    'delete' : True,
                    'template' : 'civ_jep_support_logistics',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (-477.833, 25.0, 596.384),
                    'rotation' : (-92.085, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_habr_gidr_hq_spawn3',
                    'delete' : True,
                    'template' : 'rallypoint_arf_placeable',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (86.624, 30.975, 816.29),
                    'rotation' : (-153.243, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_mosque1_crate',
                    'delete' : True,
                    'template' : 'ammocache',
                    'team' : 1,
                    'delay' : 10,
                    'position' : (254.13, 33.843, 362.261),
                    'rotation' : (-180.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_habr_gidr_hq_jeep4',
                    'delete' : True,
                    'template' : 'civ_jep_technical',
                    'team' : 1,
                    'delay' : 600,
                    'position' : (-501.637, 25.0, 578.395),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_mosque1_rally2',
                    'delete' : True,
                    'template' : 'rallypoint_arf_placeable',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (288.171, 33.78, 358.014),
                    'rotation' : (-90.857, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_city5_ins_jeep_3',
                    'delete' : True,
                    'template' : 'civ_jep_car_blue',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (-951.654, 25.03, 397.547),
                    'rotation' : (-90.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_usmain_helo5',
                    'delete' : True,
                    'template' : 'us_the_mh6',
                    'team' : 2,
                    'delay' : 99999,
                    'position' : (-274.838, 25.0, -637.14),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_usmain_helo4',
                    'delete' : True,
                    'template' : 'us_ahe_ah6',
                    'team' : 2,
                    'delay' : 1200,
                    'position' : (-257.087, 25.0, -636.708),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_habr_gidr_hq_jeep2',
                    'delete' : True,
                    'template' : 'civ_jep_technical_red',
                    'team' : 1,
                    'delay' : 600,
                    'position' : (-484.515, 25.0, 578.685),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_160th_helo7',
                    'delete' : True,
                    'template' : 'us_ahe_ah6',
                    'team' : 2,
                    'delay' : 1200,
                    'position' : (-239.338, 25.0, -636.895),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_crew13_ammo',
                    'delete' : True,
                    'template' : 'ammocache',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (-99.253, 25.02, 573.245),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_habr_gidr_hq_jeep7',
                    'delete' : True,
                    'template' : 'civ_jep_technical',
                    'team' : 1,
                    'delay' : 600,
                    'position' : (-422.238, 25.0, 609.841),
                    'rotation' : (-180.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_10th_logi',
                    'delete' : True,
                    'template' : 'us_trk_logistics',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (-716.998, 25.0, -577.791),
                    'rotation' : (90.987, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_crew6_ammo',
                    'delete' : True,
                    'template' : 'ammocache',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (-254.281, 33.391, 199.754),
                    'rotation' : (-90.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_ramiel_aas128_habr_gidr_hq_spawn4',
                    'delete' : True,
                    'template' : 'rallypoint_arf_placeable',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (82.942, 25.0, 508.928),
                    'rotation' : (-156.886, 0.0, 0.0)
                    },
                ]
            }
        },
    'bamyan' : {
        'gpm_cq' : {
            32 :[
                # USMC spawns
                {
                    'name' : 'USA_OS_main_fixed_spawn_0',
                    'template' : 'rallypoint_us_placeable',
                    'delete' : False,
                    'team' : 2,
                    'delay' : 99999,
                    'position' : (1269.223, 47.404, 1118.870),
                    'rotation' : (4.886, 0.000, 0.000)
                    },
                {
                    'name' : 'USA_OS_main_FOB',
                    'template' : 'deployable_firebase',
                    'delete' : False,
                    'team' : 2,
                    'delay' : 99999,
                    'position' : (1243.722, 47.196, 1144.192),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                # Taliban spawns
                {
                    'name' : 'Taliban_SP_1_1',
                    'template' : 'rallypoint_taliban_placeable',
                    'delete' : False,
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (598.250, 34.443, 1313.153),
                    'rotation' : (-171.829, 0.000, 0.000)
                    },
                {
                    'name' : 'Taliban_SP_2_1',
                    'template' : 'rallypoint_taliban_placeable',
                    'delete' : False,
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (1623.301, 36.348, 1813.809),
                    'rotation' : (109.847, 0.000, 0.000)
                    },
                {
                    'name' : 'Taliban_SP_3_1',
                    'template' : 'rallypoint_taliban_placeable',
                    'delete' : False,
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (1820.718, 82.185, 483.500),
                    'rotation' : (144.024, 0.000, 0.000)
                    },
                # USMC spawners
                {
                    'name' : 'USA_OS_main_VehicleSpwn_1',
                    'template' : 'us_jep_hmmwv_uparmored',
                    'delete' : False,
                    'team' : 2,
                    'delay' : 300,
                    'position' : (1288.271, 47.992, 1161.503),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'USA_OS_main_Humvee2',
                    'template' : 'us_jep_hmmwv_uparmored',
                    'delete' : False,
                    'team' : 2,
                    'delay' : 300,
                    'position' : (1229.208, 47.070, 1153.982),
                    'rotation' : (-47.693, 0.000, 0.000)
                    },
                {
                    'name' : 'USA_OS_main_sply1',
                    'template' : 'fixed_supply_crate_us',
                    'delete' : False,
                    'team' : 2,
                    'delay' : 300,
                    'position' : (1219.495, 47.893, 1116.552),
                    'rotation' : (39.119, 0.000, 0.000)
                    },
                {
                    'name' : 'USA_OS_main_sply2',
                    'template' : 'fixed_supply_crate_us',
                    'delete' : False,
                    'team' : 2,
                    'delay' : 300,
                    'position' : (1235.473, 46.921, 1157.266),
                    'rotation' : (44.181, 0.000, 0.000)
                    },
                {
                    'name' : 'USA_OS_main_sply3',
                    'template' : 'fixed_supply_crate_us',
                    'delete' : False,
                    'team' : 2,
                    'delay' : 300,
                    'position' : (1246.846, 46.921, 1175.195),
                    'rotation' : (-49.069, 0.000, 0.000)
                    },
                {
                    'name' : 'USA_OS_main_sply4',
                    'template' : 'fixed_supply_crate_us',
                    'delete' : False,
                    'team' : 2,
                    'delay' : 300,
                    'position' : (1274.395, 49.997, 1205.436),
                    'rotation' : (0.000, 0.000, 0.000)
                    },
                {
                    'name' : 'USA_OS_main_sply5',
                    'template' : 'fixed_supply_crate_us',
                    'delete' : False,
                    'team' : 2,
                    'delay' : 300,
                    'position' : (1275.315, 46.921, 1126.203),
                    'rotation' : (31.146, 0.000, 0.000)
                    },
                {
                    'name' : 'USA_OS_main_sply6',
                    'template' : 'fixed_supply_crate_us',
                    'delete' : False,
                    'team' : 2,
                    'delay' : 300,
                    'position' : (1298.900, 46.921, 1116.142),
                    'rotation' : (96.634, 0.000, 0.000)
                    },
                {
                    'name' : 'USA_OS_main_sply7',
                    'template' : 'fixed_supply_crate_us',
                    'delete' : False,
                    'team' : 2,
                    'delay' : 300,
                    'position' : (1298.371, 46.985, 1137.345),
                    'rotation' : (-167.539, 0.000, 0.000)
                    },
                {
                    'name' : 'USA_OS_main_sply8',
                    'template' : 'fixed_supply_crate_us',
                    'delete' : False,
                    'team' : 2,
                    'delay' : 300,
                    'position' : (1216.540, 47.893, 1099.515),
                    'rotation' : (37.470, 0.000, 0.000)
                    },
                {
                    'name' : 'USA_OS_main_LogiTruckUSA',
                    'template' : 'us_trk_logistics',
                    'delete' : False,
                    'team' : 2,
                    'delay' : 300,
                    'position' : (1223.100, 47.893, 1134.893),
                    'rotation' : (-138.616, 0.000, 0.000)
                    },
                # Taliban spawners
                {
                    'name' : 'Taliban_OS_3_sply2',
                    'template' : 'fixed_supply_crate_tal',
                    'delete' : False,
                    'team' : 1,
                    'delay' : 300,
                    'position' : (1826.507, 84.441, 448.439),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_OS_1_Vehicle_technical',
                    'template' : 'civ_jep_technical_black',
                    'delete' : False,
                    'team' : 1,
                    'delay' : 300,
                    'position' : (593.042, 36.309, 1277.786),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_OS_3_sply_3',
                    'template' : 'fixed_supply_crate_tal',
                    'delete' : False,
                    'team' : 1,
                    'delay' : 300,
                    'position' : (1830.948, 82.162, 487.835),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_Vehicle_Zastava_1',
                    'template' : 'civ_jep_zastava900ak',
                    'delete' : False,
                    'team' : 1,
                    'delay' : 300,
                    'position' : (601.908, 35.227, 1298.468),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_Vehicle_VBIED',
                    'template' : 'civ_trk_dumpster_bomber',
                    'delete' : False,
                    'team' : 1,
                    'delay' : 300,
                    'position' : (586.171, 39.99, 1235.035),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_CP2_Vehicle_Zastava2',
                    'template' : 'civ_jep_zastava900ak',
                    'delete' : False,
                    'team' : 1,
                    'delay' : 300,
                    'position' : (1626.689, 33.777, 1838.27),
                    'rotation' : (171.566, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_CP3_Vehicle_Zastava2',
                    'template' : 'civ_jep_zastava900ak',
                    'delete' : False,
                    'team' : 1,
                    'delay' : 300,
                    'position' : (1836.855, 84.908, 437.604),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_OS_1_technical_ammo',
                    'template' : 'civ_jep_support',
                    'delete' : False,
                    'team' : 1,
                    'delay' : 300,
                    'position' : (581.798, 36.683, 1275.51),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_OS_1_sply_1',
                    'template' : 'fixed_supply_crate_tal',
                    'delete' : False,
                    'team' : 1,
                    'delay' : 300,
                    'position' : (582.681, 34.863, 1312.098),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_CP3_Vehicle_Zastava1',
                    'template' : 'civ_jep_zastava900ak',
                    'delete' : False,
                    'team' : 1,
                    'delay' : 300,
                    'position' : (1836.605, 84.075, 457.102),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_Vehicle_Zastava_2',
                    'template' : 'civ_jep_zastava900ak',
                    'delete' : False,
                    'team' : 1,
                    'delay' : 300,
                    'position' : (580.358, 34.993, 1297.46),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_OS_3_technical_ammo',
                    'template' : 'civ_jep_support',
                    'delete' : False,
                    'team' : 1,
                    'delay' : 300,
                    'position' : (1837.315, 84.451, 448.946),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_OS_2_technical_ammo',
                    'template' : 'civ_jep_support',
                    'delete' : False,
                    'team' : 1,
                    'delay' : 300,
                    'position' : (1636.724, 33.204, 1844.477),
                    'rotation' : (-174.61, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_CP3_Vehicle_DSHKm',
                    'template' : 'civ_jep_technical_black',
                    'delete' : False,
                    'team' : 1,
                    'delay' : 300,
                    'position' : (1824.927, 83.943, 457.796),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_CP2_Vehicle_Zastava',
                    'template' : 'civ_jep_zastava900ak',
                    'delete' : False,
                    'team' : 1,
                    'delay' : 300,
                    'position' : (1642.06, 35.295, 1826.208),
                    'rotation' : (-174.772, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_CP3_Vehicle_VBIED',
                    'template' : 'civ_trk_dumpster_bomber',
                    'delete' : False,
                    'team' : 1,
                    'delay' : 300,
                    'position' : (1826.948, 86.6, 398.444),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_CP2_Vehicle_DSHKm',
                    'template' : 'civ_jep_zastava900ak',
                    'delete' : False,
                    'team' : 1,
                    'delay' : 300,
                    'position' : (1630.216, 35.06, 1823.614),
                    'rotation' : (-178.794, 0.0, 0.0)
                    },
                {
                    'name' : 'Taliban_OS_2_sply_2',
                    'template' : 'fixed_supply_crate_tal',
                    'delete' : False,
                    'team' : 1,
                    'delay' : 300,
                    'position' : (1643.892, 37.482, 1806.833),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                # Default spawners
                {
                    'name' : 'cpname_bamyan_aas32_opformain_citycar11',
                    'delete' : True,
                    'template' : 'civ_jep_car',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (871.658, 74.291, -250.136),
                    'rotation' : (-180.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_usmain_hmmwv5',
                    'delete' : True,
                    'template' : 'us_jep_hmmwv_support',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (-1178.304, 93.981, -2027.115),
                    'rotation' : (-2.294, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_car2',
                    'delete' : True,
                    'template' : 'civ_jep_support_logistics',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (-1881.596, 1.024, 1937.768),
                    'rotation' : (-172.511, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_citycar1',
                    'delete' : True,
                    'template' : 'civ_jep_car_blue',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (-647.559, 17.389, 1079.906),
                    'rotation' : (-83.725, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_checkpoint5_firebase5',
                    'delete' : True,
                    'template' : 'rallypoint_us_placeable',
                    'team' : 2,
                    'delay' : 99999,
                    'position' : (1248.937, 47.705, 1132.77),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_usmain_trans1',
                    'delete' : True,
                    'template' : 'us_trk_logistics',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (-1244.906, 93.981, -2005.873),
                    'rotation' : (90.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_usmain_hmmwv2',
                    'delete' : True,
                    'template' : 'us_jep_hmmwv_uparmored',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (-1192.816, 93.981, -2019.035),
                    'rotation' : (14.748, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_command',
                    'delete' : True,
                    'template' : 'fixed_supply_crate_tal',
                    'team' : 1,
                    'delay' : 30,
                    'position' : (-1898.625, 1.024, 1910.563),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_usmain_ah',
                    'delete' : True,
                    'template' : 'us_jet_a10a',
                    'team' : 2,
                    'delay' : 99999,
                    'position' : (90.961, 82.103, -1718.12),
                    'rotation' : (160.9, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_gary',
                    'delete' : True,
                    'template' : 'civ_trk_dumpster_bomber',
                    'team' : 1,
                    'delay' : 1200,
                    'position' : (-1923.253, 1.024, 1900.373),
                    'rotation' : (99.153, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_citycar6',
                    'delete' : True,
                    'template' : 'civ_jep_car_black',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (-678.661, 24.166, 466.008),
                    'rotation' : (84.252, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_usmain_trans2',
                    'delete' : True,
                    'template' : 'us_the_mv22',
                    'team' : 2,
                    'delay' : 600,
                    'position' : (-1230.351, 93.981, -2021.379),
                    'rotation' : (90.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_bomber1',
                    'delete' : True,
                    'template' : 'civ_jep_car_bomber_white',
                    'team' : 1,
                    'delay' : 1200,
                    'position' : (-1914.166, 1.024, 1898.521),
                    'rotation' : (100.026, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_usmain_logi2',
                    'delete' : True,
                    'template' : 'us_trk_logistics',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (-1244.719, 93.981, -2000.222),
                    'rotation' : (90.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_car5',
                    'delete' : True,
                    'template' : 'civ_jep_technical_black',
                    'team' : 1,
                    'delay' : 600,
                    'position' : (-1890.005, 1.024, 1938.775),
                    'rotation' : (-172.5, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_citycar9',
                    'delete' : True,
                    'template' : 'civ_jep_car_blue',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (-803.257, 21.856, 704.984),
                    'rotation' : (93.785, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_usmain_loyspawn',
                    'delete' : True,
                    'template' : 'rallypoint_us_placeable',
                    'team' : 2,
                    'delay' : 99999,
                    'position' : (-61.508, 82.103, -1762.174),
                    'rotation' : (-15.982, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_usmain_hmmwv4',
                    'delete' : True,
                    'template' : 'us_jep_hmmwv_uparmored',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (-1192.871, 93.981, -2002.151),
                    'rotation' : (14.748, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_usmain_artillery1',
                    'delete' : True,
                    'template' : 'artillery_team2',
                    'team' : 2,
                    'delay' : 1800,
                    'position' : (-1230.174, 97.363, -3000.168),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_citycar8',
                    'delete' : True,
                    'template' : 'civ_jep_car',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (405.741, 58.91, -144.866),
                    'rotation' : (-70.441, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_usmain_hmmwv6',
                    'delete' : True,
                    'template' : 'us_jep_hmmwv_support',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (-1178.164, 93.981, -2015.801),
                    'rotation' : (2.515, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_citycar4',
                    'delete' : True,
                    'template' : 'civ_jep_car',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (-520.558, 21.948, 841.11),
                    'rotation' : (-154.862, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_usmain_hmmwv1',
                    'delete' : True,
                    'template' : 'us_jep_hmmwv_uparmored',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (-1192.653, 93.817, -2026.846),
                    'rotation' : (14.748, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_usmain_crate1',
                    'delete' : True,
                    'template' : 'fixed_supply_crate_us',
                    'team' : 2,
                    'delay' : 30,
                    'position' : (-1198.097, 93.981, -2007.937),
                    'rotation' : (-90.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_usmain_depot',
                    'delete' : True,
                    'template' : 'vehicle_depot_us',
                    'team' : 2,
                    'delay' : 30,
                    'position' : (-1244.821, 93.981, -1980.843),
                    'rotation' : (-90.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_usmain_crate2',
                    'delete' : True,
                    'template' : 'fixed_supply_crate_us',
                    'team' : 2,
                    'delay' : 30,
                    'position' : (-1212.096, 93.981, -2012.696),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_crate2',
                    'delete' : True,
                    'template' : 'fixed_supply_crate_tal',
                    'team' : 1,
                    'delay' : 30,
                    'position' : (-1905.631, 1.024, 1941.369),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_spg2',
                    'delete' : True,
                    'template' : 'civ_atm_technical',
                    'team' : 1,
                    'delay' : 600,
                    'position' : (-1902.749, 1.024, 1920.27),
                    'rotation' : (101.462, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_usmain_support2',
                    'delete' : True,
                    'template' : 'us_trk_support',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (-1200.473, 93.981, -1972.781),
                    'rotation' : (90.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_citycar7',
                    'delete' : True,
                    'template' : 'civ_jep_car',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (-700.72, 21.856, 725.124),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_citycar10',
                    'delete' : True,
                    'template' : 'civ_jep_car_blue',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (-688.416, 42.026, -247.0),
                    'rotation' : (-124.724, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_car4',
                    'delete' : True,
                    'template' : 'civ_jep_zastava900ak',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (-1885.8, 1.024, 1938.325),
                    'rotation' : (-172.511, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_usmain_artillery2',
                    'delete' : True,
                    'template' : 'artillery_team2',
                    'team' : 2,
                    'delay' : 1800,
                    'position' : (-1236.733, 96.542, -3000.453),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_checkpoint4_firebase4',
                    'delete' : True,
                    'template' : 'rallypoint_us_placeable',
                    'team' : 2,
                    'delay' : 99999,
                    'position' : (317.622, 55.776, -32.91),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_citycar12',
                    'delete' : True,
                    'template' : 'civ_jep_car',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (-790.145, 44.061, -375.342),
                    'rotation' : (-16.793, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_checkpoint3_firebase3',
                    'delete' : True,
                    'template' : 'rallypoint_us_placeable',
                    'team' : 2,
                    'delay' : 99999,
                    'position' : (-637.001, 32.833, 215.342),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_usmain_hmmwvnorespawn',
                    'delete' : True,
                    'template' : '',
                    'team' : 2,
                    'delay' : 99999,
                    'position' : (155.031, 82.103, -1652.678),
                    'rotation' : (-9.831, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_van1',
                    'delete' : True,
                    'template' : 'civ_jep_zastava900ak',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (-1872.933, 1.024, 1910.65),
                    'rotation' : (-82.5, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_van3',
                    'delete' : True,
                    'template' : 'civ_jep_zastava900ak',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (-1872.004, 1.024, 1917.775),
                    'rotation' : (-82.5, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_mg1',
                    'delete' : True,
                    'template' : 'civ_atm_technical_rocket',
                    'team' : 1,
                    'delay' : 600,
                    'position' : (-1901.171, 1.024, 1929.058),
                    'rotation' : (101.462, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_usmain_logi1',
                    'delete' : True,
                    'template' : 'us_trk_logistics',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (-1244.801, 93.981, -1994.292),
                    'rotation' : (90.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_car3',
                    'delete' : True,
                    'template' : 'civ_jep_technical_black',
                    'team' : 1,
                    'delay' : 600,
                    'position' : (-1894.105, 1.024, 1939.33),
                    'rotation' : (-172.511, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_mg2',
                    'delete' : True,
                    'template' : 'civ_aav_uralzu232',
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (-1896.733, 1.024, 1895.686),
                    'rotation' : (98.199, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_checkpoint1_firebase1',
                    'delete' : True,
                    'template' : 'rallypoint_us_placeable',
                    'team' : 2,
                    'delay' : 99999,
                    'position' : (-559.274, 17.389, 1040.196),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_citycar5',
                    'delete' : True,
                    'template' : 'civ_jep_car_black',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (-733.978, 20.519, 933.733),
                    'rotation' : (-130.242, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_checkpoint9_0',
                    'delete' : True,
                    'template' : 'rallypoint_us_placeable',
                    'team' : 2,
                    'delay' : 99999,
                    'position' : (518.162, 50.024, 833.958),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_usmain_command',
                    'delete' : True,
                    'template' : 'us_acv_lavc2',
                    'team' : 2,
                    'delay' : 30,
                    'position' : (-1206.396, 94.789, -2027.705),
                    'rotation' : (-180.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_citycar2',
                    'delete' : True,
                    'template' : 'civ_jep_car_blue',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (-657.451, 15.539, 1249.283),
                    'rotation' : (-63.054, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_car1',
                    'delete' : True,
                    'template' : 'civ_jep_support_logistics',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (-1877.29, 1.024, 1937.202),
                    'rotation' : (-172.511, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_usmain_artillery3',
                    'delete' : True,
                    'template' : 'artillery_team2',
                    'team' : 2,
                    'delay' : 1800,
                    'position' : (-1233.534, 96.219, -3008.662),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_checkpoint2_firebase2',
                    'delete' : True,
                    'template' : 'rallypoint_us_placeable',
                    'team' : 2,
                    'delay' : 99999,
                    'position' : (-1283.901, 36.166, 604.771),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_usmain_crate3',
                    'delete' : True,
                    'template' : 'fixed_supply_crate_us',
                    'team' : 2,
                    'delay' : 30,
                    'position' : (-1212.109, 93.981, -2000.64),
                    'rotation' : (0.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_citycar3',
                    'delete' : True,
                    'template' : 'civ_jep_car',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (-556.333, 15.441, 1167.781),
                    'rotation' : (-65.888, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_depot',
                    'delete' : True,
                    'template' : 'vehicle_depot_tal',
                    'team' : 1,
                    'delay' : 30,
                    'position' : (-1864.337, 1.024, 1924.554),
                    'rotation' : (97.5, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_usmain_logi3',
                    'delete' : True,
                    'template' : 'us_jep_hmmwv_support',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (-1176.485, 93.981, -2003.649),
                    'rotation' : (14.698, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_aav1',
                    'delete' : True,
                    'template' : 'civ_aav_uralzu232',
                    'team' : 1,
                    'delay' : 600,
                    'position' : (-1905.586, 1.024, 1896.856),
                    'rotation' : (98.188, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_usmain_hmmwv3',
                    'delete' : True,
                    'template' : 'us_jep_hmmwv_uparmored',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (-1192.792, 93.981, -2010.543),
                    'rotation' : (14.748, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_usmain_support1',
                    'delete' : True,
                    'template' : 'us_trk_support',
                    'team' : 2,
                    'delay' : 300,
                    'position' : (-1200.433, 93.981, -1978.078),
                    'rotation' : (90.0, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_van2',
                    'delete' : True,
                    'template' : 'civ_jep_zastava900ak',
                    'team' : 1,
                    'delay' : 300,
                    'position' : (-1872.488, 1.024, 1914.318),
                    'rotation' : (-82.5, 0.0, 0.0)
                    },
                {
                    'name' : 'cpname_bamyan_aas32_opformain_spg1',
                    'delete' : True,
                    'template' : 'civ_atm_technical',
                    'team' : 1,
                    'delay' : 600,
                    'position' : (-1901.984, 1.024, 1924.628),
                    'rotation' : (101.462, 0.0, 0.0)
                    },
                ]
            }
        }
    }

MAP_FLAGS = {
    'ramiel' : {
        'gpm_cq' : {
            128 : {
                'cpname_ramiel_aas128_habr_gidr_hq' : (67.3558, 20.0, 525.785)
                }
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
                    'delete' : False,
                    'modify' : True,
                    'team' : 1, # we're changing to team 1 so USMC can't move anywhere
                    'vehicles' : 4,
                    'layer' : 4,
                    'inverted' : 0,
                    'areapoints' : [
                        (2048.000000, -2048.000000),
                        (2048.000000, 2048.000000),
                        (-2048.000000, 2048.000000),
                        (-2048.000000, -2048.000000)
                        ]
                    },
                'CombatArea_12_aas_32' : {
                    'name' : 'CombatArea_12_aas_32',
                    'create' : True,
                    'delete' : False,
                    'modify' : False,
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
                'CombatArea_11_aas_32' : {
                    'name' : 'CombatArea_11_aas_32',
                    'create' : False,
                    'delete' : False,
                    'modify' : True,
                    'team' : 1, # we're changing to team 1 so USMC can't move anywhere
                    'vehicles' : 4,
                    'layer' : 4,
                    'inverted' : 1,
                    'areapoints' : [
                        (-2047.375488, 2047.329834),
                        (-1279.542725, 2047.559326),
                        (-1269.797852, 1754.953369),
                        (-1710.020508, 1540.485596),
                        (-2045.995850, 1418.165771),
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















