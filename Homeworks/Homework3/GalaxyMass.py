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

# Calculate the halo mass of the 3 galaxies
halo_MW = ComponentMass("MW_000.txt",1)
halo_31 = ComponentMass("M31_000.txt",1)
halo_33 = ComponentMass("M33_000.txt",1)
# Calculate the disk mass of the 3 galaxies
disk_MW = ComponentMass("MW_000.txt",2)
disk_31 = ComponentMass("M31_000.txt",2)
disk_33 = ComponentMass("M33_000.txt",2)
# Calculate the bulge mass of the 3 galaxies
bulge_MW = ComponentMass("MW_000.txt",3)
bulge_31 = ComponentMass("M31_000.txt",3)
bulge_33 = ComponentMass("M33_000.txt",3)
# Calculate the total mass of the 3 galaxies
total_MW = halo_MW+disk_MW+bulge_MW
total_31 = halo_31+disk_31+bulge_31
total_33 = halo_33+disk_33+bulge_33
# Calculate the baryonic mass fraction of the 3 galaxies
f_MW = np.round((disk_MW+bulge_MW)/total_MW,3)
f_31 = np.round((disk_31+bulge_31)/total_31,3)
f_33 = np.round((disk_33+bulge_33)/total_33,3)
# calculate the total halo mass of the Local group
halo_LG = halo_MW+halo_31+halo_33
# Calculate the total disk mass of the Local group
disk_LG = np.round(disk_MW+disk_31+disk_33,3)
# Calculate the total bulge mass of the Local group
bulge_LG = np.round(bulge_MW+bulge_31+bulge_33,3)
# Calculate the total mass of the Local group
total_LG = total_MW+total_31+total_33
# Calculate the baryonic mass fraction of the Local group
f_LG = np.round((disk_LG+bulge_LG)/total_LG,3)
# Create a table containing all the above clculated values
# Rows are the specific galaxies and the Local Group
# Columns are the calculated mass values and the baryonic mass fraction
data = {"Galaxy Name": ["MW","M31","M33","Local Group"],
        "Halo Mass (10^12 solMass)": [halo_MW,halo_31,halo_33,halo_LG],
        "Disk Mass (10^12 solMass)": [disk_MW,disk_31,disk_33,disk_LG],
        "Bulge Mass (10^12 solMass)": [bulge_MW,bulge_31,bulge_33,bulge_LG],
        "Total (10^12 solMass)": [total_MW,total_31,total_33,total_LG],
        "f_bar": [f_MW,f_31,f_33,f_LG]}
# Create a Data Frame of the data
df = pd.DataFrame(data)

# Create a figure of the table so that it can be saved as a pdf
fig, ax = plt.subplots(figsize=(20,10))
ax.axis('off')
final_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')
# Save the pdf to specified location
pdf_tables = PdfPages("C:/Users/msg91/400B HW/3/table.pdf")
pdf_tables.savefig(fig)
pdf_tables.close()