import sunpy.map
import sunpy.data.sample
import matplotlib.pyplot as plt
import astropy.units as u
from astropy.coordinates import SkyCoord

aia_map = sunpy.map.Map(sunpy.data.sample.AIA_171_IMAGE)

bottom_left = SkyCoord(-500 * u.arcsec, -500 * u.arcsec, frame=aia_map.coordinate_frame)
top_right = SkyCoord(500 * u.arcsec, 500 * u.arcsec, frame=aia_map.coordinate_frame)

submap = aia_map.submap(bottom_left=bottom_left, top_right=top_right)

fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(1, 2, 1, projection=aia_map)
im1 = aia_map.plot(axes=ax1)
plt.colorbar(im1, ax=ax1)
ax1.set_title("Full Sun")

ax2 = fig.add_subplot(1, 2, 2, projection=submap)
im2 = submap.plot(axes=ax2)
plt.colorbar(im2, ax=ax2)
ax2.set_title("Zoomed Region")

plt.tight_layout()
plt.show()
