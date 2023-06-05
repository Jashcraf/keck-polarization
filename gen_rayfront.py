from poke.poke_core import Rayfront
from poke.writing import write_rayfront_to_serial
from poke.poke_math import np

# set up the file
pth = 'C:/Users/UASAL-OPTICS/Desktop/keck-polarization/raytraces/keck_orkid.zmx'

# user params
nrays = 64
wvl = 633e-9
pupil_radius = 10950/2
max_fov = 0.01670
coat = 0.4 + 1j*7
a = np.array([0.9781476007,-0.2079116908, 0.0000000000])
ap = np.array([0.9851019261,-0.1719714953, 0.0000000000]) # ray from edge of pupil
x = np.cross(a,ap)
x /= np.linalg.norm(x)

# set up surfaces
m1 = {'coating':coat,'surf':1,'mode':'reflect'}
m2 = {'coating':coat,'surf':2,'mode':'reflect'}
m3 = {'coating':coat,'surf':4,'mode':'reflect'}

k1 = {'coating':coat,'surf':10,'mode':'reflect'}
k2 = {'coating':coat,'surf':13,'mode':'reflect'}
k3 = {'coating':coat,'surf':16,'mode':'reflect'}

tt = {'coating':coat,'surf':20,'mode':'reflect'}
o1 = {'coating':coat,'surf':25,'mode':'reflect'}
pu = {'coating':coat,'surf':30,'mode':'reflect'}
o2 = {'coating':coat,'surf':33,'mode':'reflect'}
di = {'coating':coat,'surf':36,'mode':'reflect'}

sod = {'coating':coat,'surf':40,'mode':'reflect'}
ifm = {'coating':coat,'surf':43,'mode':'reflect'}
afm = {'coating':coat,'surf':46,'mode':'reflect'}

surflist = [m1,m2,m3,k1,k2,k3,tt,o1,pu,o2,di,sod,ifm,afm]

rf = Rayfront(nrays,wvl,pupil_radius,max_fov)
rf.as_polarized(surflist)
rf.trace_rayset(pth)
rf.compute_jones_pupil(aloc=a,exit_x=x)

# import poke.plotting as plot
# plot.jones_pupil(rf)

write_rayfront_to_serial(rf,f'rayfronts/k2_acam_{nrays}rays_{int(wvl*1e9)}nm')
