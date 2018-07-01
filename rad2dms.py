import math

def rad2dms(rad):
#% RAD2DMS  Converts radians to degrees-minutes-seconds. Vectorized.
#% Version: 12 Mar 00
#% Useage:  dms=rad2dms(rad)
#% Input:   rad - vector of angles in radians
#% Output:  dms - [d m s] array of angles in deg-min-sec, where
#%                d = vector of degrees
#%                m = vector of minutes
#%                s = vector of seconds

#% Copyright (c) 2011, Michael R. Craymer
#% All rights reserved.
#% Email: mike@craymer.com

    d   = math.fabs(rad)*(180/math.pi);
    id  = math.floor(d);
    rm  = (d-id)*60;
    im  = math.floor(rm);
    s   = (rm-im)*60;

    if rad<0:
      if id==0:
        if im==0:
          s = -s;
        else:
          im = -im;
      else:
        id = -id;

    #ind=(rad<0 & id~=0);
    #id(ind)=-id(ind);

    #ind=(rad<0 & id==0 & im~=0);
    #im(ind)=-im(ind);

    #ind=(rad<0 & id==0 & im==0);
    #s(ind)=-s(ind);

    dms=[id, im, s];

    return dms