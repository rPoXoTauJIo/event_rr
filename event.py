# importing standart bf2 packages
import bf2
import host

#importing PR packages
import game.realitycore as realitycore
import game.realitytimer as realitytimer

# importing custom modules
import advdebug as D
import config as C


# ------------------------------------------------------------------------
# Init
# ------------------------------------------------------------------------
def init():
    D.init()
    host.registerGameStatusHandler(onGameStatusChanged)

# ------------------------------------------------------------------------
# DeInit
# ------------------------------------------------------------------------
def deinit():
    host.unregisterGameStatusHandler(onGameStatusChanged)

# ------------------------------------------------------------------------
# onGameStatusChanged
# ------------------------------------------------------------------------
def onGameStatusChanged(status):
    map_name = bf2.gameLogic.getMapName()
    map_gamemode = bf2.serverSettings.getGameMode()
    map_layer = realitycore.g_mapLayer

    if status == bf2.GameStatus.Loaded:
        # time critical tasks and should be done asap
        D.debugMessage('Event init stage0')
        init_event_stage_0(map_name, map_gamemode, map_layer)
    if status == bf2.GameStatus.Playing: # game is now in playing state
        # registering chatMessage handler
        #host.registerHandler('ChatMessage', onChatMessage, 1)
        D.debugMessage('Event init stage 1')
        init_event_stage_1(map_name, map_gamemode, map_layer)
        D.debugMessage('Event init finished')

def init_event_stage_0(map_name, map_gamemode, map_layer):
    if (map_name, map_gamemode, map_layer) in C.MAP_EVENT:
        try:
            if map_name in C.MAP_SPAWNERS:
                if map_gamemode in C.MAP_SPAWNERS[map_name]:
                    if map_layer in C.MAP_SPAWNERS[map_name][map_gamemode]:
                        deleteSpawners(map_name, map_gamemode, map_layer)
        except:
            D.errorMessage()
        '''
        if map_name in C.MAP_SPAWNPOINTS:
            if map_gamemode in C.MAP_SPAWNPOINTS[map_name]:
                if map_layer in C.MAP_SPAWNPOINTS[map_name][map_gamemode]:
                    setupSpawnpoints(map_name, map_gamemode, map_layer)
        '''

def init_event_stage_1(map_name, map_gamemode, map_layer):
    if (map_name, map_gamemode, map_layer) in C.MAP_EVENT:
        #D.debugMessage(getObjectSpawners())
        try:
            if map_name in C.MAP_FLAGS:
                if map_gamemode in C.MAP_FLAGS[map_name]:
                    if map_layer in C.MAP_FLAGS[map_name][map_gamemode]:
                        setupFlags(map_name, map_gamemode, map_layer)
            if map_name in C.MAP_HIDEOUTS:
                if map_gamemode in C.MAP_HIDEOUTS[map_name]:
                    if map_layer in C.MAP_HIDEOUTS[map_name][map_gamemode]:
                        pass
                        #setupHideouts(map_name, map_gamemode, map_layer)
            '''
            if map_name in C.MAP_SPAWNPOINTS:
                if map_gamemode in C.MAP_SPAWNPOINTS[map_name]:
                    if map_layer in C.MAP_SPAWNPOINTS[map_name][map_gamemode]:
                        setupSpawnpoints(map_name, map_gamemode, map_layer)
            '''
            if map_name in C.MAP_SPAWNERS:
                if map_gamemode in C.MAP_SPAWNERS[map_name]:
                    if map_layer in C.MAP_SPAWNERS[map_name][map_gamemode]:
                        setupSpawners(map_name, map_gamemode, map_layer)
            if map_name in C.MAP_DODS:
                if map_gamemode in C.MAP_DODS[map_name]:
                    if map_layer in C.MAP_DODS[map_name][map_gamemode]:
                        setupDoD(map_name, map_gamemode, map_layer)
        except:
            D.errorMessage()

# python 2.3.4 cant do [v for v in list]
def getbf2str(tuple, sep='/'):
    new_str = []
    for value in tuple:
        new_str.append(str(value))
    return sep.join(new_str)

def getObjectSpawners():
    spawners = realitycore.cleanListOfObjects(bf2.objectManager.getObjectsOfType(\
			'dice.hfe.world.ObjectTemplate.ObjectSpawner'))
    spawnerTemplates = []
    for spawner in spawners:
        spawnerTemplates.append(str(spawner.templateName))
    return spawnerTemplates

# this doesn't work
def setupSpawnpoints(map_name, map_gamemode, map_layer):
    spawnpoints = bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.Spawnpoint')
    for spawnpoint in spawnpoints:
        spawn_name = spawnpoint.templateName
        object = host.rcon_invoke("""
            objecttemplate.active %s
            objecttemplate.objecttemplate
            """ % spawn_name)
        D.debugMessage('setupSpawnpoints(): %s: %s' % (str(spawn_name), str(object)))

def setupFlags(map_name, map_gamemode, map_layer):
    for cp in realitycore.cleanListOfObjects(bf2.objectManager.getObjectsOfType(\
			'dice.hfe.world.ObjectTemplate.ControlPoint')):

		# checking for movable flags
        if cp.templateName in C.MAP_FLAGS[map_name][map_gamemode][map_layer].keys():
            position = C.MAP_FLAGS[map_name][map_gamemode][map_layer][cp.templateName]
            cp.setPosition((position[0], position[1], position[2])) # because setPosition((x, y, z))
            D.debugMessage('setupFlags(): moved flag %s to %s' % (str(cp.templateName), str(position)))
    
def setupSpawners(map_name, map_gamemode, map_layer):
    for spawner_set in C.MAP_SPAWNERS[map_name][map_gamemode][map_layer]:
        if spawner_set['name'] in getObjectSpawners():
            continue
        D.debugMessage('Spawning "%s" %s at %s' % (
            spawner_set['name'],
            spawner_set['template'],
            getbf2str(spawner_set['position']))
            )
        spawnAsset(spawner_set)

def deleteSpawners(map_name, map_gamemode, map_layer):
    mapObjectsSpawners = bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.ObjectSpawner')
    
    delete = []
    
    for spawner_set in C.MAP_SPAWNERS[map_name][map_gamemode][map_layer]:
        if 'delete' in spawner_set and spawner_set['delete']:
            delete.append(spawner_set['name'])

    for mapSpawner in mapObjectsSpawners:
        spawner_name = mapSpawner.templateName

        if spawner_name in delete:
            # acquiring spawner object&template
            # I DONT KNOW WHY THIS EVEN WORKS
            object = host.rcon_invoke("""
                objecttemplate.active %s
                objecttemplate.objecttemplate
                """ % spawner_name)

            # removing spawn&spawner
            host.rcon_invoke("""
                objecttemplate.nrofobjecttospawn 0
                objecttemplate.remove
                """)
            

            D.debugMessage('deleteSpawners(): removed.spawner = %s' % (spawner_name))
            D.debugMessage('deleteSpawners(): removed.PCOtemplate = %s' % (object))


def onGetSpawnersExpire(data = ''):
    for spawner in bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.ObjectSpawner'):
        D.debugMessage(spawner.templateName)




def spawnAsset(properties):
    host.rcon_invoke("""
ObjectTemplate.create ObjectSpawner %s
ObjectTemplate.activeSafe ObjectSpawner %s
ObjectTemplate.isNotSaveable 1
ObjectTemplate.hasMobilePhysics 0
ObjectTemplate.setObjectTemplate %s %s
ObjectTemplate.minSpawnDelay %s
ObjectTemplate.maxSpawnDelay %s
ObjectTemplate.maxNrOfObjectSpawned 1
ObjectTemplate.TimeToLive 12000
ObjectTemplate.Distance 100
ObjectTemplate.team %s
ObjectTemplate.teamOnVehicle 1""" % (
        properties['name'],
        properties['name'],
        properties['team'],
        properties['template'],
        properties['delay'],
        properties['delay'],
        properties['team'],
        ))
    host.rcon_invoke("""
Object.create %s
Object.absolutePosition %s
Object.rotation %s
Object.team %s
Object.delete 1
""" % (
        properties['name'],
        getbf2str(properties['position']),
        getbf2str(properties['rotation']),
        properties['team'],
        ))

def setupHideouts(map_name, map_gamemode, map_layer):
    for spawner_set in C.MAP_HIDEOUTS[map_name][map_gamemode][map_layer]:
        if spawner_set['name'] not in spawnerTemplates:
            D.debugMessage('Spawning "%s" %s at %s' % (
                spawner_set['name'],
                spawner_set['template'],
                getbf2str(spawner_set['position']))
                )
            spawnAsset(spawner_set)


def setupObjectives(map_name, map_gamemode, map_layer):
    pass

def setupDoD(map_name, map_gamemode, map_layer):
    for dod_set in C.MAP_DODS[map_name][map_gamemode][map_layer]:
        #host.rcon_invoke()
        #combatArea.active
        if 'create' in C.MAP_DODS[map_name][map_gamemode][map_layer][dod_set] and C.MAP_DODS[map_name][map_gamemode][map_layer][dod_set]['create']:
            createDoD(C.MAP_DODS[map_name][map_gamemode][map_layer][dod_set])
        if 'modify' in C.MAP_DODS[map_name][map_gamemode][map_layer][dod_set] and C.MAP_DODS[map_name][map_gamemode][map_layer][dod_set]['modify']:
            modifyDoD(C.MAP_DODS[map_name][map_gamemode][map_layer][dod_set])

def modifyDoD(properties):
    if 'delete' in properties and properties['delete']:
        host.rcon_invoke("""
CombatArea.active %s
CombatArea.deleteActiveCombatArea""" % (properties['name']))
        D.debugMessage('CombatArea.deleteActiveCombatArea %s' % (properties['name']))
        return #cause we dont need to do anything with deleted combat area
    if 'team' in properties:
        host.rcon_invoke("""
CombatArea.active %s
CombatArea.team %s""" % (properties['name'], properties['team']))
        D.debugMessage('CombatArea.team %s' % (properties['team']))
    
def createDoD(properties):
    #area_strings = ('CombatArea.addAreaPoint ' + '/'.join(point) + '/n') for point in properties['areapoints']) # can't use generators
    area_strings = []
    for point in properties['areapoints']:
        invoke_area_string = 'CombatArea.addAreaPoint ' + str(point[0]) + '/' + str(point[1])
        area_strings.append(invoke_area_string)
    invoke_area_strings = '\n'.join(area_strings)
    invoke_string = """
CombatArea.create %s
CombatArea.min 0.000000/0.000000
CombatArea.max 0.000000/0.000000
CombatArea.team %s
CombatArea.vehicles %s
CombatArea.layer %s
CombatArea.Inverted %s
""" % (properties['name'], properties['team'], properties['vehicles'], properties['layer'], properties['inverted'])
    host.rcon_invoke(invoke_string)
    D.debugMessage(invoke_string)
    for point in properties['areapoints']:
        invoke_area_string = 'CombatArea.addAreaPoint ' + str(point[0]) + '/' + str(point[1])
        host.rcon_invoke(invoke_area_string)
        D.debugMessage(invoke_area_string)
    active = host.rcon_invoke('combatArea.getActiveCombatAreaName')
    D.debugMessage(active)

















