

class FeatureStructure(object):
    def __init__(self):
        self.feature_name = ""
        self.feature_desc = []
    def add_feature_name(self, name):
        if self.feature_name: 
            raise Exception("feature name have already been defined")

        self.feature_name = name.split(":")[1].strip()
