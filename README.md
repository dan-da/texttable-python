# texttable-python

A handy python class for printing fixed-width text tables.
( ported to python from [texttable-php](https://github.com/dan-da/texttable-php) ) 

Let's see a couple examples, shall we?

## Example Price History Report ( from [bitprices](https://github.com/dan-da/bitprices) )

```
+------------+------------------+-----------+-------------+----------------+---------------+----------+
| Date       | BTC Amount       | USD Price | USD Amount  | USD Amount Now | USD Gain      | Type     |
+------------+------------------+-----------+-------------+----------------+---------------+----------+
| 2011-11-16 |  500000.00000000 |      2.46 |  1230000.00 |   189905000.00 |  188675000.00 | purchase |
| 2011-11-16 | -500000.00000000 |      2.46 | -1230000.00 |  -189905000.00 | -188675000.00 | sale     |
| 2013-11-26 |       0.00011000 |    913.95 |        0.10 |           0.04 |         -0.06 | purchase |
| 2013-11-26 |      -0.00011000 |    913.95 |       -0.10 |          -0.04 |          0.06 | sale     |
| 2014-11-21 |       0.00010000 |    351.95 |        0.04 |           0.04 |          0.00 | purchase |
| 2014-12-09 |       0.00889387 |    353.67 |        3.15 |           3.38 |          0.23 | purchase |
| 2015-06-05 |       0.44520000 |    226.01 |      100.62 |         169.09 |         68.47 | purchase |
| 2015-06-07 |       0.44917576 |    226.02 |      101.52 |         170.60 |         69.08 | purchase |
| 2015-10-17 |       0.00010000 |    270.17 |        0.03 |           0.04 |          0.01 | purchase |
| 2015-11-05 |       0.00010000 |    400.78 |        0.04 |           0.04 |          0.00 | purchase |
| Totals:    |       0.90356963 |           |      205.40 |         343.19 |        137.79 |          |
+------------+------------------+-----------+-------------+----------------+---------------+----------+
```

## Days of the week.  From ./example-weekdays2.py

```
+-----------+--------+---------+----------+
| Day       | Abbrev | Initial | Position |
+-----------+--------+---------+----------+
| Sunday    | Sun    | S       |        0 |
| Monday    | Mon    | M       |        1 |
| Tuesday   | Tue    | T       |        2 |
| Wednesday | Wed    | W       |        3 |
| Thursday  | Thu    | T       |        4 |
| Friday    | Fri    | F       |        5 |
| Saturday  | Sat    | S       |        6 |
+-----------+--------+---------+----------+
```


# Usage.

There are no dependencies!  works with python 2.7+

Simply import texttable.py from any python file and call texttable.table() with
an array of rows.

Here's the method definition.

```
class texttable:
    # Formats a fixed-width text table, with borders.
    #
    # param rows  array of rows.  each row contains array or ttrow (key/val)
    # param headertype  keys | firstrow | none/None 
    # param footertype  keys | lastrow | none/None
    # param empty_row_string  String to use when there is no data, or None.
    @classmethod
    def table( cls, rows, headertype = 'keys', footertype = 'none', empty_row_string = 'No Data' ):
```

Here's a trivial example that prints info about the days of the week:

```
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
```

## Table rows: arrays, dicts, ttrow

The data structure that texttable.table() expects is an array of rows.

Each row can be either an array, dict, or ttrow.

In general, either array or ttrow should be used and dict should be avoided
because it does not preserve the initial ordering.

ttrow is a subclass of collections.OrderedDict. It is useful is when it is
desired to use a dict's keys as column header (or footer) labels.

If headertype param is 'keys', then the first row must be a dict or ttrow else
the header will not be displayed.

Likewise if the footertype param is 'keys', then the last row must be a dict or
ttrow else the footer will not be displayed.
