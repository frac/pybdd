from pybdd.utils import slug_me

TYPE_GIVEN = 0
TYPE_WHEN = 1
TYPE_THEN = 2

class Step(object):
    def __init__(self):
        self.name = ""
        self.desc = ""
        self.type = -1

    def add_name(self, name, type):

        self.name = slug_me(name)
        self.desc = name
        self.type = type
    

class Scenario(object):
    def __init__(self):
        self.name = ""
        self.desc = ""
        self.steps = []

    def add_name(self, name):
        self.name = slug_me(name)
        self.desc = name

    def add_steps(self,step):
        self.steps.append(step)

    

class FeatureStructure(object):
    def __init__(self):
        self.feature_name = ""
        self.feature_desc = []
        self.scenarios = []
    def add_feature_name(self, name):
        if self.feature_name: 
            raise Exception("feature name have already been defined")
        self.feature_name = slug_me(name)
        self.feature_desc.append(name)
    def add_feature_desc(self, line):
        self.feature_desc.append( line.strip() )

    def add_scenario(self, scenario)
        self.scenarios.append(scenario)
        

