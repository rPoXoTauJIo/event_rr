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




class Spawner:

    def __init__(self, name):
        self.name = name
        self.template = ['', '']
        self.team = 1
        self.delay = 30
        self.position = (0.0, 0.0, 0.0)
        self.rotation = (0.0, 0.0, 0.0)
        self.output_str = ''

with open('gameplayobjects_bamyan_cq32.con') as gpo:
    file = gpo.read()

spawners = {}
activeSafe = None
for line in file.splitlines():
    line = line.strip()
    if line == 'endIf':
        break # supposed to start spawnpoints
    if line.lower().startswith('objecttemplate.create '):
        type = line.split(' ')[1]
        name = line.split(' ')[2]
        if type == 'ObjectSpawner':
            activeSafe = name
            spawners[activeSafe] = Spawner(name)
    if line.lower().startswith('objecttemplate.activesafe '):
        type = line.split(' ')[1]
        name = line.split(' ')[2]
        if type == 'ObjectSpawner':
            activeSafe = name
    if line.lower().startswith('object.create'):
        name = line.split(' ')[1]
        if name not in spawners:
            print('{} not found in spawners'.format(name))
            break
        activeSafe = name

    # spawner properties
    if line.lower().startswith('objecttemplate.team '):
        team = int(line.split(' ')[1])
        spawners[activeSafe].team = team
    if line.lower().startswith('objecttemplate.setobjecttemplate '):
        template_team = int(line.split(' ')[1])
        template_name = line.split(' ')[2]
        #print(template_team, activeSafe, template_name)
        spawners[activeSafe].template[template_team-1] = template_name
        #print(spawners[activeSafe].template)
    #ObjectTemplate.maxSpawnDelay 300
    if line.lower().startswith('objecttemplate.minspawndelay '): # because vbf2 style
        delay = int(line.split(' ')[1])
        spawners[activeSafe].delay = delay

    # spawner spawn modifiers
    if line.lower().startswith('object.absoluteposition '):
        position_str = line.split(' ')[1].split('/')
        position = (float(position_str[0]), float(position_str[1]), float(position_str[2]))
        spawners[activeSafe].position = position
    if line.lower().startswith('object.rotation '):
        rotation_str = line.split(' ')[1].split('/')
        rotation = (float(rotation_str[0]), float(rotation_str[1]), float(rotation_str[2]))
        spawners[activeSafe].rotation = rotation
        
for spawner in spawners:
    spawners[spawner].output_str = """
                {
                    'name' : '%s',
                    'delete' : True,
                    'template' : '%s',
                    'team' : %s,
                    'delay' : %s,
                    'position' : %s,
                    'rotation' : %s
                    },""" % (spawners[spawner].name,
            spawners[spawner].template[spawners[spawner].team-1],
            spawners[spawner].team,
            spawners[spawner].delay,
            spawners[spawner].position,
            spawners[spawner].rotation)
    print(spawners[spawner].team, spawners[spawner].name, spawners[spawner].template)

with open('out.txt', 'w') as out:
    for spawner in spawners:
        #print(spawners[spawner].output_str)
        out.write(spawners[spawner].output_str)





