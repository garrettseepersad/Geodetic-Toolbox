from cal2jd import cal2jd

def doy2jd(year,doy):
#% DOY2JD  Converts year and day of year to Julian date.
#% . Non-vectorized version. See also CAL2JD, GPS2JD,
#%   JD2CAL, JD2DOW, JD2DOY, JD2GPS, JD2YR, YR2JD.
#% Version: 24 Apr 99
#% Usage:   jd=doy2jd(year,doy)
#% Input:    year - year
#%          doy - day of year
#% Output:  jd  - Julian date
#
#% Copyright (c) 2011, Michael R. Craymer
#% All rights reserved.
#% Email: mike@craymer.com

    jd = cal2jd(year,1,0) + doy
    return (jd)
