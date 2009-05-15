

class Testcase(object):
    def __init__(self, file):
        self.file = file

    def run(self):
        print "running file %s" % self.file
        return 1
