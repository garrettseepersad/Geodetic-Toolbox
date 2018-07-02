import math

def xyz2ell3(X,Y,Z,a,b,e2):
#% XYZ2ELL3  Converts cartesian coordinates to ellipsoidal.
#%   Uses direct algorithm in B.R. Bowring, "The accuracy of
#%   geodetic latitude and height equations", Survey
#%   Review, v28 #218, October 1985, pp.202-206.  Vectorized.
#%   See also XYZ2ELL, XYZ2ELL2.
#% Version: 2011-02-19
#% Useage:  [lat,lon,h]=xyz2ell3(X,Y,Z,a,b,e2)
#%          [lat,lon,h]=xyz2ell3(X,Y,Z)
#% Input:   X \
#%          Y  > vectors of cartesian coordinates in CT system (m)
#%          Z /
#%          a   - ref. ellipsoid major semi-axis (m) default GRS80
#%          b   - ref. ellipsoid minor semi-axis (m) default GRS80
#%          e2  - ref. ellipsoid eccentricity squared default GRS80
#% Output:  lat - vector of ellipsoidal latitudes (radians)
#%          lon - vector of ellipsoidal longitudes (radians)
#%          h   - vector of ellipsoidal heights (m)
#
#% Copyright (c) 2011, Michael R. Craymer
#% All rights reserved.
#% Email: mike@craymer.com

    lon  = math.atan2(Y,X)
    e    = e2*(a/b)^2
    p    = math.sqrt(X*X+Y*Y)
    r    = math.sqrt(p*p+Z*Z)
    u    = math.atan(b*Z*(1+e*b/r)/(a*p))
    lat  = math.atan((Z+e*b*math.sin(u)^3)/(p-e2*a*math.cos(u)^3))
    v    = a/math.sqrt(1-e2*math.sin(lat)^2)
    h    = p*math.cos(lat)+Z*math.sin(lat)-a*a/v

    return (lat,lon,h)