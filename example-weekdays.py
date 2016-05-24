#!/usr/bin/env python

from texttable import *

data = [
['Weekday', 'Abbrev', 'Initial', 'Position'],
['Sunday', 'Sun', 'S', '0'],
['Monday', 'Mon', 'M', '1'],
['Tuesday', 'Tue', 'T', '2'],
['Wednesday', 'Wed', 'W', '3'],
['Thursday', 'Thu', 'T', '4'],
['Friday', 'Fri', 'F', '5'],
['Saturday', 'Sat', 'S', '6']
];

print "  [  Table with header from first row values ]\n"
print texttable.table( data, headertype = 'firstrow' )

# Display header from keys instead.  ( default behavior )
footer = data.pop(0)  # remove first and second row.
data.pop(0)
data.insert(0, ttrow( (('weekday', 'Sunday'), ('abbrev', 'Sun'), ('initial', 'S'), ('position', 0)) ) )
print "\n\n  [ Example 2.  Table with header generated from ttrow keys ]\n"
print texttable.table( data )

# Add a footer row), same as header), but displaying values instead of keys.
data.append(footer)
print "\n\n  [ Example 3.  Table with header (ttrow keys) and footer ( array vals ) ]\n"
print texttable.table( data, headertype = 'keys', footertype = 'lastrow' )

