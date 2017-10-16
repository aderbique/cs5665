from collections import namedtuple
from pprint import pprint as pp
#pulled from rosetta code. planning to use as base for stem plot
from math import floor
 
 
def StemAndLeafPlot(v):
    d = []
    interval = int(10**int(v.leafdigits))
    for data in sorted(v.data):
        data = int(floor(data))
        stm, lf = divmod(data,interval)
        d.append( (int(stm), int(lf)) )
    stems, leafs = list(zip(*d))
    stemwidth = max(len(str(x)) for x in stems)
    leafwidth = max(len(str(x)) for x in leafs)
    laststem, out = min(stems) - 1, []
    for s,l in d:
        while laststem < s:
            laststem += 1
            out.append('\n%*i |' % ( stemwidth, laststem))
        out.append(' %0*i' % (leafwidth, l))
    out.append('\n\nKey:\n Stem multiplier: %i\n X | Y  =>  %i*X+Y\n'
               % (interval, interval))
    return ''.join(out)
 
if __name__ == '__main__':
    print( stemplot(data0) )
