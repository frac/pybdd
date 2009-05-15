from pybdd.feature_structure import FeatureStructure


FEATURE_MARKER = "Feature:"


class Parser(object):
    def __init__(self):
        self.iden = 0
    
    def process(self, content):
        self.lines = [line.strip() for line in content.split("\n") if len(line)]
        self.structure = FeatureStructure()
        self._process_line()

    def _process_line(self):
       for line in self.lines:
            if ( self._is_feature_name_line(line) ):
                self.structure.add_feature_name(line)
                print self.structure.feature_name

    def _is_feature_name_line(self, line):
        if line.startswith(FEATURE_MARKER):
            return True
        return False
        
            

