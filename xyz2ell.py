import math

def XYZ2ELL(X,Y,Z,a,e2):
# XYZ2ELL  Converts cartesian coordinates to ellipsoidal.
#   Uses iterative alogithm.  Vectorized.  See also XYZ2ELL2,
#   XYZ2ELL3.
# Version: 2011-02-19
# Useage:  [lat,lon,h]=xyz2ell(X,Y,Z,a,e2)
#          [lat,lon,h]=xyz2ell(X,Y,Z)
# Input:   X \
#          Y  > vectors of cartesian coordinates in CT system (m)
#          Z /
#          a   - ref. ellipsoid major semi-axis (m) default GRS80
#          e2  - ref. ellipsoid eccentricity squared default GRS80
# Output:  lat - vector of ellipsoidal latitudes (radians)
#          lon - vector of ellipsoidal longitudes (radians)
#          h   - vector of ellipsoidal heights (m)
#
# Copyright (c) 2011, Michael R. Craymer
# All rights reserved.
# Email: mike@craymer.com

# Note
# Currently isn't vector wise

    elat = 1.e-12
    eht  = 1.e-5
    p    = math.sqrt(X*X+Y*Y)
    xlat = math.atan2(Z,p/(1-e2))
    h    = 0
    dh   = 1
    dlat = 1

    while (dlat>elat) or (dh>eht):
      lat0 = lat
      h0   = h
      v    = a/sqrt(1-e2*math.sin(lat)*math.sin(lat))
      h    = p/cos(lat)-v
      lat  = math.atan2(Z, p*(1-e2*v/(v+h)))
      dlat = abs(lat-lat0)
      dh   = abs(h-h0)

    lon    = math.atan2(Y,X)

    return lat, lon, h