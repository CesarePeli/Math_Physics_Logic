from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.constants import h,c,k
T=5000.
lam=np.geomspace(1e-7,1e-4,1200)
planck=8*np.pi*h*c/lam**5/np.expm1(h*c/(lam*k*T))
rj=8*np.pi*k*T/lam**4
assert np.all(rj>=planck)
plt.rcParams.update({'font.size':12})
fig,ax=plt.subplots(figsize=(9,5.4),layout='constrained')
ax.loglog(lam*1e6,planck,color='#1a5490',lw=2.2,label='Planck')
ax.loglog(lam*1e6,rj,'--',color='#a43c26',lw=2,label='Rayleigh–Jeans')
ax.axvspan(.38,.75,color='#ddb848',alpha=.17,label='Approximate visible band')
ax.set(xlabel='Wavelength λ (μm)',ylabel='Spectral energy density uλ (J m⁻⁴)',title='Thermal radiation at T = 5000 K',xlim=(.1,100),ylim=(1e-7,1e7))
ax.grid(True,which='major',alpha=.3);ax.legend(loc='upper right')
out=Path(__file__).resolve().parents[2]/'images/plank.png';out.parent.mkdir(exist_ok=True)
fig.savefig(out,dpi=180)
print('Saved unscaled spectra in physical units; verified Rayleigh–Jeans ≥ Planck at every plotted wavelength')
