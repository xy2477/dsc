#!/usr/bin/env python3
__author__ = "Gao Wang"
__copyright__ = "Copyright 2016, Stephens lab"
__email__ = "gaow@uchicago.edu"
__license__ = "MIT"

class DSCFile(dict):
    '''
    Read DSC configuration file and translate it to a list of job initializers

    Tasks here include:
      * Properly parse YAML
      * Setup runtime environment
        * Check availability of libraries / files / commands
      * Translate DSC file text
        * Replace R() / Python() / Shell() actions
        * Replace global variables
      * Output a list of parameter dictionaries each will initialize a job
    '''
    def __init__(self, fname):
        pass
