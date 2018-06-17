import math

def sph2xyz(az,va,d):
#% SPH2XYZ  Converts spherical coordinates to Cartesian
#%   coordinates in a left-handed (local geodetic) system.
#%   Vetorized. See also XYZ2SPH.
#% Version: 7 Jul 96
#% Useage:  [x,y,z]=sph2xyz(az,va,d)
#% Input:  az - vector of azimuths (radians)
#%         va - vector of vertical angles (radians)
#%         d  - vector of distances (linear units)
#% Output: x \
#%         y  > cartesian coordinates (linear units)
#%         z /
#
#% Copyright (c) 2011, Michael R. Craymer
#% All rights reserved.
#% Email: mike@craymer.com

    sinv = math.sin(va);
    cosv = math.cos(va);
    sina = math.sin(az);
    cosa = math.cos(az);
    x    = d*cosv*cosa;
    y    = d*cosv*sina;
    z    = d*sinv;

    return(x,y,z)