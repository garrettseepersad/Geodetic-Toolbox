import numpy
import sys
from cal2jd import cal2jd
from doy2jd import doy2jd

def yr2jd(year):
#% YR2JD  Converts year and decimal of year to Julian date.
#% . Non-vectorized version. See also CAL2JD, DOY2JD,
#%   GPS2JD, JD2CAL, JD2DOW, JD2DOY, JD2GPS, YR2JD
#% Version: 24 Apr 99
#% Usage:   jd=yr2jd(year)
#% Input:   year - year and decimal of year
#% Output:  jd - Julian date
#
#% Copyright (c) 2011, Michael R. Craymer
#% All rights reserved.
#% Email: mike@craymer.com

    iyr   = numpy.fix(year)
    jd0   = cal2jd(iyr,1,1)
    days  = cal2jd(iyr+1,1,1) - jd0
    doy   = (year-iyr)*days + 1
    jd    = doy2jd(iyr,doy)

    return (jd)
