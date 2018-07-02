import numpy

def cal2jd(year, mn, dy):
#% CAL2JD  Converts calendar date to Julian date using algorithm
#%   from "Practical Ephemeris Calculations" by Oliver Montenbruck
#%   (Springer-Verlag, 1989). Uses astronomical year for B.C. dates
#%   (2 BC = -1 year). Non-vectorized version. See also DOY2JD, GPS2JD,
#%   JD2CAL, JD2DOW, JD2DOY, JD2GPS, JD2YR, YR2JD.
#% Version: 1999-04-24
#% Usage:   jd=cal2jd(year,mn,dy)
#% Input:   year - calendar year (4-digit including century)
#%          mn - calendar month
#%          dy - calendar day (including factional day)
#% Output:  jd - jJulian date
#
#% Copyright (c) 2011, Michael R. Craymer
#% All rights reserved.
#% Email: mike@craymer.com

    monthWithLessThan31Days = [3, 5, 9, 11]

    if (mn < 1) or (mn > 12):
        print('Invalid input month')
        return

    if (dy < 1):
        if (mn == 2 & dy > 29) or ((mn in monthWithLessThan31Days) and dy > 30) or (dy > 31):
            print('Invalid input day')
            return

    if (mn > 2):
        y = year
        m = mn
    else:
        y = year - 1
        m = mn + 12

    date1 =  4+31*(10+12*1582)  # Last day of Julian calendar (1582.10.04)
    date2 = 15+31*(10+12*1582)  # First day of Gregorian calendar (1582.10.15)
    date  = dy+31*(mn+12*year)

    if (date <= date1):
        b = -2
    elif (date >= date2):
        b = numpy.fix(y/400) - numpy.fix(y/100)
    else:
        print('Dates between October 5 & 15, 1582 do not exist')
        return

    if (y > 0):
        jd = numpy.fix(365.25*y) + numpy.fix(30.6001*(m+1)) + b + 1720996.5 + dy
    else:
        jd = numpy.fix(365.25*y-0.75) + numpy.fix(30.6001*(m+1)) + b + 1720996.5 + dy

    return (jd)