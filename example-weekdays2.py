#!/usr/bin/env python

from texttable import *
import datetime

data = [];

# find next Sunday
d = datetime.date.today()
while d.weekday() != 6:
    d += datetime.timedelta(1)


for i in range(0, 7):
    # note:  we use ttrow instead of dict because ttrow preserves initial order.
    row = ttrow()
    row['Day']    = d.strftime('%A')
    row['Abbrev'] = d.strftime('%a')
    row['Initial'] = d.strftime('%A')[0]
    row['Position'] = i

    data.append( row )
    d += datetime.timedelta(1)

print data
print "  [  Table with header from first row keys. ]\n";
print texttable.table( data );


# Now we will do the same thing, but init the ttrow with tuples instead.
data = []
for i in range(0, 7):
    row = ttrow( (('Day',      d.strftime('%A') ),
                  ('Abbrev',   d.strftime('%a') ),
                  ('Initial',  d.strftime('%A')[0] ),
                  ('Position', i ))
                )
    data.append( row )
    d += datetime.timedelta(1)


print data
print "  [  Same thing, but initialized ttrow dict with tuples. ]\n";
print texttable.table( data );

