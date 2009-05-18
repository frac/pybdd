from pybdd.feature_structure import FeatureStructure
from pybdd.constants import FEATURE_MARKER



class Parser(object):
    def __init__(self):
        self.iden = 0
        self._in_scenario = False
    
    def process(self, content):
        self.lines = [line.strip() for line in content.split("\n") if len(line)]
        self.structure = FeatureStructure()
        self._process_line()
        return self.structure

    def _process_line(self):
       for line in self.lines:
            if ( self._is_feature_name_line(line) ):
                self.structure.add_feature_name(line)
            elif (  self._is_feature_desc(line) ):
                self.structure.add_feature_desc(line)


    def _is_feature_name_line(self, line):
        if line.startswith(FEATURE_MARKER):
            return True
        return False

    def _is_feature_desc(self, line):
        return not self._in_scenario
        
            

