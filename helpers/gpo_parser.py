'''
                { # 4 tabs
                    # 5 tabs
                    'name' : 'USA_OS_main_LogiTruckUSA',
                    'template' : 'us_jep_hmmwv',
                    'team' : 2,
                    'delay' : 20,
                    'position' : (1223.100/47.893/1134.893),
                    'rotation' : (-138.616/0.000/0.000)
                    },
'''

g_filename_gpo = 'gameplayobjects_ramiel_cq128_custom.con'
# Define what you need as main output
# Default is 'ObjectSpawner'
# Options are: ObjectSpawner, SpawnPoint
g_output_type = 'ObjectSpawner'

class Spawner:

    def __init__(self, name):
        self.type = 'ObjectSpawner'
        self.name = name
        self.delete = True
        self.template = ['', '']
        self.cpid = None
        self.team = 1
        self.delay = 30
        self.position = (0.0, 0.0, 0.0)
        self.rotation = (0.0, 0.0, 0.0)
        self.output_str = ''

class SpawnPoint:

    def __init__(self, name):
        self.type = 'SpawnPoint'
        self.name = name
        self.delete = True
        self.cpid = None
        self.team = 1
        self.position = (0.0, 0.0, 0.0)
        self.rotation = (0.0, 0.0, 0.0)
        self.output_str = ''

with open(g_filename_gpo) as gpo:
    file = gpo.read()

objects = {}
activeSafe = None # should be object

# FUGGGGGGGGGGG
for line in file.splitlines():
    line = line.strip()
    if line.lower().startswith('objecttemplate.create '):
        type = line.split(' ')[1]
        name = line.split(' ')[2]
        if type == 'ObjectSpawner':
            object = Spawner(name)
        if type == 'SpawnPoint':
            object = SpawnPoint(name)
        objects[object.name] = object
        objects[object.name].type = type
        activeSafe = objects[object.name]
    if line.lower().startswith('objecttemplate.activesafe '):
        type = line.split(' ')[1]
        name = line.split(' ')[2]
        if type == 'ObjectSpawner':
            activeSafe = objects[name]
        if type == 'SpawnPoint':
            activeSafe = objects[name]
    if line.lower().startswith('object.create'): # wtf is this check
        name = line.split(' ')[1]
        if name not in objects:
            print('{} not found in objects'.format(name))
            break
        activeSafe = objects[name]

    # spawner properties
    if line.lower().startswith('objecttemplate.team '):
        team = int(line.split(' ')[1])
        objects[activeSafe.name].team = team
    if line.lower().startswith('objecttemplate.setobjecttemplate '):
        template_team = int(line.split(' ')[1])
        template_name = line.split(' ')[2]
        #print(template_team, activeSafe, template_name)
        objects[activeSafe.name].template[template_team-1] = template_name
        #print(objects[activeSafe.type][activeSafe].template)
    #ObjectTemplate.maxSpawnDelay 300
    if line.lower().startswith('objecttemplate.minspawndelay '): # because vbf2 style min more important
        delay = int(line.split(' ')[1])
        objects[activeSafe.name].delay = delay
    if line.lower().startswith('objecttemplate.setcontrolpointid '):
        cpid = int(line.split(' ')[1])
        objects[activeSafe.name].cpid = cpid

    # spawner object modifiers
    if line.lower().startswith('object.absoluteposition '):
        position_str = line.split(' ')[1].split('/')
        position = (float(position_str[0]), float(position_str[1]), float(position_str[2]))
        objects[activeSafe.name].position = position
    if line.lower().startswith('object.rotation '):
        rotation_str = line.split(' ')[1].split('/')
        rotation = (float(rotation_str[0]), float(rotation_str[1]), float(rotation_str[2]))
        objects[activeSafe.name].rotation = rotation
    if line.lower().startswith('object.setcontrolpointid '):
        cpid = int(line.split(' ')[1])
        objects[activeSafe.name].cpid = cpid

for object in objects:

    if objects[object].type == 'ObjectSpawner':
    
    
        # PART FOR RAMIEL INS GPO
        skip = True
        if objects[object].name.startswith('cpname_ramiel_aas128_insmain_vcp_rpg_') and skip:
            objects[object].template[objects[object].team-1] = 'arf_riflemanat_alt'
            skip = False
        if objects[object].name.startswith('cpname_ramiel_aas128_insmain_vcp_svd_') and skip:
            objects[object].template[objects[object].team-1] = 'arf_marksman'
            skip = False
        if objects[object].name.startswith('cpname_ramiel_aas128_insmain_vcp_pkm_') and skip:
            objects[object].template[objects[object].team-1] = 'arf_mg'
            skip = False

        if objects[object].name.startswith('cpname_ramiel_aas128_insmain_fob_rpg_') and skip:
            objects[object].template[objects[object].team-1] = 'arf_riflemanat_alt'
            skip = False
        if objects[object].name.startswith('cpname_ramiel_aas128_insmain_fob_svd_') and skip:
            objects[object].template[objects[object].team-1] = 'arf_marksman'
            skip = False
        if objects[object].name.startswith('cpname_ramiel_aas128_insmain_fob_pkm_') and skip:
            objects[object].template[objects[object].team-1] = 'arf_mg'
            skip = False
            
        if objects[object].name.startswith('cpname_ramiel_aas128_insmain_prison_rpg_') and skip:
            objects[object].template[objects[object].team-1] = 'arf_riflemanat_alt'
            skip = False
        if objects[object].name.startswith('cpname_ramiel_aas128_insmain_prison_svd_') and skip:
            objects[object].template[objects[object].team-1] = 'arf_marksman'
            skip = False
        if objects[object].name.startswith('cpname_ramiel_aas128_insmain_prison_pkm_') and skip:
            objects[object].template[objects[object].team-1] = 'arf_mg'
            skip = False
        
        if skip:
            continue

        objects[object].delete = False
        objects[object].delay = 300
        
        # note that it has tabs already
        objects[object].output_str = """
                {
                    'name' : '%s',
                    'delete' : %s,
                    'template' : '%s',
                    'team' : %s,
                    'delay' : %s,
                    'position' : %s,
                    'rotation' : %s
                    },""" % (objects[object].name,
                objects[object].delete,
                objects[object].template[objects[object].team-1],
                objects[object].team,
                objects[object].delay,
                objects[object].position,
                objects[object].rotation)
        print(objects[object].team, objects[object].name, objects[object].template)
    if objects[object].type == 'SpawnPoint':
        objects[object].output_str = """
                {
                    'name' : '%s',
                    'delete' : %s,
                    'cpid' : %s,
                    'team' : %s,
                    'position' : %s,
                    'rotation' : %s
                    },""" % (objects[object].name,
            objects[object].delete,
            objects[object].cpid,
            objects[object].team,
            objects[object].position,
            objects[object].rotation)
        print(objects[object].team, objects[object].name)

with open('out_gpo.txt', 'w') as out:
    for object in objects:
        if objects[object].type == g_output_type:
            print(objects[object].output_str)
            out.write(objects[object].output_str)





