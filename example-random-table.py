#!/usr/bin/env python

from texttable import *
from random import randint

data = []

numcols = randint(2,6)
for i in range(0, 20-1):
    row = {}
    for j in range(0, numcols-1):
        buf = ''
        if( randint(0, 60) == 0):
            buf = str(randint( 0, 10000 ))
        key = 'col-' + str(j+1)
        row[key] = buf + str(randint(0, 1000))
    data.append( row )

headertypes = [ 'keys', 'firstrow', 'none']
headertype = headertypes[randint(0, len( headertypes) - 1)]

footertypes = [ 'keys', 'lastrow', 'none']
footertype = footertypes[randint(0, len( footertypes) - 1)]

print texttable.table( data, headertype, footertype )

print "headertype: " + headertype
print "footertype: " + footertype