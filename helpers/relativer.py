"""
    Algorithm:
        Grab source statics object
        Grab gpo objects data
        Calculate offset
        
        Grab statics objects
        Create new objects
        Move them to source postions + offset.
        
        Parse
"""

import random


class Kit:

    def __init__(self, name):
        self.name = name
        self.position = None
        self.rotation = (0.0, 0.0, 0.0) # due to bug in bf2 they have to face north all the time
        self.parent_position_offset = None
        
    def set_offset_position(self, other_position):
        offset_X = self.position[0] - other_position[0]
        offset_Y = self.position[1] - other_position[1]
        offset_Z = self.position[2] - other_position[2]
        self.parent_position_offset = (offset_X, offset_Y, offset_Z)
    
    def set_position_from_position_and_offset(self, other_position, offset_position):
        self.parent_position_offset = offset_position
        position_X = other_position[0] + offset_position[0]
        position_Y = other_position[1] + offset_position[1]
        position_Z = other_position[2] + offset_position[2]
        self.position = (position_X, position_Y, position_Z)
    
    def get_spawner_object_string(self):
        output = '''
    rem [ObjectSpawner: {self.name}]
    Object.create {self.name}
    Object.absolutePosition {self.position[0]}/{self.position[1]}/{self.position[2]}
    Object.rotation {self.rotation[0]}/{self.rotation[1]}/{self.rotation[2]}
    Object.setControlPointId 1
    Object.layer 1
    '''.format(self=self)
        return output
    
    def get_spawner_template_string(self):
        output = '''
rem [ObjectSpawnerTemplate: {self.name}]
ObjectTemplate.create ObjectSpawner {self.name}
ObjectTemplate.activeSafe ObjectSpawner {self.name}
ObjectTemplate.modifiedByUser "Administrator"
ObjectTemplate.isNotSaveable 1
ObjectTemplate.hasMobilePhysics 0
ObjectTemplate.setObjectTemplate 1 meinsurgent_riflemanat_pickup
    '''.format(self=self)
        return output
        
        
class StaticObject:
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.position = None
        self.rotation = None
        self.source = False
        self.childs = {}

    def parse_childs(self, filename):
        self.childs = Parser().parse_gpo(filename)
        for child in self.childs:
            self.childs[child].set_offset_position(self.position)
            #print(self.childs[child].parent_position_offset)
    
    def is_source(self):
        return self.source
    
    def create_kits_from_kits_offsets(self, kits, template):
        id = 0
        for kit in kits:
            name = '_'.join([template, str(id)])
            id += 1
            newKit = Kit(name)
            newKit.set_position_from_position_and_offset(self.position, kits[kit].parent_position_offset)
            self.childs[name] = newKit
        
    def generate_gpo_output(self):
        final_string = ''
        for kit in self.childs:
            final_string += self.childs[kit].get_spawner_object_string()

        return final_string

    def generate_template_output(self):
        final_string = ''
        for kit in self.childs:
            final_string += self.childs[kit].get_spawner_template_string()

        return final_string
        
class Parser:
    
    def __init__(self):
        pass
    
    def parse_staticobjects(self, filename):
        with open(filename) as fo:
            lines = fo.read().splitlines()

        objects = {}
        activeSafe = None
        for line in lines:
            line = line.strip()
            if line.lower().startswith('object.create '):
                name = line.split(' ')[1]
                id = random.randint(0, 1023) # hue hue
                object = StaticObject(id, name)
                objects[object.id] = object
                activeSafe = objects[object.id]
            if line.lower().startswith('object.absoluteposition '):
                objects[activeSafe.id].position = tuple(float(num) for num in line.replace('\n', '').split(' ')[1].split('/'))
            if line.lower().startswith('object.rotation '):
                objects[activeSafe.id].rotation = tuple(float(num) for num in line.replace('\n', '').split(' ')[1].split('/'))
            if line.lower().startswith('object.source '):
                objects[activeSafe.id].source = True
        
        return objects
        
    def parse_gpo(self, filename):
        with open(filename) as fo:
            lines = fo.read().splitlines()

        objects = {}
        activeSafe = None
        for line in lines:
            line = line.strip()
            if line.lower().startswith('object.create '):
                name = line.split(' ')[1]
                object = Kit(name)
                objects[object.name] = object
                activeSafe = objects[object.name]
            if line.lower().startswith('object.absoluteposition '):
                objects[activeSafe.name].position = tuple(float(num) for num in line.replace('\n', '').split(' ')[1].split('/'))
            if line.lower().startswith('object.rotation '):
                objects[activeSafe.name].rotation = tuple(float(num) for num in line.replace('\n', '').split(' ')[1].split('/'))
        
        return objects

class Calculator:
    
    def __init__(self):
        self.filenames = {
            'source_staticobjects' : 'relative_data_staticobjects.txt',
            'source_gpo' : 'relative_data_gpo.txt'
            }
        self.staticobjects = {}

    def main(self):
        #static_source = StaticObject(Parser().parse_gpo(self.filenames['static_source']))
        #static_source.parse_childs(self.filenames['gpo_source'])
        self.staticobjects = Parser().parse_staticobjects(self.filenames['source_staticobjects'])
        source_id = self.get_source_id()
        self.staticobjects[source_id].parse_childs(self.filenames['source_gpo'])
        # DIRTY HACK for diffirent templates
        template = 'cpname_ramiel_aas128_insmain_prison_svd'
        for object in self.staticobjects:
            if not self.staticobjects[object].is_source():
                self.staticobjects[object].create_kits_from_kits_offsets(self.staticobjects[source_id].childs, template)
                template = 'cpname_ramiel_aas128_insmain_prison_pkm'
                print(self.staticobjects[object].generate_template_output())
                print(self.staticobjects[object].generate_gpo_output())
        
    def get_source_id(self):
        for object_id in self.staticobjects:
            if self.staticobjects[object_id].is_source():
                return object_id
        
        
if __name__ == '__main__':
    calc = Calculator()
    calc.main()