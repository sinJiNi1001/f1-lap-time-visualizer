import fastf1
from fastf1.plotting import setup_mpl
import matplotlib.pyplot as plt

# Enable cache
fastf1.Cache.enable_cache('cache')

# Setup matplotlib
setup_mpl()

# Load session (Example: 2023 British GP - Qualifying)
session = fastf1.get_session(2023, 'Silverstone', 'Q')
session.load()

# Choose a driver
driver = 'HAM'  # You can change to VER, NOR, etc.

laps = session.laps.pick_drivers(driver).pick_quicklaps()
lap_times = laps['LapTime'].dt.total_seconds()

# Plot lap times
plt.plot(lap_times, marker='o')
plt.title(f'{driver} Lap Times - 2023 British GP Qualifying')
plt.xlabel('Lap Number')
plt.ylabel('Lap Time (s)')
plt.grid(True)
plt.show()
