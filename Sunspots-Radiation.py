import numpy as np
import matplotlib.pyplot as plt

# Constants

h = 6.626e-34
c = 2.998e8
k = 1.381e-23
b = 2.898e-3
sigma = 5.67e-8
emissivity = 0.99

# Temperatures (Kelvin)

T_quiet = 5778
T_penumbra = 4500
T_umbra = 3800
T_range = np.linspace(3000,7000,10000)

# Wavelength array: 100 nm to 2500 nm, in meters

wavelength = np.linspace(1e-7, 2.5e-6, 10000)

# Planck's radiation law

def planck(wl, T):
    return (2 * h * c**2 / wl**5) / (np.exp((h * c) / (wl * k * T)) - 1)

#Stefan-Boltzmann Law

def stefan(T):
    return emissivity * sigma * T ** 4      #Considering flux to avoid taking surface area

# Evaluate

B_quiet = planck(wavelength, T_quiet)
B_penumbra = planck(wavelength, T_penumbra)
B_umbra = planck(wavelength, T_umbra)

F_quiet = stefan(T_quiet)
F_penumbra = stefan(T_penumbra)
F_umbra = stefan(T_umbra)
F_range = stefan(T_range)

# Plot

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
ax1.plot(wavelength * 1e9, B_quiet, label='Quiet Sun (5778 K)')
ax1.plot(wavelength * 1e9, B_penumbra, label='Penumbra (4500 K)')
ax1.plot(wavelength * 1e9, B_umbra, label='Umbra (3800 K)')
ax1.set_xlabel('Wavelength (nm)')
ax1.set_ylabel('Spectral Radiance (W m⁻³ sr⁻¹)')
ax1.set_title('Planck Blackbody Curves')
for T, color in zip([T_quiet, T_penumbra, T_umbra], ['C0', 'C1', 'C2']):
    ax1.axvline(b / T * 1e9, linestyle='--', color=color, alpha=0.5)
ax1.legend()

ax2.plot(T_range, F_range, label='Stefan-Boltzmann curve')
ax2.scatter([T_umbra, T_penumbra, T_quiet], [F_umbra, F_penumbra, F_quiet])
ax2.annotate('Umbra (3800 K)', (T_umbra, F_umbra))
ax2.annotate('Penumbra (4500 K)', (T_penumbra, F_penumbra))
ax2.annotate('Quiet Sun (5778 K)', (T_quiet, F_quiet))
ax2.set_xlabel('Temperature (K)')
ax2.set_ylabel('Flux Radiated (W/m²)')
ax2.set_title('Stefan-Boltzmann Law Curves')
ax2.legend()

plt.tight_layout()
plt.show()

print(f"Umbra-Quiet Sun flux ratio:    {F_umbra / F_quiet:.4f}")
print(f"Penumbra-Quiet Sun flux ratio: {F_penumbra / F_quiet:.4f}")
