import math

def  ell2xyz(lat, lon, h, a, e2):
#% ELL2XYZ  Converts ellipsoidal coordinates to cartesian.
#%   Vectorized.
#% Version: 2011-02-19
#% Useage:  [x,y,z]=ell2xyz(lat,lon,h,a,e2)
#%          [x,y,z]=ell2xyz(lat,lon,h)
#% Input:   lat - vector of ellipsoidal latitudes (radians)
#%          lon - vector of ellipsoidal E longitudes (radians)
#%          h   - vector of ellipsoidal heights (m)
#%          a   - ref. ellipsoid major semi-axis (m) default GRS80
#%          e2  - ref. ellipsoid eccentricity squared default GRS80
#% Output:  x \
#%          y  > vectors of cartesian coordinates in CT system (m)
#%          z /
#
#% Copyright (c) 2011, Michael R. Craymer
#% All rights reserved.
#% Email: mike@craymer.com

    v = a/math.sqrt(1-e2*math.sin(lat)*math.sin(lat))
    x = (v+h)*math.cos(lat)*math.cos(lon)
    y = (v+h)*math.cos(lat)*math.sin(lon)
    z = (v*(1-e2)+h)*math.sin(lat)

    return(x, y, z)
