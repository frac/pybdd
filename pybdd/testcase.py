from pybdd.exceptions import ConfigFileException
from pybdd.parser import Parser

class Testcase(object):
    def __init__(self, filename):
        self.filename = filename
        

    def run(self):
        """ try to read, parse and execute the testcase """

        print "running filename %s" % self.filename
        try:
            structure = Parser().process( open(self.filename, 'r').read() )
        except:
            raise ConfigFileException("file not found  %s" % self.filename)





        return 1

    
