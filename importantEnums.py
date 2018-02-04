from enum import Enum, unique

@unique
class reportIntervals(Enum):
    min1    = 0
    min5    = 1
    min15   = 2
    min30   = 3
    min60   = 4
    daily   = 5
    weekly  = 6
    monthly = 7

@unique
class outputSizes(Enum):
    compact = 0
    full    = 1

@unique
class dataTypes(Enum):
    json = 0
    csv  = 1

@unique
class activityType(Enum):
    buy = 0
    sell = 1
