import numpy as np
import astropy.units as u
# This function reads a file and returns three values
# The values are the time(Myr), number of total particles, and the data associated with these particles
def Read(filename):
    # Open and read the file
    file = open(filename,'r')
    # Read the first line and save it as the time
    line1 = file.readline()
    label, value = line1.split()
    time = float(value)*u.Myr
    # Read the second line and save it as the number of particles
    line2 = file.readline()
    label, value = line2.split()
    particles = float(value)
    # Close the file
    file.close()
    # Save the mass, position, and velocity data associated with the particles
    data = np.genfromtxt(filename,dtype=None,names=True,skip_header=3)
    # Return all the values
    return time,particles,data