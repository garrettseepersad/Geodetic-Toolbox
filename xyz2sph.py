import math

def xyz2sph(x,y,z):
#% XYZ2SPH  Converts Cartesian coordinates in a left-handed
#%   (local geodetic) system to spherical coordinates.
#%   Vectorized.  See also SPH2XYZ.
#% Version: 7 Jul 96
#% Useage: [az,va,d]=xyz2sph(x,y,z)
#% Input:  x \
#%         y  > vectors of cartesian coordinates (linear units)
#%         z /
#% Output: az - vector of azimuths (radians)
#%         va - vector of vertical angles (radians)
#%         d  - vector of distances (linear units)
#
#% Copyright (c) 2011, Michael R. Craymer
#% All rights reserved.
#% Email: mike@craymer.com

    d   = math.sqrt(x*x+y*y+z*z)
    az  = math.atan2(y,x)
    #az = math.atan(y./x)
    #az = az+(x<0)*math.pi     # 2nd & 3rd quad
    #az = az+(az<0)*2*math.pi  # 4th quad
    va  = math.asin(z/d)

    return(az,va,d)