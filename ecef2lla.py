import math

def ecef2lla(x,y,z):

    #% ECEF2LLA - convert earth-centered earth-fixed (ECEF)
    #%            cartesian coordinates to latitude, longitude,
    #%            and altitude
    #%
    #% USAGE:
    #% [lat,lon,alt] = ecef2lla(x,y,z)
    #%
    #% lat = geodetic latitude (radians)
    #% lon = longitude (radians)
    #% alt = height above WGS84 ellipsoid (m)
    #% x = ECEF X-coordinate (m)
    #% y = ECEF Y-coordinate (m)
    #% z = ECEF Z-coordinate (m)
    #%
    #% Notes: (1) This function assumes the WGS84 model.
    #%        (2) Latitude is customary geodetic (not geocentric).
    #%        (3) Inputs may be scalars, vectors, or matrices of the same
    #%            size and shape. Outputs will have that same size and shape.
    #%        (4) Tested but no warranty; use at your own risk.
    #%        (5) Michael Craymer, April 2006
    
    #% WGS84 ellipsoid constants
    a = 6378137;
    e = 8.1819190842622e-2;

    #% calculations
    b   = math.sqrt(a**2*(1-e**2));
    ep  = math.sqrt((a**2-b**2)/b**2);
    p   = math.sqrt(x**2+y**2);
    th  = math.atan2(a*z,b*p);
    lon = math.atan2(y,x);
    lat = math.atan2((z+ep**2*b*math.sin(th)**3),(p-e**2*a*math.cos(th)**3));
    N   = a/math.sqrt(1-e**2.*math.sin(lat)**2);
    alt = p/math.cos(lat)-N;

    #% return lon in range [0,2*pi)
    lon = math.fmod(lon,2*pi);

    #% correct for numerical instability in altitude near exact poles:
    #% (after this correction, error is about 2 millimeters, which is about
    #% the same as the numerical precision of the overall function)

    k   = math.fabs(x)<1 and math.fabs(y)<1;
    alt = math.fabs(z)-b;
    
    return (lat,lon,alt)

