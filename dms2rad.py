import math

def dms2rad(dms):
#% DMS2RAD  Converts degrees-minutes-seconds to radians.
#%   Vectorized.
#% Version: 12 Mar 00
#% Useage:  rad=dms2rad(dms)
#% Input:   dms - [d m s] array of angles in deg-min-sec, where
#%                d = vector of degrees
#%                m = vector of minutes
#%                s = vector of seconds
#% Output: rad - vector of angles in radians
#
#% Copyright (c) 2011, Michael R. Craymer
#% All rights reserved.
#% Email: mike@craymer.com

    d   = dms[0];
    m   = dms[1];
    s   = dms[2];
    dec = math.fabs(d)+math.fabs(m)/60+math.fabs(s)/3600;
    rad = dec*math.pi/180;
    
    if (d<0 or m<0 or s<0):
        rad = -rad;

    return (rad)