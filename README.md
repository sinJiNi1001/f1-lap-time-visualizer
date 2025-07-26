# 🏎️ F1 Lap Time Visualizer

A dynamic visualization tool to plot and compare qualifying lap times of all drivers from the latest completed Formula 1 Grand Prix. Powered by the [FastF1](https://theoehrly.github.io/Fast-F1/) api.

<br/>

## 📊 Features

- Automatically fetches the **latest completed qualifying session** (2025 season).
- Plots **lap times vs lap numbers** for **all drivers**.
- Uses color-coded lines for easy comparison.
- Filters out slow laps (in-laps, out-laps) to show only quick laps.

<br/>

## 🛠️ Technologies Used

- [FastF1](https://theoehrly.github.io/Fast-F1/)
- Python 3.x
- Matplotlib
- Pandas
- UTC-based event scheduling

<br/>

## 🚀 Lookup Table

| Abbreviation | Full Name        | Team (2024)              |
| ------------ | ---------------- | ------------------------ |
| VER          | Max Verstappen   | Red Bull Racing          |
| PER          | Sergio Pérez     | Red Bull Racing          |
| HAM          | Lewis Hamilton   | Mercedes                 |
| RUS          | George Russell   | Mercedes                 |
| LEC          | Charles Leclerc  | Ferrari                  |
| SAI          | Carlos Sainz     | Ferrari                  |
| NOR          | Lando Norris     | McLaren                  |
| PIA          | Oscar Piastri    | McLaren                  |
| ALO          | Fernando Alonso  | Aston Martin             |
| STR          | Lance Stroll     | Aston Martin             |
| GAS          | Pierre Gasly     | Alpine                   |
| OCO          | Esteban Ocon     | Alpine                   |
| ALB          | Alexander Albon  | Williams                 |
| SAR          | Logan Sargeant   | Williams                 |
| BOT          | Valtteri Bottas  | Sauber (Alfa Romeo)      |
| ZHO          | Zhou Guanyu      | Sauber (Alfa Romeo)      |
| TSU          | Yuki Tsunoda     | RB (formerly AlphaTauri) |
| RIC          | Daniel Ricciardo | RB (formerly AlphaTauri) |
| HUL          | Nico Hülkenberg  | Haas                     |
| MAG          | Kevin Magnussen  | Haas                     |

<br/>

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/sinJiNi1001/f1-lap-time-visualizer.git
cd f1-lap-time-visualizer
