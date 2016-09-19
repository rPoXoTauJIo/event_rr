# importing standart bf2 packages
import bf2
import host

#importing PR packages
import game.realitycore as realitycore

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
    if status == bf2.GameStatus.Playing: # game is now in playing state
        # registering chatMessage handler
        #host.registerHandler('ChatMessage', onChatMessage, 1)
        init_event()

def init_event():
    map_name = bf2.gameLogic.getMapName()
    map_gamemode = bf2.serverSettings.getGameMode()
    map_layer = realitycore.g_mapLayer
    if (map_name, map_gamemode, map_layer) in C.MAP_EVENT:
        try:
            setupFlags(map_name, map_gamemode, map_layer)
            setupHideouts(map_name, map_gamemode, map_layer)
            setupSpawners(map_name, map_gamemode, map_layer)
        except:
            D.errorMessage()

# python 2.3.4 cant do [v for v in list]
def getbf2str(turple, sep='/'):
    new_str = []
    for value in turple:
        new_str.append(str(value))
    return sep.join(new_str)

def getObjectSpawners():
    spawners = realitycore.cleanListOfObjects(bf2.objectManager.getObjectsOfType(\
			'dice.hfe.world.ObjectTemplate.ObjectSpawner'))
    spawnerTemplates = []
    for spawner in spawners:
        spawnerTemplates.append(str(spawner.templateName))
    return 
    
    

def setupFlags(map_name, map_gamemode, map_layer):
    for cp in realitycore.cleanListOfObjects(bf2.objectManager.getObjectsOfType(\
			'dice.hfe.world.ObjectTemplate.ControlPoint')):

		# checkinf for movable flags
        if map_name in C.MAP_FLAGS.keys():
            if map_gamemode in C.MAP_FLAGS[map_name].keys():
                if map_layer in C.MAP_FLAGS[map_name][map_gamemode].keys():
                    if cp.templateName in C.MAP_FLAGS[map_name][map_gamemode][map_layer].keys():
                        position = C.MAP_FLAGS[map_name][map_gamemode][map_layer][cp.templateName]
                        cp.setPosition((position[0], position[1], position[2])) # because setPosition((x, y, z))
                        D.debugMessage('setupFlags(): moved flag %s to %s' % (str(cp.templateName), str(position)))
    
def setupSpawners(map_name, map_gamemode, map_layer):
    for spawner_set in C.MAP_SPAWNERS[map_name][map_gamemode][map_layer]:
        if spawner_set['name'] not in spawnerTemplates:
            D.debugMessage('Spawning "%s" %s at %s' % (
                spawner_set['name'],
                spawner_set['template'],
                getbf2str(spawner_set['position']))
                )
            spawnAsset(spawner_set)


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
        getbf2str(spawner_set['position']),
        getbf2str(spawner_set['rotation']),
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






















