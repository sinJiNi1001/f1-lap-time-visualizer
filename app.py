import fastf1
from fastf1 import plotting
import matplotlib.pyplot as plt
from fastf1 import get_event_schedule, get_session
from datetime import datetime, timezone

# Get the current UTC time (timezone-aware)
now = datetime.now(timezone.utc)

# Get the event schedule for the current year
schedule = get_event_schedule(2025)

# Filter only past events (up to last known race)
past_events = schedule[schedule['Session5Date'] < now]

# Get the latest one
latest_event = past_events.iloc[-1]
gp_name = latest_event['EventName']

print(f"Using latest GP: {gp_name}")

# Now load the session (Qualifying shown, change 'Q' to 'R' for Race, etc.)
session = get_session(2025, gp_name, 'Q')
session.load()


# Enable cache
fastf1.Cache.enable_cache('cache')

# Load session
#session = fastf1.get_session(2023, 'British Grand Prix', 'Q')
#session.load()

# Get all driver codes
all_driver_codes = [session.get_driver(d)['Abbreviation'] for d in session.drivers]

# Assign distinct colors automatically
colors = plt.cm.get_cmap('tab20', len(all_driver_codes))

# Plot all drivers
plt.figure(figsize=(16, 8))

for i, code in enumerate(all_driver_codes):
    laps = session.laps.pick_driver(code).pick_quicklaps()
    if not laps.empty:
        plt.plot(laps['LapNumber'], laps['LapTime'].dt.total_seconds(),
                 marker='o', label=code, color=colors(i))

plt.title(f'Lap Times - {latest_event["EventName"]} {latest_event["EventDate"].year} Qualifying (All Drivers)')
plt.xlabel('Lap Number')
plt.ylabel('Lap Time (seconds)')
plt.legend(title='Driver Code', ncol=5, fontsize='small')
plt.grid(True)
plt.tight_layout()
plt.show()
