import numpy

def cal2jd(year, month, day):
#% CAL2JD  Converts calendar date to Julian date using algorithm
#%   from "Practical Ephemeris Calculations" by Oliver Montenbruck
#%   (Springer-Verlag, 1989). Uses astronomical year for B.C. dates
#%   (2 BC = -1 year). Non-vectorized version. See also DOY2JD, GPS2JD,
#%   JD2CAL, JD2DOW, JD2DOY, JD2GPS, JD2YR, YR2JD.
#% Version: 1999-04-24
#% Usage:   jd=cal2jd(year,month,day)
#% Input:   year - calendar year (4-digit including century)
#%          month - calendar month
#%          day - calendar day (including factional day)
#% Output:  jd - jJulian date
#
#% Copyright (c) 2011, Michael R. Craymer
#% All rights reserved.
#% Email: mike@craymer.com

    month_with_less_than_31_days = [3, 5, 9, 11]
    jd = -1

    if (month < 1) or (month > 12):
        print('Invalid input month')
        return jd

    if day < 1:
        # disable for only one line
        if ((month == 2 & day > 29) or
                ((month in month_with_less_than_31_days) and day > 30) or
                (day > 31)):
            print('Invalid input day')
            return jd

    if month > 2:
        y = year
        m = month
    else:
        y = year - 1
        m = month + 12

    date1 = 4+31*(10+12*1582)  # Last day of Julian calendar (1582.10.04)
    date2 = 15+31*(10+12*1582)  # First day of Gregorian calendar (1582.10.15)
    date = day+31*(month+12*year)

    if date <= date1:
        b = -2
    elif date >= date2:
        b = numpy.fix(y/400) - numpy.fix(y/100)
    else:
        print('Dates between October 5 & 15, 1582 do not exist')
        return jd

    if y > 0:
        jd = numpy.fix(365.25*y) + numpy.fix(30.6001*(m+1)) + b + 1720996.5 + day
    else:
        jd = numpy.fix(365.25*y-0.75) + numpy.fix(30.6001*(m+1)) + b + 1720996.5 + day

    return jd
