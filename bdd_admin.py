#!/usr/bin/python



import os, sys, optparse
from pybdd.core import Core

__doc__ = "pyBdd"

def main():
    """ Main function - parses args and runs action """
    parser = optparse.OptionParser(usage="%prog or type %prog -h (--help) for help", description=__doc__, version="%prog")

    parser.add_option("-f", "--file", dest="file", default="", help="file to test [default: %default].")

    (options, args) = parser.parse_args()


    bdd = Core()

    result = bdd.run_tests()

    sys.exit(result)

if __name__ == "__main__":
    main()
    
