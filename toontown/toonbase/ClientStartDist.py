#Embedded file name: toontown.toonbase.ClientStartDist
import sys
import __builtin__
import collections
collections.namedtuple = lambda *x: list
__builtin__.__dev__ = False

def __runfunc(*args, **kw):
    print 'Something Spoopys Happened!'


__builtin__.__dict__.update(__import__('pandac.PandaModules', fromlist=['*']).__dict__)
import toontown.toonbase.DCImporter
