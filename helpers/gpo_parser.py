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
        self.template = 'fixed_supply_crate_tal'
        self.team = 1
        self.delay = 300
        self.position = (0.0, 0.0, 0.0)
        self.rotation = (0.0, 0.0, 0.0)
        self.output_str = ''

with open('file.txt') as gpo:
    file = gpo.read()

spawners = {}
activeSafe = None
for line in file.splitlines():
    line = line.strip()
    if line.lower().startswith('object.create'):
        name = line.split(' ')[1]
        activeSafe = name
        spawners[activeSafe] = Spawner(name)
    if line.lower().startswith('object.absoluteposition'):
        position_str = line.split(' ')[1].split('/')
        position = (float(position_str[0]), float(position_str[1]), float(position_str[2]))
        spawners[activeSafe].position = position
    if line.lower().startswith('object.rotation'):
        rotation_str = line.split(' ')[1].split('/')
        rotation = (float(rotation_str[0]), float(rotation_str[1]), float(rotation_str[2]))
        spawners[activeSafe].rotation = rotation

for spawner in spawners:
    spawners[spawner].output_str = """
                {
                    'name' : '%s',
                    'template' : '%s',
                    'team' : %s,
                    'delay' : %s,
                    'position' : %s,
                    'rotation' : %s
                    },""" % (spawners[spawner].name,
            spawners[spawner].template,
            spawners[spawner].team,
            spawners[spawner].delay,
            spawners[spawner].position,
            spawners[spawner].rotation)

with open('out.txt', 'w') as out:
    for spawner in spawners:
        out.write(spawners[spawner].output_str)





