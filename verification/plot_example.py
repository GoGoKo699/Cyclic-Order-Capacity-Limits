#!/usr/bin/env python3
"""Plot the exact finite-N qubit example; no simulation or fitted data."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parents[1]
n = np.unique(np.round(np.geomspace(1, 100000, 500)).astype(int))
v, d = 4/5, 2
denominator = d*d+v*(n-1)
success = denominator/(n*d*d)
fidelity = (1+v*(n-1))/denominator

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.hashsalt':'cyclic-capacity-v1'})
fig, ax = plt.subplots(figsize=(8.4,4.5), layout='constrained')
fig.patch.set_facecolor('white')
ax.plot(n,fidelity,color='#087e8b',linewidth=2.6,label='Accepted entanglement fidelity')
ax.plot(n,success,color='#4165a8',linewidth=2.6,label='Acceptance probability')
ax.axhline(0.2,color='#4165a8',linewidth=1,linestyle=':',alpha=0.7)
ax.scatter([1000],[4001/4016],color='#087e8b',s=30,zorder=4)
ax.scatter([1000],[251/1250],color='#4165a8',s=30,zorder=4)
ax.annotate('N = 1,000: fidelity 0.9963',xy=(1000,4001/4016),xytext=(80,0.78),
            color='#075e68',arrowprops={'arrowstyle':'-','color':'#087e8b'})
ax.set_xscale('log')
ax.set_xlim(1,100000)
ax.set_ylim(0,1.06)
ax.set_xlabel('Underlying channel uses per device, N (log scale)')
ax.set_ylabel('Probability or fidelity')
ax.set_title('Accurate accepted outputs with zero unassisted capacity',loc='left',fontsize=14,pad=20)
ax.text(0,1.025,'Qubit target; unobserved order dephasing with v = 4/5',transform=ax.transAxes,fontsize=10,color='#555555')
ax.text(0.5,0.47,'Quantum and private capacities are zero\nfor every finite N in this family',
        transform=ax.transAxes,ha='center',va='center',fontsize=11,
        bbox={'facecolor':'#f0f5f6','edgecolor':'none','boxstyle':'round,pad=0.6'})
ax.legend(loc='lower right',frameon=False,fontsize=10)
ax.grid(axis='y',color='#e6e9ec',linewidth=0.7)
ax.spines[['top','right']].set_visible(False)
out=root/'figures';out.mkdir(exist_ok=True)
fig.savefig(out/'qubit_dephasing.svg',metadata={'Date':None,'Creator':'verification/plot_example.py'})
print(out/'qubit_dephasing.svg')
