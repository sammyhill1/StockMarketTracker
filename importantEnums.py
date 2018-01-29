from enum import Enum

class reportIntervals(Enum):
    min1    = 0
    min5    = 1
    min15   = 2
    min30   = 3
    min60   = 4
    daily   = 5
    weekly  = 6
    monthly = 7

class outputSizes(Enum):
    compact = 0
    full    = 1

class dataTypes(Enum):
    json = 0
    csv  = 1
