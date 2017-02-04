# importing standart bf2 packages
import bf2
import host

# importing PR packages
import game.realitycore as realitycore
import game.realitytimer as realitytimer
import game.realityserver as realityserver
import game.realityconstants as realityconstants
import game.realitykits as realitykits
import game.realitygamemode as realitygamemode

# importing custom modules
import advdebug as D
import config as C

G_WAVE = 0
G_DOD_TIMER = None

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
    if status == bf2.GameStatus.Playing:  # game is now in playing state
        # registering chatMessage handler
        #host.registerHandler('ChatMessage', onChatMessage, 1)
        D.debugMessage('Event init stage 1')
        destroyDodTimer()
        setupDodTimer()
        init_event_stage_1(map_name, map_gamemode, map_layer)
        init_event_setup_special_conditions()
        host.registerHandler('VehicleDestroyed', onObjectiveDestroyed)
        D.debugMessage('Event init finished')


def destroyDodTimer():
    global G_DOD_TIMER

    if G_DOD_TIMER is not None:
        G_DOD_TIMER.destroy()
        G_DOD_TIMER = None


def setupDodTimer():
    global G_DOD_TIMER

    destroyDodTimer()
    G_DOD_TIMER = realitytimer.Timer(onDodTimerExpired, 300, 1)


def onDodTimerExpired(data=''):
    map_name = bf2.gameLogic.getMapName()
    map_gamemode = bf2.serverSettings.getGameMode()
    map_layer = realitycore.g_mapLayer
    for dod_set in C.MAP_DODS[map_name][map_gamemode][map_layer]:
        if 'delayed' in C.MAP_DODS[map_name][map_gamemode][map_layer][dod_set] and C.MAP_DODS[map_name][map_gamemode][map_layer][dod_set]['delayed']:
            modifyDoD(C.MAP_DODS[map_name][map_gamemode][map_layer][dod_set])
            D.debugMessage('Dod %s modified' % (C.MAP_DODS[map_name][map_gamemode][map_layer][dod_set]['name']))

    destroyDodTimer()


def init_event_stage_0(map_name, map_gamemode, map_layer):
    if (map_name, map_gamemode, map_layer) in C.MAP_EVENT:
        try:
            if map_name in C.MAP_SPAWNERS:
                if map_gamemode in C.MAP_SPAWNERS[map_name]:
                    if map_layer in C.MAP_SPAWNERS[map_name][map_gamemode]:
                        deleteSpawners(map_name, map_gamemode, map_layer)
            if map_name in C.MAP_FLAGS:
                if map_gamemode in C.MAP_FLAGS[map_name]:
                    if map_layer in C.MAP_FLAGS[map_name][map_gamemode]:
                        setupFlags(map_name, map_gamemode, map_layer)
            if map_name in C.MAP_DODS:
                if map_gamemode in C.MAP_DODS[map_name]:
                    if map_layer in C.MAP_DODS[map_name][map_gamemode]:
                        setupDoD(map_name, map_gamemode, map_layer)
            if map_name in C.MAP_OBJECTIVES:
                if map_gamemode in C.MAP_OBJECTIVES[map_name]:
                    if map_layer in C.MAP_OBJECTIVES[map_name][map_gamemode]:
                        setupObjectives(map_name, map_gamemode, map_layer)
            if map_name in C.MAP_HIDEOUTS:
                if map_gamemode in C.MAP_HIDEOUTS[map_name]:
                    if map_layer in C.MAP_HIDEOUTS[map_name][map_gamemode]:
                        setupHideouts(map_name, map_gamemode, map_layer)
        except:
            D.errorMessage()


def init_event_stage_1(map_name, map_gamemode, map_layer):
    if (map_name, map_gamemode, map_layer) in C.MAP_EVENT:
        # D.debugMessage(getObjectSpawners())
        try:

            if map_name in C.MAP_SPAWNERS:
                if map_gamemode in C.MAP_SPAWNERS[map_name]:
                    if map_layer in C.MAP_SPAWNERS[map_name][map_gamemode]:
                        setupSpawners(map_name, map_gamemode, map_layer)

        except:
            D.errorMessage()

# PURE SHIT
def init_event_setup_special_conditions():
    global realityserver
    global realitykits

    tickets = {
        realityconstants.VEHICLE_TYPE_ARMOR: -10,
        realityconstants.VEHICLE_TYPE_IFV: -10,
        realityconstants.VEHICLE_TYPE_JET: -10,
        realityconstants.VEHICLE_TYPE_HELIATTACK: -10,
        realityconstants.VEHICLE_TYPE_TURBOPROP: -7,
        realityconstants.VEHICLE_TYPE_SHIP: -50,
        realityconstants.VEHICLE_TYPE_HELI: -5,
        realityconstants.VEHICLE_TYPE_RECON: -5,
        realityconstants.VEHICLE_TYPE_AAV: -5,
        realityconstants.VEHICLE_TYPE_APC: -35,  # modified for fr_apc_vbci
        realityconstants.VEHICLE_TYPE_TRANSPORT: -2,
        realityconstants.VEHICLE_TYPE_SOLDIER: -1
    }
    # realityserver.C( 'SUPPLIES_TEMPLATES_TEAMLOCKED' )
    realityserver.C('TICKETS', tickets)

    kitlimits = {}

    kitlimits['KIT_LIMIT_8'] = {
        'sniper': 0,
        'aa': 0,
        'at': 0,
        'engineer': 0,
        'marksman': 1,
        'assault': 1,
        'riflemanat': 1,
        'riflemanap': 1,
        'mg': 1,
        'spotter': 0,
        'civilian': 1,
        'specialist': 0}
    kitlimits['KIT_LIMIT_16'] = {
        'sniper': 1,
        'aa': 1,
        'at': 0,
        'engineer': 1,
        'marksman': 2,
        'assault': 2,
        'riflemanat': 2,
        'riflemanap': 2,
        'mg': 2,
        'spotter': 0,
        'civilian': 3,
        'specialist': 0}
    kitlimits['KIT_LIMIT_24'] = {
        'sniper': 1,
        'aa': 1,
        'at': 0,
        'engineer': 1,
        'marksman': 3,
        'assault': 3,
        'riflemanat': 4,
        'riflemanap': 3,
        'mg': 3,
        'spotter': 0,
        'civilian': 9,
        'specialist': 0}
    kitlimits['KIT_LIMIT_32'] = {
        'sniper': 2,
        'aa': 2,
        'at': 0,
        'engineer': 2,
        'marksman': 3,
        'assault': 3,
        'riflemanat': 5,
        'riflemanap': 3,
        'mg': 3,
        'spotter': 0,
        'civilian': 12,
        'specialist': 0}
    kitlimits['KIT_LIMIT_44'] = {
        'sniper': 2,
        'aa': 2,
        'at': 0,
        'engineer': 2,
        'marksman': 4,
        'assault': 4,
        'riflemanat': 8,
        'riflemanap': 4,
        'mg': 4,
        'spotter': 0,
        'civilian': 16,
        'specialist': 0}

    kits_factions = {
        'ch': {
            'marksman': 6, 'support': 4, 'riflemanat': 4, 'assault': 6, 'riflemanap': 4, 'specialist': 4, 'mg': 6,
            'spotter': 3,
            'officer': 2, 'sniper': 3, 'aa': 3, 'at': 3, 'engineer': 3, 'medic': 2, 'tanker': 1, 'pilot': 1, 'rifleman': 0
        },
        'gb': {
            'marksman': 6, 'support': 4, 'riflemanat': 4, 'assault': 6, 'riflemanap': 4, 'specialist': 4, 'mg': 6,
            'spotter': 3,
            'officer': 2, 'sniper': 3, 'aa': 3, 'at': 3, 'engineer': 3, 'medic': 2, 'tanker': 1, 'pilot': 1, 'rifleman': 0
        },
        'ger': {
            'marksman': 6, 'support': 4, 'riflemanat': 4, 'assault': 6, 'riflemanap': 4, 'specialist': 4, 'mg': 6,
            'spotter': 3,
            'officer': 2, 'sniper': 3, 'aa': 3, 'at': 3, 'engineer': 3, 'medic': 2, 'tanker': 1, 'pilot': 1, 'rifleman': 0
        },
        'mec': {
            'marksman': 6, 'support': 4, 'riflemanat': 4, 'assault': 6, 'riflemanap': 4, 'specialist': 4, 'mg': 6,
            'spotter': 3,
            'officer': 2, 'sniper': 3, 'aa': 3, 'at': 3, 'engineer': 3, 'medic': 2, 'tanker': 1, 'pilot': 1, 'rifleman': 0
        },
        'us': {
            'marksman': 6, 'support': 4, 'riflemanat': 4, 'assault': 6, 'riflemanap': 4, 'specialist': 4, 'mg': 6,
            'spotter': 3,
            'officer': 2, 'sniper': 3, 'aa': 3, 'at': 3, 'engineer': 3, 'medic': 2, 'tanker': 1, 'pilot': 1, 'rifleman': 0
        },
        'usa': {  # limited assault ############################################
            'marksman': 6, 'support': 4, 'riflemanat': 4, 'assault': 9, 'riflemanap': 4, 'specialist': 4, 'mg': 6,
            'spotter': 3,
            'officer': 2, 'sniper': 3, 'aa': 3, 'at': 3, 'engineer': 3, 'medic': 2, 'tanker': 1, 'pilot': 1, 'rifleman': 0
        },
        'arf': {
            'marksman': 1, 'support': 2, 'riflemanat': 4, 'assault': 1, 'riflemanap': 1, 'specialist': 1, 'mg': 2,
            'spotter': 1,
            'officer': 2, 'sniper': 1, 'engineer': 2, 'medic': 1, 'rifleman': 0
        },
        'cf': {
            'marksman': 6, 'support': 4, 'riflemanat': 4, 'assault': 6, 'riflemanap': 4, 'specialist': 4, 'mg': 6,
            'spotter': 3,
            'officer': 2, 'sniper': 3, 'aa': 3, 'at': 3, 'engineer': 3, 'medic': 2, 'tanker': 1, 'pilot': 1, 'rifleman': 0
        },
        'ru': {
            'marksman': 6, 'support': 4, 'riflemanat': 4, 'assault': 6, 'riflemanap': 4, 'specialist': 4, 'mg': 6,
            'spotter': 3,
            'officer': 2, 'sniper': 3, 'aa': 3, 'at': 3, 'engineer': 3, 'medic': 2, 'tanker': 1, 'pilot': 1, 'rifleman': 0
        },
        'idf': {
            'marksman': 6, 'support': 4, 'riflemanat': 4, 'assault': 6, 'riflemanap': 4, 'specialist': 4, 'mg': 6,
            'spotter': 3,
            'officer': 2, 'sniper': 3, 'aa': 3, 'at': 3, 'engineer': 3, 'medic': 2, 'tanker': 1, 'pilot': 1, 'rifleman': 0
        },
        'chinsurgent': {
            'marksman': 6, 'support': 4, 'riflemanat': 4, 'assault': 6, 'riflemanap': 4, 'specialist': 4, 'mg': 6,
            'spotter': 3,
            'officer': 2, 'sniper': 3, 'aa': 3, 'at': 3, 'engineer': 3, 'medic': 2, 'tanker': 1, 'rifleman': 0
        },
        'hamas': {
            'marksman': 6, 'support': 4, 'riflemanat': 4, 'assault': 6, 'riflemanap': 4, 'specialist': 4, 'mg': 6,
            'spotter': 3,
            'officer': 2, 'sniper': 3, 'aa': 3, 'at': 3, 'engineer': 3, 'medic': 2, 'tanker': 1, 'rifleman': 0
        },
        'taliban': {
            'marksman': 6, 'support': 4, 'riflemanat': 4, 'assault': 6, 'riflemanap': 4, 'specialist': 4, 'mg': 6,
            'spotter': 3,
            'officer': 2, 'sniper': 3, 'aa': 3, 'at': 3, 'engineer': 3, 'medic': 2, 'tanker': 1, 'rifleman': 0
        },
        'meinsurgent': {
            'officer': 2, 'insurgent1': 0, 'insurgent2': 0, 'insurgent3': 0, 'insurgent4': 0, 'civilian': 0, 'sapper': 0,
            'medic': 2
        },
        'vnusa': {
            'support': 4, 'riflemanat': 4, 'assault': 6, 'riflemanap': 4, 'specialist': 4, 'mg': 6, 'spotter': 3,
            'officer': 2, 'sniper': 3, 'at': 3, 'engineer': 3, 'medic': 2, 'tanker': 1, 'pilot': 1, 'rifleman': 0
        },
        'vnusmc': {
            'support': 4, 'riflemanat': 4, 'assault': 6, 'riflemanap': 4, 'specialist': 4, 'mg': 6, 'spotter': 3,
            'officer': 2, 'sniper': 3, 'at': 3, 'engineer': 3, 'medic': 2, 'tanker': 1, 'pilot': 1, 'rifleman': 0
        },
        'vnnva': {
            'support': 4, 'riflemanat': 4, 'assault': 6, 'riflemanap': 4, 'specialist': 4, 'mg': 6, 'spotter': 3,
            'officer': 2, 'sniper': 3, 'at': 3, 'engineer': 3, 'medic': 2, 'tanker': 1, 'pilot': 1, 'rifleman': 0
        },
        'gb82': {
            'marksman': 6, 'support': 4, 'riflemanat': 4, 'assault': 6, 'riflemanap': 4, 'specialist': 4, 'mg': 6,
            'spotter': 3,
            'officer': 2, 'sniper': 3, 'aa': 3, 'at': 3, 'engineer': 3, 'medic': 2, 'tanker': 1, 'pilot': 1, 'rifleman': 0
        },
        'arg82': {
            'marksman': 6, 'support': 4, 'riflemanat': 4, 'assault': 6, 'riflemanap': 4, 'specialist': 4, 'mg': 6,
            'spotter': 3,
            'officer': 2, 'sniper': 3, 'aa': 3, 'at': 3, 'engineer': 3, 'medic': 2, 'tanker': 1, 'pilot': 1, 'rifleman': 0
        },
        'fr': {
            'marksman': 6, 'support': 4, 'riflemanat': 4, 'assault': 6, 'riflemanap': 4, 'specialist': 4, 'mg': 6,
            'spotter': 3,
            'officer': 2, 'sniper': 3, 'aa': 3, 'at': 3, 'engineer': 3, 'medic': 2, 'tanker': 1, 'pilot': 1, 'rifleman': 0
        },
        'fsa': {
            'marksman': 6, 'support': 4, 'riflemanat': 4, 'assault': 6, 'riflemanap': 4, 'specialist': 4, 'mg': 6,
            'spotter': 3,
            'officer': 2, 'sniper': 3, 'aa': 3, 'at': 3, 'engineer': 3, 'medic': 2, 'tanker': 1, 'rifleman': 0
        },
        'nl': {
            'marksman': 6, 'support': 4, 'riflemanat': 4, 'assault': 6, 'riflemanap': 4, 'specialist': 4, 'mg': 6,
            'spotter': 3,
            'officer': 2, 'sniper': 3, 'aa': 3, 'at': 3, 'engineer': 3, 'medic': 2, 'tanker': 1, 'pilot': 1, 'rifleman': 0
        },
    }

    for limit, limits in kitlimits.items():
        realityserver.C(limit, limits)

    realityserver.C('KIT_LIMITS', kits_factions)

    realitykits.setupKitLimits()


def onObjectiveDestroyed(obj, attacker):

    if obj.templateName.lower() != 'ammocache':
        return

    init_event_stage_wave()


def init_event_stage_wave():
    global G_WAVE

    G_WAVE = int(G_WAVE + 1)  # cause hularious fucks were given in past

    map_name = bf2.gameLogic.getMapName()
    map_gamemode = bf2.serverSettings.getGameMode()
    map_layer = realitycore.g_mapLayer

    if (map_name, map_gamemode, map_layer) in C.MAP_EVENT:
        try:
            if map_name in C.MAP_SPAWNERS_WAVE:
                if map_gamemode in C.MAP_SPAWNERS_WAVE[map_name]:
                    if map_layer in C.MAP_SPAWNERS_WAVE[
                            map_name][map_gamemode]:
                        if G_WAVE in C.MAP_SPAWNERS_WAVE[
                                map_name][map_gamemode][map_layer]:
                            setupSpawnersWave(
                                map_name, map_gamemode, map_layer, G_WAVE)
                            disableSpawnersWave(
                                map_name, map_gamemode, map_layer, G_WAVE)
        except:
            D.errorMessage()

# python 2.3.4 cant do [v for v in list]
def getbf2str(tuple, sep='/'):
    new_str = []
    for value in tuple:
        new_str.append(str(value))
    return sep.join(new_str)


def getObjectSpawners():
    spawners = realitycore.cleanListOfObjects(bf2.objectManager.getObjectsOfType(
        'dice.hfe.world.ObjectTemplate.ObjectSpawner'))
    spawnerTemplates = []
    for spawner in spawners:
        spawnerTemplates.append(str(spawner.templateName))
    return spawnerTemplates


def setupSpawnersWave(map_name, map_gamemode, map_layer, wave):
    D.debugMessage('Spawning wave: %s' % (G_WAVE))
    for spawner_set in C.MAP_SPAWNERS_WAVE[
            map_name][map_gamemode][map_layer][wave]:
        if 'delete' in spawner_set and spawner_set['delete']:
            continue
        D.debugMessage('Spawning "%s" %s at %s' % (
            spawner_set['name'],
            spawner_set['template'],
            getbf2str(spawner_set['position']))
        )
        spawnAsset(spawner_set)


def setupFlags(map_name, map_gamemode, map_layer):
    for cp in realitycore.cleanListOfObjects(bf2.objectManager.getObjectsOfType(
            'dice.hfe.world.ObjectTemplate.ControlPoint')):

                # checking for movable flags
        if cp.templateName in C.MAP_FLAGS[map_name][
                map_gamemode][map_layer].keys():
            settings = C.MAP_FLAGS[map_name][
                map_gamemode][map_layer][cp.templateName]
            if 'delete' in settings and settings['delete']:
                D.debugMessage('setupFlags(): removed flag %s' %
                               (str(cp.templateName)))
                #try:
                #    realitycore.g_controlPoints.remove(cp)
                #except:
                #    pass
                try:
                    realitycore.deleteObject(cp)
                    realitygamemode.getCurrentGameMode().setupRoutes()
                    realitygamemode.getCurrentGameMode().updateObjectives()
                except:
                    D.errorMessage()
                continue
            if 'position' in settings:
                position = C.MAP_FLAGS[map_name][map_gamemode][
                    map_layer][cp.templateName]['position']
                # because setPosition((x, y, z))
                cp.setPosition((position[0], position[1], position[2]))
                D.debugMessage('setupFlags(): moved flag %s to %s' %
                               (str(cp.templateName), str(position)))
            if 'team' in settings:
                object = host.rcon_invoke("""
                    objecttemplate.active %s
                    objecttemplate.team %s
                    """ % (cp.templateName, settings['team']))


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


def disableSpawnersWave(map_name, map_gamemode, map_layer, wave):
    mapObjectsSpawners = bf2.objectManager.getObjectsOfType(
        'dice.hfe.world.ObjectTemplate.ObjectSpawner')

    delete = []

    for spawner_set in C.MAP_SPAWNERS_WAVE[
            map_name][map_gamemode][map_layer][wave]:
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

            D.debugMessage(
                'deleteSpawners(): removed.spawner = %s' %
                (spawner_name))
            D.debugMessage(
                'deleteSpawners(): removed.PCOtemplate = %s' %
                (object))


def deleteSpawners(map_name, map_gamemode, map_layer):
    mapObjectsSpawners = bf2.objectManager.getObjectsOfType(
        'dice.hfe.world.ObjectTemplate.ObjectSpawner')

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

            D.debugMessage(
                'deleteSpawners(): removed.spawner = %s' %
                (spawner_name))
            D.debugMessage(
                'deleteSpawners(): removed.PCOtemplate = %s' %
                (object))


def onGetSpawnersExpire(data=''):
    for spawner in bf2.objectManager.getObjectsOfType(
            'dice.hfe.world.ObjectTemplate.ObjectSpawner'):
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
        D.debugMessage('Spawning "%s" %s at %s' % (
            spawner_set['name'],
            spawner_set['template'],
            getbf2str(spawner_set['position']))
        )
        spawnAsset(spawner_set)


def setupObjectives(map_name, map_gamemode, map_layer):
    for spawner_set in C.MAP_OBJECTIVES[map_name][map_gamemode][map_layer]:
        D.debugMessage('Spawning "%s" %s at %s' % (
            spawner_set['name'],
            spawner_set['template'],
            getbf2str(spawner_set['position']))
        )
        spawnAsset(spawner_set)


def setupDoD(map_name, map_gamemode, map_layer):
    for dod_set in C.MAP_DODS[map_name][map_gamemode][map_layer]:
        # host.rcon_invoke()
        # combatArea.active
        if 'create' in C.MAP_DODS[map_name][map_gamemode][map_layer][
                dod_set] and C.MAP_DODS[map_name][map_gamemode][map_layer][dod_set]['create']:
            createDoD(C.MAP_DODS[map_name][map_gamemode][map_layer][dod_set])
        if 'modify' in C.MAP_DODS[map_name][map_gamemode][map_layer][
                dod_set] and C.MAP_DODS[map_name][map_gamemode][map_layer][dod_set]['modify']:
            modifyDoD(C.MAP_DODS[map_name][map_gamemode][map_layer][dod_set])


def modifyDoD(properties):
    if 'delete' in properties and properties['delete']:
        host.rcon_invoke("""
CombatArea.active %s
CombatArea.deleteActiveCombatArea""" % (properties['name']))
        D.debugMessage(
            'CombatArea.deleteActiveCombatArea %s' %
            (properties['name']))
        return  # cause we dont need to do anything with deleted combat area
    if 'team' in properties:
        host.rcon_invoke("""
CombatArea.active %s
CombatArea.team %s""" % (properties['name'], properties['team']))
        D.debugMessage('CombatArea.team %s' % (properties['team']))
    if 'delayed' in properties:
        host.rcon_invoke("""
CombatArea.active %s
CombatArea.deleteActiveCombatArea""" % (properties['name']))
        D.debugMessage('CombatArea.deleteActiveCombatArea %s' % (properties['name']))


def createDoD(properties):
    # area_strings = ('CombatArea.addAreaPoint ' + '/'.join(point) + '/n') for
    # point in properties['areapoints']) # can't use generators
    area_strings = []
    for point in properties['areapoints']:
        invoke_area_string = 'CombatArea.addAreaPoint ' + \
            str(point[0]) + '/' + str(point[1])
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
        invoke_area_string = 'CombatArea.addAreaPoint ' + \
            str(point[0]) + '/' + str(point[1])
        host.rcon_invoke(invoke_area_string)
        D.debugMessage(invoke_area_string)
    active = host.rcon_invoke('combatArea.getActiveCombatAreaName')
    D.debugMessage(active)
