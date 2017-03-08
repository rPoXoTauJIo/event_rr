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
    ('bamyan', 'gpm_cq', 32),
    ]


# Define spawners that will be spawned or deleted from start
# Spawner settings:
#   'name' : string: name of spawner, should be unique,
#   'template' : string: template name for spawner template,
#   'delete' : boolean: if spawner should be deleted,
#   'team' : integer: spawner team,
#   'delay' : integer: spawn delay,
#   'position' : vec3: spawner position,
#   'rotation' : vec3: spawner rotation
MAP_SPAWNERS = {
    'bamyan' : {
        'gpm_cq' : {
            32 :[
                # USMC spawn points for start
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
                # Taliban rallypoints
                {
                    'name' : 'Taliban_SP_1_1',
                    'template' : 'rallypoint_taliban_placeable_noexpire',
                    'delete' : False,
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (598.250, 34.443, 1313.153),
                    'rotation' : (-171.829, 0.000, 0.000)
                    },
                {
                    'name' : 'Taliban_SP_2_1',
                    'template' : 'rallypoint_taliban_placeable_noexpire',
                    'delete' : False,
                    'team' : 1,
                    'delay' : 99999,
                    'position' : (1623.301, 36.348, 1813.809),
                    'rotation' : (109.847, 0.000, 0.000)
                    },
                {
                    'name' : 'Taliban_SP_3_1',
                    'template' : 'rallypoint_taliban_placeable_noexpire',
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
                # map default spawners to remove
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

    
# Define flags move position
# Settings:
#   name of flag : vec3 position
MAP_FLAGS = {
    'ramiel' : {
        'gpm_cq' : {
            128 : {
                'cpname_ramiel_aas128_habr_gidr_hq' : (67.3558, 20.0, 525.785)
                }
            }
        }
    }

# Define combat area parameters here
# CombatArea settings:
#   'name' : string: name of spawner, should be unique,
#   'create' : boolean: need to specify if it's new DoD,
#   'delete' : boolean: if need to remove combat area completely,
#   'modify' : boolean: if need to change something in combat area,
#   'team' : integer: spawner team,
#   'vehicles' : integer: vehicles type,
#   'layer' : integer: map layer,
#   'inverted' : integer 1 or 0: specifies if combat area will be inverted,
#   'areapoints' : list of vec2 positions for CA points,
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
                'CombatArea_11_aas_32' : { # instead of removing DoD we're changing it's team to 1 so only taliban allowed to move freely
                    'name' : 'CombatArea_11_aas_32',
                    'create' : False,
                    'delete' : False,
                    'modify' : True,
                    'team' : 1,
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
    }















