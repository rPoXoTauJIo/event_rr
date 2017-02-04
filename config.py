# config file

# address and port for listening UDP server
SERVERHOST = 'localhost'  # Symbolic name meaning all available interfaces
SERVERPORT = 8888  # Arbitrary non-privileged port

# address and port for streaming client
CLIENTHOST = 'localhost'  # Symbolic name meaning all available interfaces
CLIENTPORT = 8888  # Arbitrary non-privileged port

DEBUGS_DEFAULT = [
    'file',  # debugging in files, set log path first
    #'udp', # UDP debug, sending
    'echo',  # printing debug to server console
    #'ingame' # printing debug ingame
]

# specify on which levels event script will run
MAP_EVENT = [
    #('ramiel', 'gpm_cq', 64), # pure for testing
    ('ramiel', 'gpm_cq', 128),
]

MAP_HIDEOUTS = {
    'ramiel': {
        'gpm_cq': {
            128: [
                {  # need to have this short spawn incase prics on main
                    'name': 'cpname_ramiel_aas128_insmain_fob_0',
                    'template': 'fixed_insurgent_hideout',
                    'team': 1,
                    'delay': 60,
                    'position': (65.126, 28.689, 500.840),
                    'rotation': (0.000, 0.000, 0.000)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_vcp_hideout_0',
                    'template': 'fixed_insurgent_hideout',
                    'team': 1,
                    'delay': 99999,
                    'position': (-57.513, 24.883, -234.638),
                    'rotation': (170.446, 0.000, 0.000)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_fob_hideout_0',
                    'template': 'fixed_insurgent_hideout',
                    'team': 1,
                    'delay': 99999,
                    'position': (16.078, 26.171, 67.502),
                    'rotation': (0.000, 0.000, 0.000)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_prison_hideout_0',
                    'template': 'fixed_insurgent_hideout',
                    'team': 1,
                    'delay': 99999,
                    'position': (64.974, 27.872, 330.396),
                    'rotation': (0.000, 0.000, 0.000)
                },
            ]
        }
    }
}

MAP_OBJECTIVES = {
    'ramiel': {
        'gpm_cq': {
            128: [
                {
                    'name': 'ammocache_1',
                    'template': 'ammocache',
                    'team': 1,
                    'delay': 99999,
                    'position': (-41.895, 25.1362, -238.107),
                    'rotation': (0.000, 0.000, 0.000)
                },
                {
                    'name': 'ammocache_2',
                    'template': 'ammocache',
                    'team': 1,
                    'delay': 99999,
                    'position': (37.1265, 25.1362, 56.8647),
                    'rotation': (0.000, 0.000, 0.000)
                },
                {
                    'name': 'ammocache_3',
                    'template': 'ammocache',
                    'team': 1,
                    'delay': 99999,
                    'position': (59.3651, 27.931, 306.934),
                    'rotation': (0.000, 0.000, 0.000)
                },
                {
                    'name': 'ammocache_4',
                    'template': 'ammocache',
                    'team': 1,
                    'delay': 99999,
                    'position': (67.3558, 25.1935, 525.785),
                    'rotation': (0.000, 0.000, 0.000)
                },
            ]
        }
    }
}

MAP_SPAWNERS_WAVE = {
    'ramiel': {
        'gpm_cq': {
            128: {
                1: [
                    {
                        'name': 'cpname_ramiel_aas128_usmain_vcp_vbci_0',
                        'delete': False,
                        'template': 'fr_apc_vbci',
                        'team': 2,
                        'delay': 600,
                        'position': (-46.040, 26.500, -259.076),
                        'rotation': (0.000, 0.000, 0.000)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_usmain_vcp_hmmwv_0',
                        'delete': False,
                        'template': 'us_jep_hmmwv',
                        'team': 2,
                        'delay': 99999,
                        'position': (-29.993, 26.000, -229.538),
                        'rotation': (-79.633, 0.000, 0.000)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_usmain_vcp_hmmwv_mk19_1',
                        'delete': False,
                        'template': 'us_jep_hmmwv_mk19',
                        'team': 2,
                        'delay': 99999,
                        'position': (-36.443, 26.000, -228.408),
                        'rotation': (-80.172, 0.000, 0.000)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_usmain_vcp_crate_0',
                        'delete': False,
                        'template': 'fixed_supply_crate_us',
                        'team': 2,
                        'delay': 300,
                        'position': (-52.829, 25.500, -269.352),
                        'rotation': (0.000, 0.000, 0.000)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_usmain_depot',
                        'delete': False,
                        'template': 'vehicle_depot_us',
                        'team': 2,
                        'delay': 99999,
                        'position': (-719.592, 25.0, -585.962),
                        'rotation': (-90.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_prison_pkm_1',
                        'delete': False,
                        'template': 'arf_mg',
                        'team': 1,
                        'delay': 300,
                        'position': (48.269, 27.844, 345.579),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_prison_rpg_0',
                        'delete': False,
                        'template': 'arf_riflemanat_alt',
                        'team': 1,
                        'delay': 300,
                        'position': (48.052, 27.846, 336.824),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_prison_svd_1',
                        'delete': False,
                        'template': 'arf_marksman',
                        'team': 1,
                        'delay': 300,
                        'position': (56.604299999999995, 27.941200000000002, 328.432),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_prison_rpg_1',
                        'delete': False,
                        'template': 'arf_riflemanat_alt',
                        'team': 1,
                        'delay': 300,
                        'position': (47.906, 27.841, 340.426),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_prison_pkm_0',
                        'delete': False,
                        'template': 'arf_mg',
                        'team': 1,
                        'delay': 300,
                        'position': (54.81, 27.872, 344.023),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_prison_rpg_4',
                        'delete': False,
                        'template': 'arf_riflemanat_alt',
                        'team': 1,
                        'delay': 300,
                        'position': (54.703, 27.838, 340.659),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_prison_svd_0',
                        'delete': False,
                        'template': 'arf_marksman',
                        'team': 1,
                        'delay': 300,
                        'position': (63.1453, 27.9692, 326.87600000000003),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_prison_svd_4',
                        'delete': False,
                        'template': 'arf_marksman',
                        'team': 1,
                        'delay': 300,
                        'position': (56.387299999999996, 27.9432, 326.66200000000003),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_prison_pkm_2',
                        'delete': False,
                        'template': 'arf_mg',
                        'team': 1,
                        'delay': 300,
                        'position': (47.906, 27.841, 347.411),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_prison_svd_3',
                        'delete': False,
                        'template': 'arf_marksman',
                        'team': 1,
                        'delay': 300,
                        'position': (63.0383, 27.935200000000002, 330.497),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_prison_pkm_3',
                        'delete': False,
                        'template': 'arf_mg',
                        'team': 1,
                        'delay': 300,
                        'position': (54.703, 27.838, 347.644),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_prison_rpg_2',
                        'delete': False,
                        'template': 'arf_riflemanat_alt',
                        'team': 1,
                        'delay': 300,
                        'position': (54.81, 27.872, 337.038),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_prison_pkm_4',
                        'delete': False,
                        'template': 'arf_mg',
                        'team': 1,
                        'delay': 300,
                        'position': (48.052, 27.846, 343.809),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_prison_rpg_3',
                        'delete': False,
                        'template': 'arf_riflemanat_alt',
                        'team': 1,
                        'delay': 300,
                        'position': (48.269, 27.844, 338.594),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    # DELETE VCP kits
                    {
                        'name': 'cpname_ramiel_aas128_insmain_vcp_rpg_0',
                        'delete': True,
                        'template': 'arf_riflemanat_alt',
                        'team': 1,
                        'delay': 300,
                        'position': (-33.942, 25.6, -238.0),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_vcp_rpg_1',
                        'delete': True,
                        'template': 'arf_riflemanat_alt',
                        'team': 1,
                        'delay': 300,
                        'position': (-34.311, 25.6, -238.0),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_vcp_rpg_3',
                        'delete': True,
                        'template': 'arf_riflemanat_alt',
                        'team': 1,
                        'delay': 300,
                        'position': (-34.956, 25.6, -237.764),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_vcp_pkm_2',
                        'delete': True,
                        'template': 'arf_mg',
                        'team': 1,
                        'delay': 300,
                        'position': (-42.107, 25.6, -239.218),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_vcp_svd_2',
                        'delete': True,
                        'template': 'arf_marksman',
                        'team': 1,
                        'delay': 300,
                        'position': (-41.574, 25.6, -236.773),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_vcp_pkm_1',
                        'delete': True,
                        'template': 'arf_mg',
                        'team': 1,
                        'delay': 300,
                        'position': (-41.738, 25.6, -239.218),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_vcp_svd_1',
                        'delete': True,
                        'template': 'arf_marksman',
                        'team': 1,
                        'delay': 300,
                        'position': (-41.205, 25.6, -236.773),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_vcp_svd_4',
                        'delete': True,
                        'template': 'arf_marksman',
                        'team': 1,
                        'delay': 300,
                        'position': (-42.629, 25.6, -236.635),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_vcp_pkm_3',
                        'delete': True,
                        'template': 'arf_mg',
                        'team': 1,
                        'delay': 300,
                        'position': (-42.752, 25.6, -238.982),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_vcp_rpg_2',
                        'delete': True,
                        'template': 'arf_riflemanat_alt',
                        'team': 1,
                        'delay': 300,
                        'position': (-34.587, 25.6, -238.0),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_vcp_pkm_0',
                        'delete': True,
                        'template': 'arf_mg',
                        'team': 1,
                        'delay': 300,
                        'position': (-42.383, 25.6, -239.218),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_vcp_rpg_4',
                        'delete': True,
                        'template': 'arf_riflemanat_alt',
                        'team': 1,
                        'delay': 300,
                        'position': (-35.366, 25.6, -237.862),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_vcp_pkm_4',
                        'delete': True,
                        'template': 'arf_mg',
                        'team': 1,
                        'delay': 300,
                        'position': (-43.162, 25.6, -239.08),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_vcp_svd_3',
                        'delete': True,
                        'template': 'arf_marksman',
                        'team': 1,
                        'delay': 300,
                        'position': (-42.219, 25.6, -236.537),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                ],
                2: [
                    {
                        'name': 'cpname_ramiel_aas128_usmain_fob_hmmwv_0',
                        'delete': False,
                        'template': 'us_jep_hmmwv',
                        'team': 2,
                        'delay': 99999,
                        'position': (18.877, 26.000, 24.944),
                        'rotation': (0.000, 0.000, 0.000)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_usmain_fob_hmmwv_1',
                        'delete': False,
                        'template': 'us_jep_hmmwv',
                        'team': 2,
                        'delay': 99999,
                        'position': (23.291, 26.000, 24.898),
                        'rotation': (0.000, 0.000, 0.000)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_usmain_fob_hmmwv_2',
                        'delete': False,
                        'template': 'us_jep_hmmwv_mk19',
                        'team': 2,
                        'delay': 99999,
                        'position': (27.326, 26.000, 24.987),
                        'rotation': (0.000, 0.000, 0.000)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_rpg_0',
                        'delete': False,
                        'template': 'arf_riflemanat_alt',
                        'team': 1,
                        'delay': 300,
                        'position': (48.3, 25.05, 530.5),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_rpg_1',
                        'delete': False,
                        'template': 'arf_riflemanat_alt',
                        'team': 1,
                        'delay': 300,
                        'position': (49.3, 25.05, 530.5),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_rpg_2',
                        'delete': False,
                        'template': 'arf_riflemanat_alt',
                        'team': 1,
                        'delay': 300,
                        'position': (50.3, 25.05, 530.5),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_rpg_3',
                        'delete': False,
                        'template': 'arf_riflemanat_alt',
                        'team': 1,
                        'delay': 300,
                        'position': (51.3, 25.05, 530.5),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_rpg_4',
                        'delete': False,
                        'template': 'arf_riflemanat_alt',
                        'team': 1,
                        'delay': 300,
                        'position': (52.3, 25.05, 530.5),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_svd_0',
                        'delete': False,
                        'template': 'arf_marksman',
                        'team': 1,
                        'delay': 300,
                        'position': (48.3, 25.05, 534.5),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_svd_1',
                        'delete': False,
                        'template': 'arf_marksman',
                        'team': 1,
                        'delay': 300,
                        'position': (49.3, 25.05, 534.5),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_svd_2',
                        'delete': False,
                        'template': 'arf_marksman',
                        'team': 1,
                        'delay': 300,
                        'position': (50.3, 25.05, 534.5),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_svd_3',
                        'delete': False,
                        'template': 'arf_marksman',
                        'team': 1,
                        'delay': 300,
                        'position': (51.3, 25.05, 534.5),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_svd_4',
                        'delete': False,
                        'template': 'arf_marksman',
                        'team': 1,
                        'delay': 300,
                        'position': (52.3, 25.05, 534.5),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_pkm_0',
                        'delete': False,
                        'template': 'arf_mg',
                        'team': 1,
                        'delay': 300,
                        'position': (48.3, 25.05, 527.5),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_pkm_1',
                        'delete': False,
                        'template': 'arf_mg',
                        'team': 1,
                        'delay': 300,
                        'position': (49.3, 25.05, 527.5),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_pkm_2',
                        'delete': False,
                        'template': 'arf_mg',
                        'team': 1,
                        'delay': 300,
                        'position': (50.3, 25.05, 527.5),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_pkm_3',
                        'delete': False,
                        'template': 'arf_mg',
                        'team': 1,
                        'delay': 300,
                        'position': (51.3, 25.05, 527.5),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_pkm_4',
                        'delete': False,
                        'template': 'arf_mg',
                        'team': 1,
                        'delay': 300,
                        'position': (52.3, 25.05, 527.5),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    # DELETE FOB KITS
                    {
                        'name': 'cpname_ramiel_aas128_insmain_fob_pkm_1',
                        'delete': True,
                        'template': 'arf_mg',
                        'team': 1,
                        'delay': 300,
                        'position': (45.475, 25.135, 53.647),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_fob_rpg_0',
                        'delete': True,
                        'template': 'arf_riflemanat_alt',
                        'team': 1,
                        'delay': 300,
                        'position': (52.531, 25.135, 53.814),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_fob_pkm_2',
                        'delete': True,
                        'template': 'arf_mg',
                        'team': 1,
                        'delay': 300,
                        'position': (45.751, 25.135, 53.647),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_fob_svd_3',
                        'delete': True,
                        'template': 'arf_marksman',
                        'team': 1,
                        'delay': 300,
                        'position': (36.924, 25.135, 53.842),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_fob_svd_1',
                        'delete': True,
                        'template': 'arf_marksman',
                        'team': 1,
                        'delay': 300,
                        'position': (37.293, 25.135, 53.606),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_fob_svd_2',
                        'delete': True,
                        'template': 'arf_marksman',
                        'team': 1,
                        'delay': 300,
                        'position': (37.569, 25.135, 53.606),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_fob_pkm_4',
                        'delete': True,
                        'template': 'arf_mg',
                        'team': 1,
                        'delay': 300,
                        'position': (44.696, 25.135, 53.785),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_fob_rpg_2',
                        'delete': True,
                        'template': 'arf_riflemanat_alt',
                        'team': 1,
                        'delay': 300,
                        'position': (53.31, 25.135, 53.676),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_fob_svd_4',
                        'delete': True,
                        'template': 'arf_marksman',
                        'team': 1,
                        'delay': 300,
                        'position': (36.514, 25.135, 53.744),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_fob_rpg_3',
                        'delete': True,
                        'template': 'arf_riflemanat_alt',
                        'team': 1,
                        'delay': 300,
                        'position': (53.586, 25.135, 53.676),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_fob_pkm_0',
                        'delete': True,
                        'template': 'arf_mg',
                        'team': 1,
                        'delay': 300,
                        'position': (46.12, 25.135, 53.647),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_fob_rpg_1',
                        'delete': True,
                        'template': 'arf_riflemanat_alt',
                        'team': 1,
                        'delay': 300,
                        'position': (52.941, 25.135, 53.912),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_fob_pkm_3',
                        'delete': True,
                        'template': 'arf_mg',
                        'team': 1,
                        'delay': 300,
                        'position': (45.106, 25.135, 53.883),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_fob_rpg_4',
                        'delete': True,
                        'template': 'arf_riflemanat_alt',
                        'team': 1,
                        'delay': 300,
                        'position': (53.955, 25.135, 53.676),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_insmain_fob_svd_0',
                        'delete': True,
                        'template': 'arf_marksman',
                        'team': 1,
                        'delay': 300,
                        'position': (37.938, 25.135, 53.606),
                        'rotation': (0.0, 0.0, 0.0)
                    },
                ],
                3: [
                    {
                        'name': 'cpname_ramiel_aas128_usmain_prison_crate_0',
                        'delete': False,
                        'template': 'fixed_supply_crate_us',
                        'team': 2,
                        'delay': 60,
                        'position': (18.877, 26.000, 24.944),
                        'rotation': (0.000, 0.000, 0.000)
                    },
                    {
                        'name': 'cpname_ramiel_aas128_usmain_prison_hmmwv_0',
                        'delete': False,
                        'template': 'us_jep_hmmwv',
                        'team': 2,
                        'delay': 99999,
                        'position': (23.291, 26.000, 24.898),
                        'rotation': (0.000, 0.000, 0.000)
                    },
                ],
            }
        }
    }
}

MAP_SPAWNERS = {
    'ramiel': {
        'gpm_cq': {
            128: [
                # US default fob and crate
                {
                    'name': 'cpname_ramiel_aas128_usmain_fixed_fob_0',
                    'delete': False,
                    'template': 'fixed_firebase',
                    'team': 2,
                    'delay': 600,
                    'position': (-652.177, 25.726, -681.075),
                    'rotation': (0.000, 0.000, 0.000)
                },
                {
                    'name': 'cpname_ramiel_aas128_usmain_crate_0',
                    'delete': False,
                    'template': 'fixed_supply_crate_us',
                    'team': 2,
                    'delay': 60,
                    'position': (-639.591, 26.000, -670.966),
                    'rotation': (0.000, 0.000, 0.000)
                },
                # US grenadiers
                {
                    'name': 'cpname_ramiel_aas128_usmain_assault_0',
                    'delete': False,
                    'template': 'usa_assault_alt',
                    'team': 2,
                    'delay': 300,
                    'position': (-637.654, 24.922, -666.264),
                    'rotation': (0.000, 0.000, 0.000)
                },
                {
                    'name': 'cpname_ramiel_aas128_usmain_assault_1',
                    'delete': False,
                    'template': 'usa_assault_alt',
                    'team': 2,
                    'delay': 300,
                    'position': (-637.664, 24.962, -668.867),
                    'rotation': (0.000, 0.000, 0.000)
                },
                # US default spawns
                {
                    'name': 'cpname_ramiel_aas128_usmain_hmmwv_0',
                    'delete': False,
                    'template': 'us_jep_hmmwv',
                    'team': 2,
                    'delay': 600,
                    'position': (-669.291, 26.000, -655.993),
                    'rotation': (0.000, 0.000, 0.000)
                },
                {
                    'name': 'cpname_ramiel_aas128_usmain_hmmwv_1',
                    'delete': False,
                    'template': 'us_jep_hmmwv',
                    'team': 2,
                    'delay': 600,
                    'position': (-640.339, 26.000, -648.535),
                    'rotation': (0.000, 0.000, 0.000)
                },
                {
                    'name': 'cpname_ramiel_aas128_usmain_hmmwv_2',
                    'delete': False,
                    'template': 'us_jep_hmmwv',
                    'team': 2,
                    'delay': 600,
                    'position': (-643.765, 26.000, -648.608),
                    'rotation': (0.000, 0.000, 0.000)
                },
                {
                    'name': 'cpname_ramiel_aas128_usmain_hmmwv_3',
                    'delete': False,
                    'template': 'us_jep_hmmwv',
                    'team': 2,
                    'delay': 600,
                    'position': (-647.249, 26.000, -655.122),
                    'rotation': (0.000, 0.000, 0.000)
                },
                {
                    'name': 'cpname_ramiel_aas128_usmain_hmmwv_4',
                    'delete': False,
                    'template': 'us_jep_hmmwv',
                    'team': 2,
                    'delay': 600,
                    'position': (-647.297, 26.000, -648.665),
                    'rotation': (0.000, 0.000, 0.000)
                },
                {
                    'name': 'cpname_ramiel_aas128_usmain_hmmwv_5',
                    'delete': False,
                    'template': 'us_jep_hmmwv',
                    'team': 2,
                    'delay': 600,
                    'position': (-651.151, 26.000, -648.747),
                    'rotation': (0.000, 0.000, 0.000)
                },
                {
                    'name': 'cpname_ramiel_aas128_usmain_hmmwv_6',
                    'delete': False,
                    'template': 'us_jep_hmmwv',
                    'team': 2,
                    'delay': 600,
                    'position': (-653.719, 26.000, -655.258),
                    'rotation': (0.000, 0.000, 0.000)
                },
                {
                    'name': 'cpname_ramiel_aas128_usmain_hmmwv_7',
                    'delete': False,
                    'template': 'us_jep_hmmwv',
                    'team': 2,
                    'delay': 600,
                    'position': (-659.606, 26.000, -655.333),
                    'rotation': (0.000, 0.000, 0.000)
                },
                {
                    'name': 'cpname_ramiel_aas128_usmain_hmmwv_8',
                    'delete': False,
                    'template': 'us_jep_hmmwv',
                    'team': 2,
                    'delay': 600,
                    'position': (-662.583, 26.000, -649.083),
                    'rotation': (0.000, 0.000, 0.000)
                },
                {
                    'name': 'cpname_ramiel_aas128_usmain_hmmwv_9',
                    'delete': False,
                    'template': 'us_jep_hmmwv',
                    'team': 2,
                    'delay': 600,
                    'position': (-656.599, 26.000, -648.798),
                    'rotation': (0.000, 0.000, 0.000)
                },
                {
                    'name': 'cpname_ramiel_aas128_usmain_hmmwv_mk19_0',
                    'delete': False,
                    'template': 'us_jep_hmmwv_uparmored_mk19',
                    'team': 2,
                    'delay': 600,
                    'position': (-628.403, 26.000, -633.676),
                    'rotation': (0.000, 0.000, 0.000)
                },
                {
                    'name': 'cpname_ramiel_aas128_usmain_hmmwv_mk19_1',
                    'delete': False,
                    'template': 'us_jep_hmmwv_uparmored_mk19',
                    'team': 2,
                    'delay': 600,
                    'position': (-624.692, 26.000, -633.736),
                    'rotation': (0.000, 0.000, 0.000)
                },
                # ARF supply
                {
                    'name': 'cpname_ramiel_aas128_insmain_vehicle_depot',
                    'delete': False,
                    'template': 'vehicle_depot_tal',
                    'team': 1,
                    'delay': 99999,
                    'position': (93.024, 25.000, 523.416),
                    'rotation': (0.000, 0.000, 0.000)
                },
                # ARF default spawns
                {
                    'name': 'arf_main_atm1',
                    'delete': False,
                    'template': 'civ_atm_technical',
                    'team': 1,
                    'delay': 300,
                    'position': (40.809, 26, 523.824),
                    'rotation': (180.000, 0.000, 0.000)
                },
                {
                    'name': 'arf_main_atm2',
                    'delete': False,
                    'template': 'civ_atm_technical',
                    'team': 1,
                    'delay': 300,
                    'position': (46.8542, 26, 523.824),
                    'rotation': (180.000, 0.000, 0.000)
                },
                {
                    'name': 'arf_main_uralzu23_1',
                    'delete': False,
                    'template': 'civ_aav_uralzu232',
                    'team': 1,
                    'delay': 300,
                    'position': (97.3817, 26, 513.75),
                    'rotation': (180.000, 0.000, 0.000)
                },
                {
                    'name': 'arf_main_uralzu23_2',
                    'delete': False,
                    'template': 'civ_aav_uralzu232',
                    'team': 1,
                    'delay': 300,
                    'position': (92.2107, 26, 513.75),
                    'rotation': (180.000, 0.000, 0.000)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_jep_support_logistics_0',
                    'delete': False,
                    'template': 'civ_jep_support_logistics',
                    'team': 1,
                    'delay': 300,
                    'position': (63.940, 26.000, 511.311),
                    'rotation': (180.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_jep_support_logistics_1',
                    'delete': False,
                    'template': 'civ_jep_support_logistics',
                    'team': 1,
                    'delay': 300,
                    'position': (67.509, 26.000, 511.216),
                    'rotation': (180.000, 0.000, 0.000)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_jep_techie_0',
                    'delete': False,
                    'template': 'civ_jep_technical',
                    'team': 1,
                    'delay': 300,
                    'position': (98.847, 26.000, 475.585),
                    'rotation': (-90.000, 0.000, 0.000)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_jep_techie_1',
                    'delete': False,
                    'template': 'civ_jep_technical_red',
                    'team': 1,
                    'delay': 300,
                    'position': (98.959, 26.000, 472.628),
                    'rotation': (-90.000, 0.000, 0.000)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_jep_techie_2',
                    'delete': False,
                    'template': 'civ_jep_technical',
                    'team': 1,
                    'delay': 300,
                    'position': (46.829, 26.000, 471.489),
                    'rotation': (90.000, 0.000, 0.000)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_jep_techie_3',
                    'delete': False,
                    'template': 'civ_jep_technical_red',
                    'team': 1,
                    'delay': 300,
                    'position': (46.823, 26.000, 474.435),
                    'rotation': (90.000, 0.000, 0.000)
                },
                # ARF kits weapons
                {
                    'name': 'cpname_ramiel_aas128_insmain_vcp_rpg_0',
                    'delete': False,
                    'template': 'arf_riflemanat_alt',
                    'team': 1,
                    'delay': 300,
                    'position': (-33.942, 25.6, -238.0),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_vcp_rpg_1',
                    'delete': False,
                    'template': 'arf_riflemanat_alt',
                    'team': 1,
                    'delay': 300,
                    'position': (-34.311, 25.6, -238.0),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_vcp_rpg_3',
                    'delete': False,
                    'template': 'arf_riflemanat_alt',
                    'team': 1,
                    'delay': 300,
                    'position': (-34.956, 25.6, -237.764),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_vcp_pkm_2',
                    'delete': False,
                    'template': 'arf_mg',
                    'team': 1,
                    'delay': 300,
                    'position': (-42.107, 25.6, -239.218),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_vcp_svd_2',
                    'delete': False,
                    'template': 'arf_marksman',
                    'team': 1,
                    'delay': 300,
                    'position': (-41.574, 25.6, -236.773),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_vcp_pkm_1',
                    'delete': False,
                    'template': 'arf_mg',
                    'team': 1,
                    'delay': 300,
                    'position': (-41.738, 25.6, -239.218),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_vcp_svd_1',
                    'delete': False,
                    'template': 'arf_marksman',
                    'team': 1,
                    'delay': 300,
                    'position': (-41.205, 25.6, -236.773),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_vcp_svd_4',
                    'delete': False,
                    'template': 'arf_marksman',
                    'team': 1,
                    'delay': 300,
                    'position': (-42.629, 25.6, -236.635),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_vcp_pkm_3',
                    'delete': False,
                    'template': 'arf_mg',
                    'team': 1,
                    'delay': 300,
                    'position': (-42.752, 25.6, -238.982),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_vcp_rpg_2',
                    'delete': False,
                    'template': 'arf_riflemanat_alt',
                    'team': 1,
                    'delay': 300,
                    'position': (-34.587, 25.6, -238.0),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_vcp_pkm_0',
                    'delete': False,
                    'template': 'arf_mg',
                    'team': 1,
                    'delay': 300,
                    'position': (-42.383, 25.6, -239.218),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_vcp_rpg_4',
                    'delete': False,
                    'template': 'arf_riflemanat_alt',
                    'team': 1,
                    'delay': 300,
                    'position': (-35.366, 25.6, -237.862),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_vcp_pkm_4',
                    'delete': False,
                    'template': 'arf_mg',
                    'team': 1,
                    'delay': 300,
                    'position': (-43.162, 25.6, -239.08),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_vcp_svd_3',
                    'delete': False,
                    'template': 'arf_marksman',
                    'team': 1,
                    'delay': 300,
                    'position': (-42.219, 25.6, -236.537),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_vcp_svd_0',
                    'delete': False,
                    'template': 'arf_marksman',
                    'team': 1,
                    'delay': 300,
                    'position': (-41.85, 25.6, -236.773),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_fob_pkm_1',
                    'delete': False,
                    'template': 'arf_mg',
                    'team': 1,
                    'delay': 300,
                    'position': (45.475, 25.135, 53.647),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_fob_rpg_0',
                    'delete': False,
                    'template': 'arf_riflemanat_alt',
                    'team': 1,
                    'delay': 300,
                    'position': (52.531, 25.135, 53.814),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_fob_pkm_2',
                    'delete': False,
                    'template': 'arf_mg',
                    'team': 1,
                    'delay': 300,
                    'position': (45.751, 25.135, 53.647),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_fob_svd_3',
                    'delete': False,
                    'template': 'arf_marksman',
                    'team': 1,
                    'delay': 300,
                    'position': (36.924, 25.135, 53.842),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_fob_svd_1',
                    'delete': False,
                    'template': 'arf_marksman',
                    'team': 1,
                    'delay': 300,
                    'position': (37.293, 25.135, 53.606),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_fob_svd_2',
                    'delete': False,
                    'template': 'arf_marksman',
                    'team': 1,
                    'delay': 300,
                    'position': (37.569, 25.135, 53.606),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_fob_pkm_4',
                    'delete': False,
                    'template': 'arf_mg',
                    'team': 1,
                    'delay': 300,
                    'position': (44.696, 25.135, 53.785),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_fob_rpg_2',
                    'delete': False,
                    'template': 'arf_riflemanat_alt',
                    'team': 1,
                    'delay': 300,
                    'position': (53.31, 25.135, 53.676),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_fob_svd_4',
                    'delete': False,
                    'template': 'arf_marksman',
                    'team': 1,
                    'delay': 300,
                    'position': (36.514, 25.135, 53.744),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_fob_rpg_3',
                    'delete': False,
                    'template': 'arf_riflemanat_alt',
                    'team': 1,
                    'delay': 300,
                    'position': (53.586, 25.135, 53.676),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_fob_pkm_0',
                    'delete': False,
                    'template': 'arf_mg',
                    'team': 1,
                    'delay': 300,
                    'position': (46.12, 25.135, 53.647),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_fob_rpg_1',
                    'delete': False,
                    'template': 'arf_riflemanat_alt',
                    'team': 1,
                    'delay': 300,
                    'position': (52.941, 25.135, 53.912),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_fob_pkm_3',
                    'delete': False,
                    'template': 'arf_mg',
                    'team': 1,
                    'delay': 300,
                    'position': (45.106, 25.135, 53.883),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_fob_rpg_4',
                    'delete': False,
                    'template': 'arf_riflemanat_alt',
                    'team': 1,
                    'delay': 300,
                    'position': (53.955, 25.135, 53.676),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_insmain_fob_svd_0',
                    'delete': False,
                    'template': 'arf_marksman',
                    'team': 1,
                    'delay': 300,
                    'position': (37.938, 25.135, 53.606),
                    'rotation': (0.0, 0.0, 0.0)
                },
                # Default spawners, deleting
                {
                    'name': 'cpname_ramiel_aas128_habr_gidr_hq_acv',
                    'delete': True,
                    'template': 'arf_acv_technical',
                    'team': 1,
                    'delay': 30,
                    'position': (-434.807, 25.561, 585.825),
                    'rotation': (90.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_160th_jeep2',
                    'delete': True,
                    'template': 'us_jep_hmmwv',
                    'team': 2,
                    'delay': 600,
                    'position': (-681.662, 24.922, -663.341),
                    'rotation': (18.774, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_10th_apc2',
                    'delete': True,
                    'template': 'fr_apc_vbci',
                    'team': 2,
                    'delay': 99999,
                    'position': (-663.333, 25.0, -606.06),
                    'rotation': (48.766, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_160th_crate',
                    'delete': True,
                    'template': 'fixed_supply_crate_us',
                    'team': 2,
                    'delay': 10,
                    'position': (-556.409, 25.0, -656.401),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_crew5_ammo',
                    'delete': True,
                    'template': 'ammocache',
                    'team': 1,
                    'delay': 99999,
                    'position': (-510.286, 29.28, 188.861),
                    'rotation': (90.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_habr_gidr_hq_ammo1',
                    'delete': True,
                    'template': 'ammocache',
                    'team': 1,
                    'delay': 99999,
                    'position': (83.105, 25.0, 492.553),
                    'rotation': (90.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_crew3_ammo',
                    'delete': True,
                    'template': 'ammocache',
                    'team': 1,
                    'delay': 99999,
                    'position': (-798.903, 29.281, 753.191),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_mosque2_rally',
                    'delete': True,
                    'template': 'rallypoint_arf_placeable',
                    'team': 1,
                    'delay': 99999,
                    'position': (-357.975, 25.0, 420.629),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_mosque1_rally',
                    'delete': True,
                    'template': 'rallypoint_arf_placeable',
                    'team': 1,
                    'delay': 99999,
                    'position': (251.686, 33.78, 348.532),
                    'rotation': (84.279, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_habr_gidr_hq_spawn',
                    'delete': True,
                    'template': 'rallypoint_arf_placeable',
                    'team': 1,
                    'delay': 99999,
                    'position': (-35.399, 25.0, 228.185),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_habr_gidr_hq_ammo5',
                    'delete': True,
                    'template': 'ammocache',
                    'team': 1,
                    'delay': 99999,
                    'position': (80.379, 30.975, 808.549),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_habr_gidr_hq_jeep6',
                    'delete': True,
                    'template': 'civ_jep_car',
                    'team': 1,
                    'delay': 300,
                    'position': (-426.699, 25.0, 609.527),
                    'rotation': (-180.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_crew7_ammo',
                    'delete': True,
                    'template': 'ammocache',
                    'team': 1,
                    'delay': 99999,
                    'position': (-227.732, 28.569, 349.682),
                    'rotation': (-135.306, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_usmain_helo1',
                    'delete': True,
                    'template': 'us_the_mh6',
                    'team': 2,
                    'delay': 300,
                    'position': (-328.938, 25.0, -636.964),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_habr_gidr_hq_mortar3',
                    'delete': True,
                    'template': 'mortar_team1',
                    'team': 1,
                    'delay': 1200,
                    'position': (-568.174, 24.96, 2562.838),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_habr_gidr_hq_bike3',
                    'delete': True,
                    'template': 'civ_bik_dirtbike',
                    'team': 1,
                    'delay': 300,
                    'position': (-501.962, 25.0, 611.714),
                    'rotation': (29.476, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_160th_tank',
                    'delete': True,
                    'template': 'fr_apc_vab',
                    'team': 2,
                    'delay': 99999,
                    'position': (-685.489, 25.0, -628.714),
                    'rotation': (46.872, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_habr_gidr_hq_jeep3',
                    'delete': True,
                    'template': 'civ_aav_uralzu232',
                    'team': 1,
                    'delay': 600,
                    'position': (-491.092, 25.0, 578.76),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_crew8_ammo',
                    'delete': True,
                    'template': 'ammocache',
                    'team': 1,
                    'delay': 99999,
                    'position': (-503.754, 29.429, 252.449),
                    'rotation': (90.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_city5_rally',
                    'delete': True,
                    'template': 'rallypoint_arf_placeable',
                    'team': 1,
                    'delay': 99999,
                    'position': (-945.856, 25.03, 410.563),
                    'rotation': (101.712, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_160th_helo7_0',
                    'delete': True,
                    'template': 'us_the_uh60_soar',
                    'team': 2,
                    'delay': 300,
                    'position': (-580.718, 25.0, -670.87),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_10th_jeep5',
                    'delete': True,
                    'template': 'us_jep_hmmwv',
                    'team': 2,
                    'delay': 600,
                    'position': (-702.703, 24.922, -663.557),
                    'rotation': (20.24, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_crew10_jeep1',
                    'delete': True,
                    'template': 'us_jep_hmmwv',
                    'team': 2,
                    'delay': 99999,
                    'position': (30.726, 25.0, 432.36),
                    'rotation': (96.038, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_160th_acv',
                    'delete': True,
                    'template': 'us_acv_stryker',
                    'team': 2,
                    'delay': 1,
                    'position': (-508.864, 25.58, -647.829),
                    'rotation': (-180.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_habr_gidr_hq_bike4',
                    'delete': True,
                    'template': 'civ_bik_dirtbike',
                    'team': 1,
                    'delay': 300,
                    'position': (-501.801, 25.0, 615.612),
                    'rotation': (30.191, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_habr_gidr_hq_repairdepot',
                    'delete': True,
                    'template': 'vehicle_depot_tal',
                    'team': 1,
                    'delay': 1,
                    'position': (-478.798, 25.0, 622.616),
                    'rotation': (90.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_city2_ammo',
                    'delete': True,
                    'template': 'ammocache',
                    'team': 1,
                    'delay': 99999,
                    'position': (779.942, 21.458, -305.615),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_city4_car',
                    'delete': True,
                    'template': 'civ_jep_car_blue',
                    'team': 1,
                    'delay': 300,
                    'position': (82.879, 30.975, 829.592),
                    'rotation': (-111.847, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_deltaforce_crate2',
                    'delete': True,
                    'template': 'fixed_supply_crate_us',
                    'team': 2,
                    'delay': 10,
                    'position': (-300.174, 25.0, -653.157),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_10th_jeep4',
                    'delete': True,
                    'template': 'us_jep_hmmwv',
                    'team': 2,
                    'delay': 600,
                    'position': (-697.435, 24.922, -663.476),
                    'rotation': (20.586, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_habr_gidr_hq_jeep5',
                    'delete': True,
                    'template': 'civ_jep_car_black',
                    'team': 1,
                    'delay': 300,
                    'position': (-430.824, 25.0, 608.847),
                    'rotation': (162.17, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_habr_gidr_hq_bike1',
                    'delete': True,
                    'template': 'civ_bik_dirtbike',
                    'team': 1,
                    'delay': 300,
                    'position': (-493.819, 25.0, 578.803),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_habr_gidr_hq_mortar2',
                    'delete': True,
                    'template': 'mortar_team1',
                    'team': 1,
                    'delay': 1200,
                    'position': (-782.23, 24.96, 2631.58),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_blackhawk2_spawn2',
                    'delete': True,
                    'template': 'rallypoint_arf_placeable',
                    'team': 1,
                    'delay': 99999,
                    'position': (-32.843, 25.019, 249.076),
                    'rotation': (-178.489, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_habr_gidr_hq_ammo1_0',
                    'delete': True,
                    'template': 'ammocache',
                    'team': 1,
                    'delay': 10,
                    'position': (-456.467, 25.0, 583.509),
                    'rotation': (180.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_160th_helo3',
                    'delete': True,
                    'template': 'us_the_uh60_soar',
                    'team': 2,
                    'delay': 300,
                    'position': (-599.177, 25.0, -669.998),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_habr_gidr_hq_ammo2_0',
                    'delete': True,
                    'template': 'ammocache',
                    'team': 1,
                    'delay': 10,
                    'position': (-464.483, 25.0, 620.703),
                    'rotation': (-90.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_10th_crate2',
                    'delete': True,
                    'template': 'fixed_supply_crate_us',
                    'team': 2,
                    'delay': 10,
                    'position': (-689.634, 24.922, -680.999),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_crew12_jeep3',
                    'delete': True,
                    'template': 'us_jep_hmmwv_uparmored_mk19',
                    'team': 2,
                    'delay': 99999,
                    'position': (36.438, 25.0, 435.326),
                    'rotation': (86.533, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_deltaforce_crate',
                    'delete': True,
                    'template': 'fixed_supply_crate_us',
                    'team': 2,
                    'delay': 10,
                    'position': (-364.004, 25.0, -643.047),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_160th_jeep3',
                    'delete': True,
                    'template': 'us_jep_hmmwv',
                    'team': 2,
                    'delay': 600,
                    'position': (-687.256, 24.922, -663.52),
                    'rotation': (21.355, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_160th_depot',
                    'delete': True,
                    'template': 'vehicle_depot_us',
                    'team': 2,
                    'delay': 30,
                    'position': (-719.592, 25.0, -585.962),
                    'rotation': (-90.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_city5_ammo',
                    'delete': True,
                    'template': 'ammocache',
                    'team': 1,
                    'delay': 99999,
                    'position': (-937.971, 25.185, 408.474),
                    'rotation': (41.886, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_10th_crate',
                    'delete': True,
                    'template': 'fixed_supply_crate_us',
                    'team': 2,
                    'delay': 10,
                    'position': (-727.645, 25.0, -665.829),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_usmain_helo6',
                    'delete': True,
                    'template': 'us_the_mh6',
                    'team': 2,
                    'delay': 300,
                    'position': (-310.522, 25.0, -636.971),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_crew12_cache',
                    'delete': True,
                    'template': 'fixed_supply_crate_us',
                    'team': 2,
                    'delay': 99999,
                    'position': (51.709, 25.01, 440.336),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_crew14_ammo',
                    'delete': True,
                    'template': 'ammocache',
                    'team': 1,
                    'delay': 99999,
                    'position': (-160.681, 33.391, 414.344),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_crew4_ammo',
                    'delete': True,
                    'template': 'ammocache',
                    'team': 1,
                    'delay': 99999,
                    'position': (-902.315, 33.421, 665.834),
                    'rotation': (-180.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_habr_gidr_hq_spg',
                    'delete': True,
                    'template': 'civ_atm_technical',
                    'team': 1,
                    'delay': 99999,
                    'position': (-421.085, 25.0, 596.528),
                    'rotation': (83.425, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_10th_apc1',
                    'delete': True,
                    'template': 'fr_apc_vbci',
                    'team': 2,
                    'delay': 99999,
                    'position': (-675.288, 25.0, -617.879),
                    'rotation': (46.872, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_crew11_jeep1',
                    'delete': True,
                    'template': 'us_jep_hmmwv',
                    'team': 2,
                    'delay': 99999,
                    'position': (44.634, 25.0, 434.05),
                    'rotation': (86.533, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_habr_gidr_hq_bike2',
                    'delete': True,
                    'template': 'civ_bik_dirtbike',
                    'team': 1,
                    'delay': 300,
                    'position': (-502.288, 25.0, 607.706),
                    'rotation': (32.479, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_crew11_cache',
                    'delete': True,
                    'template': 'fixed_supply_crate_us',
                    'team': 2,
                    'delay': 99999,
                    'position': (-88.748, 29.113, 106.099),
                    'rotation': (90.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_crew1_ammo',
                    'delete': True,
                    'template': 'ammocache',
                    'team': 1,
                    'delay': 99999,
                    'position': (-730.793, 33.391, 512.536),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_habr_gidr_hq_mortar1',
                    'delete': True,
                    'template': 'mortar_team1',
                    'team': 1,
                    'delay': 1200,
                    'position': (-622.97, 24.96, 2686.124),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_habr_gidr_hq_ammo2',
                    'delete': True,
                    'template': 'ammocache',
                    'team': 1,
                    'delay': 99999,
                    'position': (-30.164, 25.0, 236.698),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_mosque2_crate',
                    'delete': True,
                    'template': 'ammocache',
                    'team': 1,
                    'delay': 10,
                    'position': (-373.231, 25.218, 432.545),
                    'rotation': (-180.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_city2_car',
                    'delete': True,
                    'template': 'civ_jep_car',
                    'team': 1,
                    'delay': 300,
                    'position': (776.414, 21.458, -286.483),
                    'rotation': (154.332, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_160th_jeep1',
                    'delete': True,
                    'template': 'us_jep_hmmwv_mk19',
                    'team': 2,
                    'delay': 600,
                    'position': (-692.033, 24.922, -663.698),
                    'rotation': (18.848, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_crew2_ammo',
                    'delete': True,
                    'template': 'ammocache',
                    'team': 1,
                    'delay': 99999,
                    'position': (-666.689, 29.328, 732.089),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_crew15_ammo',
                    'delete': True,
                    'template': 'ammocache',
                    'team': 1,
                    'delay': 99999,
                    'position': (-624.837, 25.127, 445.746),
                    'rotation': (-90.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_habr_gidr_hq_mortar4',
                    'delete': True,
                    'template': 'mortar_team1',
                    'team': 1,
                    'delay': 1200,
                    'position': (-671.26, 24.96, 2647.892),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_habr_gidr_hq_jeep1',
                    'delete': True,
                    'template': 'civ_jep_support_logistics',
                    'team': 1,
                    'delay': 300,
                    'position': (-477.833, 25.0, 596.384),
                    'rotation': (-92.085, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_habr_gidr_hq_spawn3',
                    'delete': True,
                    'template': 'rallypoint_arf_placeable',
                    'team': 1,
                    'delay': 99999,
                    'position': (86.624, 30.975, 816.29),
                    'rotation': (-153.243, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_mosque1_crate',
                    'delete': True,
                    'template': 'ammocache',
                    'team': 1,
                    'delay': 10,
                    'position': (254.13, 33.843, 362.261),
                    'rotation': (-180.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_habr_gidr_hq_jeep4',
                    'delete': True,
                    'template': 'civ_jep_technical',
                    'team': 1,
                    'delay': 600,
                    'position': (-501.637, 25.0, 578.395),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_mosque1_rally2',
                    'delete': True,
                    'template': 'rallypoint_arf_placeable',
                    'team': 1,
                    'delay': 99999,
                    'position': (288.171, 33.78, 358.014),
                    'rotation': (-90.857, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_city5_ins_jeep_3',
                    'delete': True,
                    'template': 'civ_jep_car_blue',
                    'team': 1,
                    'delay': 300,
                    'position': (-951.654, 25.03, 397.547),
                    'rotation': (-90.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_usmain_helo5',
                    'delete': True,
                    'template': 'us_the_mh6',
                    'team': 2,
                    'delay': 99999,
                    'position': (-274.838, 25.0, -637.14),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_usmain_helo4',
                    'delete': True,
                    'template': 'us_ahe_ah6',
                    'team': 2,
                    'delay': 1200,
                    'position': (-257.087, 25.0, -636.708),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_habr_gidr_hq_jeep2',
                    'delete': True,
                    'template': 'civ_jep_technical_red',
                    'team': 1,
                    'delay': 600,
                    'position': (-484.515, 25.0, 578.685),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_160th_helo7',
                    'delete': True,
                    'template': 'us_ahe_ah6',
                    'team': 2,
                    'delay': 1200,
                    'position': (-239.338, 25.0, -636.895),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_crew13_ammo',
                    'delete': True,
                    'template': 'ammocache',
                    'team': 1,
                    'delay': 99999,
                    'position': (-99.253, 25.02, 573.245),
                    'rotation': (0.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_habr_gidr_hq_jeep7',
                    'delete': True,
                    'template': 'civ_jep_technical',
                    'team': 1,
                    'delay': 600,
                    'position': (-422.238, 25.0, 609.841),
                    'rotation': (-180.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_10th_logi',
                    'delete': True,
                    'template': 'us_trk_logistics',
                    'team': 2,
                    'delay': 300,
                    'position': (-716.998, 25.0, -577.791),
                    'rotation': (90.987, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_crew6_ammo',
                    'delete': True,
                    'template': 'ammocache',
                    'team': 1,
                    'delay': 99999,
                    'position': (-254.281, 33.391, 199.754),
                    'rotation': (-90.0, 0.0, 0.0)
                },
                {
                    'name': 'cpname_ramiel_aas128_habr_gidr_hq_spawn4',
                    'delete': True,
                    'template': 'rallypoint_arf_placeable',
                    'team': 1,
                    'delay': 99999,
                    'position': (82.942, 25.0, 508.928),
                    'rotation': (-156.886, 0.0, 0.0)
                },
            ]
        }
    },
}

MAP_FLAGS = {
    'ramiel': {
        'gpm_cq': {
            128: {
                'cpname_ramiel_aas128_habr_gidr_hq': {
                    'position' : (67.3558, 20.0, 525.785),
                    'delete' : False,
                    'team' : 0,
                },
                'cpname_ramiel_aas128_blackhawk1': {
                    'delete' : False,
                    'team' : 1,
                },
                'cpname_ramiel_aas128_blackhawk2': {
                    'delete' : True,
                },
                'cpname_ramiel_aas128_160th': {
                    'delete' : True,
                },
                'cpname_ramiel_aas128_deltaforce': {
                    'delete' : True,
                },
                'cpname_ramiel_aas128_10th': {
                    'delete' : False,
                },
                'cpname_ramiel_aas128_mosque1': {
                    'delete' : True,
                },
                'cpname_ramiel_aas128_mosque2': {
                    'delete' : True,
                },
                'cpname_ramiel_aas128_city2': {
                    'delete' : True,
                },
                'cpname_ramiel_aas128_extraction': {
                    'delete' : True,
                },
                'cpname_ramiel_aas128_crew1': {
                    'delete' : True,
                },
                'cpname_ramiel_aas128_crew2': {
                    'delete' : True,
                },
                'cpname_ramiel_aas128_crew3': {
                    'delete' : True,
                },
                'cpname_ramiel_aas128_crew4': {
                    'delete' : True,
                },
                'cpname_ramiel_aas128_crew5': {
                    'delete' : True,
                },
                'cpname_ramiel_aas128_crew6': {
                    'delete' : True,
                },
                'cpname_ramiel_aas128_crew7': {
                    'delete' : True,
                },
                'cpname_ramiel_aas128_crew8': {
                    'delete' : True,
                },
                'cpname_ramiel_aas128_crew11': {
                    'delete' : True,
                },
                'cpname_ramiel_aas128_crew13': {
                    'delete' : True,
                },
                'cpname_ramiel_aas128_crew14': {
                    'delete' : True,
                },
                'cpname_ramiel_aas128_crew15': {
                    'delete' : True,
                },
                'cpname_ramiel_aas128_convoy': {
                    'delete' : True,
                },
            }
        }
    }
}

MAP_DODS = {
    'ramiel': {
        'gpm_cq': {
            128: {
                'CombatArea_34_Event': {
                    'name': 'CombatArea_34_Event',
                    'create': True,
                    'delete': False,
                    'modify': False,
                    'team': 0,
                    'vehicles': 4,
                    'layer': 7,
                    'inverted': 1,  # lets see if we can create new one and invert
                    'areapoints': [
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
                'CombatArea_36_Preparation': {
                    'name': 'CombatArea_36_Preparation',
                    'create': True,  # for testing enale
                    'modify': False,
                    'delete': False,
                    'team': 0,
                    'vehicles': 4,
                    'layer': 7,
                    'inverted': 1,
                    'delayed' : True,
                    'areapoints': [
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
