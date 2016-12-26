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
        D.debugMessage('Event init start')
        init_event()
        D.debugMessage('Event init finished')

def init_event():
    map_name = bf2.gameLogic.getMapName()
    map_gamemode = bf2.serverSettings.getGameMode()
    map_layer = realitycore.g_mapLayer
    D.debugMessage('Running %s(%s, %s)' % (map_name, map_gamemode, map_layer))
    if (map_name, map_gamemode, map_layer) in C.MAP_EVENT:
        D.debugMessage('Found %s(%s, %s) in config' % (map_name, map_gamemode, map_layer))
        #D.debugMessage(getObjectSpawners())
        try:
            if map_name in C.MAP_FLAGS:
                pass
                #setupFlags(map_name, map_gamemode, map_layer)
            if map_name in C.MAP_HIDEOUTS:
                pass
                #setupHideouts(map_name, map_gamemode, map_layer)
            if map_name in C.MAP_SPAWNERS:
                setupSpawners(map_name, map_gamemode, map_layer)
            if map_name in C.MAP_DODS:
                setupDoD(map_name, map_gamemode, map_layer)
        except:
            D.errorMessage()
        #D.debugMessage('\n checking afterspawns')
        #D.debugMessage(getObjectSpawners())

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
    
    

def setupFlags(map_name, map_gamemode, map_layer):
    for cp in realitycore.cleanListOfObjects(bf2.objectManager.getObjectsOfType(\
			'dice.hfe.world.ObjectTemplate.ControlPoint')):

		# checking for movable flags
        if map_name in C.MAP_FLAGS.keys():
            if map_gamemode in C.MAP_FLAGS[map_name].keys():
                if map_layer in C.MAP_FLAGS[map_name][map_gamemode].keys():
                    if cp.templateName in C.MAP_FLAGS[map_name][map_gamemode][map_layer].keys():
                        position = C.MAP_FLAGS[map_name][map_gamemode][map_layer][cp.templateName]
                        cp.setPosition((position[0], position[1], position[2])) # because setPosition((x, y, z))
                        D.debugMessage('setupFlags(): moved flag %s to %s' % (str(cp.templateName), str(position)))
    
def setupSpawners(map_name, map_gamemode, map_layer):
    for spawner_set in C.MAP_SPAWNERS[map_name][map_gamemode][map_layer]:
        #if spawner_set['name'] in getObjectSpawners():
            #continue
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
        if not dod_set['create']:
            modifyDoD(dod_set)

def modifyDoD(properties):
    host.rcon_invoke('CombatArea.active %s' % (properties['name']))
    if 'team' in properties:
        host.rcon_invoke('CombatArea.team %s' % (properties['team']))
        D.debugMessage('CombatArea.team %s' % (properties['team']))


















