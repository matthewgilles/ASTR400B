import numpy as np
import astropy.units as u
from ReadFile import Read
# This function reads a file of particle data and calculates certain values for a specified particle
# Reads a file, collects all data for a specific particle type, and calculates for a single particle
# Calculates and returns the magnitude of the distance, velocity, and mass of the specified particle
def ParticleInfo(filename,parttype,partnum):
    # Use the Read function to get the raw data
    time,particles,data = Read(filename)
    # Group the data by particle type
    datatype = np.where(data['type']==parttype)
    # Separate the three dimensional position and velocity data
    x = data['x'][datatype]*u.kpc
    y = data['y'][datatype]*u.kpc
    z = data['z'][datatype]*u.kpc
    vx = data['vx'][datatype]*(u.km/u.s)
    vy = data['vy'][datatype]*(u.km/u.s)
    vz = data['vz'][datatype]*(u.km/u.s)
    # Get the mass data
    m = data['m'][datatype]*u.solMass*10**10
    # Use the positional data to calculate the magnitude of the distance of the particle
    distance = np.sqrt((x[partnum-1])**2+(y[partnum-1])**2+(z[partnum-1])**2)
    # Round to three decimal places
    distancef = np.around(distance,3)
    # Use the velocity data to calculate the magnitude of the velocity of the particle
    velocity = np.sqrt((vx[partnum-1])**2+(vy[partnum-1])**2+(vz[partnum-1])**2)
    # Round to three decimal places
    velocityf = np.around(velocity,3)
    # Get mass of specific particle
    mass = m[partnum-1]
    # Convert the distance to lightyears
    distancely = distancef.to(u.lyr)
    # Return all the values
    return distancef,velocityf,mass,distancely