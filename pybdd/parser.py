from pybdd.feature_structure import FeatureStructure, Scenario, Step
from pybdd.constants import FEATURE_MARKER, SCENARIO_MARKER



class Parser(object):
    def __init__(self):
        self.iden = 0
        self._in_scenario = False
        self._active_scenario = ""
    
    def process(self, content):
        self.lines = [line.strip() for line in content.split("\n") if len(line)]
        self.structure = FeatureStructure()
        self._process_line()
        return self.structure

    def _process_line(self):
       for line in self.lines:
            if ( self._is_feature_name_line(line) ):
                self.structure.add_feature_name(line)
            if ( self._is_scenario_name_line(line) ):
                self._active_scenario = Scenario()
                #### AP PARKED HERE
                self.structure.add_feature_name(line)



            else (  self._is_feature_desc(line) ):
                self.structure.add_feature_desc(line)


    def _is_feature_name_line(self, line):
        if line.startswith(FEATURE_MARKER):
            return True
        return False
    def _is_scenario_name_line(self, line):
        if line.startswith(SCENARIO_MARKER):
            self._in_scenario = True
            return True
        return False


    def _is_feature_desc(self, line):
        return not self._in_scenario
        
            

