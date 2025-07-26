import fastf1
from fastf1 import plotting, get_event_schedule, get_session
import matplotlib.pyplot as plt
from datetime import datetime, timezone

# Enable cache
fastf1.Cache.enable_cache('cache')

# Get the current UTC time
now = datetime.now(timezone.utc)

# Load latest event
schedule = get_event_schedule(2025)
past_events = schedule[schedule['Session5Date'] < now]
latest_event = past_events.iloc[-1]
gp_name = latest_event['EventName']
year = latest_event['EventDate'].year
# Extract year from index

print(f"Using latest GP: {gp_name} ({year})")

# Load qualifying session for latest GP
session = get_session(year, gp_name, 'Q')
session.load()

# Get all driver codes
all_driver_codes = [session.get_driver(d)['Abbreviation'] for d in session.drivers]

# Sort drivers by best lap time
driver_best_laps = {
    code: session.laps.pick_driver(code).pick_quicklaps()['LapTime'].min().total_seconds()
    for code in all_driver_codes
}
sorted_driver_codes = sorted(driver_best_laps, key=driver_best_laps.get)

# Set dark background
plt.style.use('dark_background')
colors = plt.cm.get_cmap('nipy_spectral', len(sorted_driver_codes))

# Create the plot
plt.figure(figsize=(16, 8))

for i, code in enumerate(sorted_driver_codes):
    laps = session.laps.pick_driver(code).pick_quicklaps()
    if not laps.empty:
        plt.plot(laps['LapNumber'], laps['LapTime'].dt.total_seconds(),
                 marker='o', label=code, color=colors(i))

        # Annotate best lap
        best_lap = laps.loc[laps['LapTime'].idxmin()]
        plt.annotate(f"{best_lap['LapTime'].total_seconds():.2f}s",
                     xy=(best_lap['LapNumber'], best_lap['LapTime'].total_seconds()),
                     textcoords='offset points',
                     xytext=(0, 5),
                     ha='center',
                     fontsize=8,
                     color=colors(i))

# Final plot formatting
plt.title(f'Lap Times - {gp_name} {year} Qualifying (All Drivers)', fontsize=16)
plt.xlabel('Lap Number', fontsize=12)
plt.ylabel('Lap Time (seconds)', fontsize=12)
plt.legend(title='Driver Code', ncol=5, fontsize='small')
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
plt.tight_layout()
plt.savefig('lap_times_visual.png', dpi=300)
plt.show()
