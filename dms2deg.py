import math

def dms2deg(dms):
#% DMS2DEG  Converts degrees-minutes-seconds to decimal degrees.
#%   Vectorized.
#% Version: 12 Mar 00
#% Useage:  deg=dms2deg(dms)
#% Input:   dms - [d m s] array of angles in deg-min-sec, where
#%                d = vector of degrees
#%                m = vector of minutes
#%                s = vector of seconds
#% Output:  deg - vector of angles in decimal degrees

#% Copyright (c) 2011, Michael R. Craymer
#% All rights reserved.
#% Email: mike@craymer.com

    d = dms[0]
    m = dms[1]
    s = dms[2]
    deg = math.fabs(d)+math.fabs(m)/60+math.fabs(s)/3600

    if (d < 0 or m < 0 or s < 0):
        deg = -deg

    return deg
