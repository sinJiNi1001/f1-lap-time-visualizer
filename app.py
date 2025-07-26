import fastf1
from fastf1 import plotting
import matplotlib.pyplot as plt

# Enable cache (creates a 'cache' folder for storing data)
fastf1.Cache.enable_cache('cache')

# Load the qualifying session for 2023 British GP
session = fastf1.get_session(2023, 'British Grand Prix', 'Q')
session.load()

# List of drivers to compare
driver_codes = ['VER', 'HAM', 'LEC', 'NOR', 'RUS']

# Assign colors to each driver
colors = {
    'VER': 'blue',
    'HAM': 'black',
    'LEC': 'red',
    'NOR': 'orange',
    'RUS': 'green'
}

# Create the plot
plt.figure(figsize=(10, 6))

# Loop over each driver and plot their quick laps
for code in driver_codes:
    laps = session.laps.pick_driver(code).pick_quicklaps()
    plt.plot(
        laps['LapNumber'],
        laps['LapTime'].dt.total_seconds(),
        marker='o',
        label=code,
        color=colors[code]
    )

# Plot settings
plt.title('Lap Times - 2023 British GP Qualifying')
plt.xlabel('Lap Number')
plt.ylabel('Lap Time (seconds)')
plt.legend(title='Driver Code')
plt.grid(True)
plt.tight_layout()

# Show plot
plt.show()
