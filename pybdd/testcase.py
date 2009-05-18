from pybdd.exceptions import ConfigFileException
from pybdd.parser import Parser

class Testcase(object):
    def __init__(self, filename):
        self.filename = filename
        

    def run(self):
        """ try to read, parse and execute the testcase """

        print "running filename %s" % self.filename
        #try:
        structure = Parser().process( open(self.filename, 'r').read() )
        #except:
        #    raise ConfigFileException("file not found  %s" % self.filename)

        try: 
            module_list = __import__ ('steps.%s'% structure.feature_name)
        except ImportError:
            print """
steps file no found

if you have not done already:
    create a steps dir:
        mkdir steps
        cd steps
    create the __init__.py:
        touch __init__.py


create and edit the steps file:
    
    vi %s.py

It can be done in other editors.. pretty sure even emacs could do it :)

>>>
#coding:utf8
from pybdd.testcase import Testcase

class %s(Testcase):
    pass

""" % ( structure.feature_name, structure.feature_name )


        try: 
            test_module = getattr( module_list, structure.feature_name )
            print test_module
        except AttributeError:
            print """
make sure that the file %s.py has at least the following:

>>>
#coding:utf8
from pybdd.testcase import Testcase

class %s(Testcase):
    pass

            """ % ( structure.feature_name, structure.feature_name )

        for scenario in test_module.scenarios:
            print scenario


        return 1

    
