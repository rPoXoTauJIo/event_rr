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
    ('ramiel', 'gpm_cq', 64),
    ('ramiel', 'gpm_cq', 128),
    ]

MAP_HIDEOUTS = {
    'ramiel' : {
        'gpm_cq' : {
            64 : [
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
            64 : [
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
            64 :[
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















