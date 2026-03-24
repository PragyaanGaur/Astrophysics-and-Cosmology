import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import scipy.constants as sci

# Constants

h = sci.hbar
c = sci.speed_of_light
G = sci.G
k = sci.k
pi = np.pi
M_sun = 1.989e30

# Defining Mass (in terms of Solar mass)

M = np.linspace(3, 1e7, 1000) * M_sun

# Physics Equations

T = (h*c**3)/(8*pi*G*k*M) # Hawking 1975
A = (16*pi*G**2*M**2)/c**4 #Horizon Area
S = (k*c**3*A)/(4*G*h) # Bekenstein 1973

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

#Logarithmic scales to visualise power law scaling

ax1.plot(M, T)
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_xlabel('M (kg)')
ax1.set_ylabel('T (K)')
ax1.set_title('Temperature ~ 1/M')

ax2.plot(M, A)
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.set_xlabel('M (kg)')
ax2.set_ylabel('A (m²)')
ax2.set_title('Area ~ M²')

ax3.plot(M, S)
ax3.set_xscale('log')
ax3.set_yscale('log')
ax3.set_xlabel('M (kg)')
ax3.set_ylabel('S (J/K)')
ax3.set_title('Entropy ~ M²')

plt.subplots_adjust(wspace=0.4, bottom=0.3)

p1 = ax1.scatter([M[0]], [T[0]], color='red')
p2 = ax2.scatter([M[0]], [A[0]], color='red')
p3 = ax3.scatter([M[0]], [S[0]], color='red')

readout = fig.text(0.5, 0.04, '', ha='center', fontsize=9)
ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
slider = Slider(ax_slider, 'Mass (Solar Masses)', 3, 1e7, valinit=3)

def update(val):
    m_val = slider.val * M_sun
    t_val = (h*c**3)/(8*pi*G*k*m_val)
    a_val = (16*pi*G**2*m_val**2)/c**4
    s_val = (k*c**3*a_val)/(4*G*h)

    p1.set_offsets([[m_val, t_val]])
    p2.set_offsets([[m_val, a_val]])
    p3.set_offsets([[m_val, s_val]])

    readout.set_text(f"T = {t_val:.3e} K    A = {a_val:.3e} m²    S = {s_val:.3e} J/K")
    fig.canvas.draw_idle()

slider.on_changed(update)
plt.show()
