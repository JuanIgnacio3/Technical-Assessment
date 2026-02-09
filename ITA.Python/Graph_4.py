import matplotlib.pyplot as mp

platforms = ["X360", "PS3", "PS2", "PS4", "PS", "XOne", "Wii", "NES", "DS", "N64", "XB", "PSP", "3DS", "PC", "2600", "GBA", "GC", "SNES", "WiiU", "GB", "GEN"]
Sales = [322.37, 285.08, 203.49, 118.96, 92.7, 50.11, 49.78, 49.3, 39.71, 28.25, 26.24, 22.87, 19.72, 19.43, 15.9, 11.33, 11.02, 7.6, 6.34, 5.75, 2.6]

mp.figure(figsize=(8,4))

mp.barh(platforms, Sales)

mp.xlabel("Global Sales (millions)")
mp.ylabel("Marker Share (%)")
mp.title("Top Platforms by M-Rated Game Sales")
mp.gca().invert_yaxis()

mp.tight_layout()
mp.show()
