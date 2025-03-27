# Import modules
import numpy as np
import astropy.units as u
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from ReadFile import Read
def ComponentMass(filename,parttype):
    # Function that computes the mass of a specified component of a galaxy
    # Inputs: filename, parttype
    # filename - name of galaxy text file to read
    # parttype - the type of particle to calculate the total mass of
    time,particles,data = Read(filename)
    # Create an array of all the mass values of a specific particle type
    datatype = np.where(data['type']==parttype)
    # Divide the mass values by 100 to convert to 10^12 solMass units
    m = data['m'][datatype]/100
    # Sum all of the mass values and round to 3 decimal places
    mass = np.sum(m)
    mass = np.round(mass,3)
    return(mass)