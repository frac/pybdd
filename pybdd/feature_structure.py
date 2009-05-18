from pybdd.utils import slug_me

class FeatureStructure(object):
    def __init__(self):
        self.feature_name = ""
        self.feature_desc = []
    def add_feature_name(self, name):
        if self.feature_name: 
            raise Exception("feature name have already been defined")
        self.feature_name = slug_me(name)
        self.feature_desc.append(name)
    def add_feature_desc(self, line):
        self.feature_desc.append( line.strip() )
