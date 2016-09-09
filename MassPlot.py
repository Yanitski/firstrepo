# Import some libraries
from astropy.table import Table
import matplotlib.pyplot as plt
# Next load the file.
mytable = Table.read('m83.co10.K_props_clfind.fits')
figure = plt.figure(figsize=(4.5,4))
#figure size in inches
plt.loglog(mytable['MASS_EXTRAP'],mytable['VIRMASS_EXTRAP_DECONV'],marker='s',linestyle='None')
# Note that matplotlib understands LaTeX math in the code below
plt.xlabel(r'$M_{\mathrm{lum}}\ (M_{\odot})$') 
plt.ylabel(r'$M_{\mathrm{vir}}\ (M_{\odot})$')
plt.title('Virial Mass v Luminous Mass')
plt.tight_layout() 	
plt.savefig('MlumMvir_matplotlib.png')
