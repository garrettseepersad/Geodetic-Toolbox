# Geodetic Toolbox  
  
###### Angle Conversions  
- [x] deg2rad   - Degrees to radians  
- [x] dms2deg   - Degrees,minutes,seconds to degrees  
- [x] dms2rad   - Degrees,minutes,seconds to radians  
- [x] rad2deg   - Radians to degrees  
- [x] rad2dms   - Radians to degrees,minutes,seconds  
- [x] rad2sec   - Radians to seconds  
- [x] sec2rad   - Seconds to radians  
  
###### Coordinate Conversions  
- [x] ell2utm   - Ellipsoidal (lat,long) to UTM (N,E) coordinates  
- [x] ell2xyz   - Ellipsoidal (lat,long) to Cartesian (x,y,z) coodinates  
- [x] sph2xyz   - Shperical (az,va,dist) to Cartesian (x,y,z) coordinates  
- [x] xyz2sph   - Cartesian (x,y,z) to spherical (az,va,dist) coordinates  
- [x] xyz2ell   - Cartesian (x,y,z) to ellipsoidal (lat,long,ht) coordinates  
- [x] xyz2ell2  - xyz2ell with Bowring height formula  
- [x] xyz2ell3  - xyz2ell using complete Bowring version  
- [x] ecef2lla  -
  
###### Coordinate Transformations  
- [ ] refell    - Reference ellipsoid definition  
- [ ] ellradii  - Various radii of curvature  
- [ ] cct2clg   - Conventional terrestrial to local geodetic cov. matrix  
- [ ] clg2cct   - Local geodetic to conventional terrestrial cov. matrix  
- [ ] ct2lg     - Conventional terrestrial (ECEF) to local geodetic (NEU)  
- [ ] dg2lg     - Differences in Geodetic (lat,lon) to local geodetic (NEU)  
- [ ] lg2ct     - Local geodetic (NEU) to conventional terrestrial (ECEF)  
- [ ] lg2dg     - Local geodetic (NEU) to differences in geodetic (lat,lon)  
- [ ] direct    - Direct geodetic problem (X1,Y1,Z1 + Az,VA,Dist to X2,Y2,Z2)  
- [ ] inverse   - Inverse geodetic problem (X1,Y1,Z1 + X2,Y2,Z2 to Az,VA,Dist)  
- [ ] simil     - Similarity transformation (translation,rotation,scale change)  
  
###### Date Conversions  
- [x] cal2jd    - Calendar date to Julian date  
- [ ] dates     - Converts between different date formats  
- [x] doy2jd    - Year and day of year to Julian date  
- [x] gps2jd    - GPS week & seconds of week to Julian date  
- [x] jd2cal    - Julian date to calendar date  
- [x] jd2dow    - Julian date to day of week  
- [x] jd2doy    - Julian date to year & day of year  
- [ ] jd2gps    - Julian date to GPS week & seconds of week  
- [ ] jd2mjd    - Julian date to Modified Julian date  
- [ ] jd2yr     - Julian date to year & decimal year  
- [ ] mjd2jd    - Modified Julian date to Julian date  
- [x] yr2jd     - Year & decimal year to Julian date  
  
###### Error Ellipses  
- [ ] errell2   - Computes error ellipse semi-axes and azimuth  
- [ ] errell3   - Computes error ellipsoid semi-axes, azimuths, inclinations  
- [ ] plterrel  - Plots error ellipse for covariance matrix  
  
###### Miscellaneous  
- [ ] findfixed - Finds fixed station based on 3D covariance matrix  
- [ ] pltnet    - Plots network of points with labels  
  
###### Example Scripts  
  
- [ ] DirInv    - Simple partial GUI script for direct and inverse problems  
- [ ] DirProb   - Example of direct problem  
- [ ] Dist3D    - Example to compute incremental 3D distances between points.  
- [ ] InvProb   - Example of inverse problem  
- [ ] PltNetEl  - Example plot of network error ellipses  
- [ ] ToUTM     - Example of conversion from latitude,longitude to UTM  
  
  
###### Limitations:  
- [ ] No vector wise multiplication  
  
###### Ideas:  
- [ ] Could link multiple files to an import : https://www.reddit.com/r/learnpython/comments/5odyok/one_function_per_file/  
  
