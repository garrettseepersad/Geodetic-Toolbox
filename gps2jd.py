from cal2jd import cal2jd

def gps2jd(gpsweek, sow, rollover):
#% GPS2JD  Converts GPS week number (since 1980.01.06) and
#%   seconds of week to Julian date. Non-vectorized version.
#%   See also CAL2JD, DOY2JD, JD2CAL, JD2DOW, JD2DOY, JD2GPS,
#%   JD2YR, YR2JD.
#% Version: 28 Sep 03
#% Usage:   jd=gps2jd(gpsweek,sow,rollover)
#% Input:   gpsweek  - GPS week number
#%          sow      - seconds of week since 0 hr, Sun (default=0)
#%          rollover - number of GPS week rollovers (default=0)
#% Output:  jd       - Julian date
#
#% Copyright (c) 2011, Michael R. Craymer
#% All rights reserved.
#% Email: mike@craymer.com

    jd = -1

    if gpsweek <= 0:
        print('GPS week must be greater than or equal to zero')
        return jd

    jdgps = cal2jd(1980, 1, 6)             # beginning of GPS week numbering
    nweek = gpsweek + 1024*rollover      # account for rollovers every 1024 weeks
    jd = jdgps + nweek*7 + sow/3600/24
    return jd
