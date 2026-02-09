import matplotlib.pyplot as mp

regions = ["NA", "EU", "JP", "Other"]
percentages = [50.15, 35.07, 4.56, 10.22]

mp.figure(figsize=(8,2))

left = 0
for region, value in zip(regions, percentages):
    mp.barh("Wii Sports", value, left=left, label=region)
    left += value

mp.xlabel("Percentage of Global Sales (%)")
mp.title("Regional Distribution fo Global Sales - Wii Sports (2006)")
mp.legend(bbox_to_anchor=(1.05,1), loc="upper left")
mp.xlim(0, 100)

mp.tight_layout()
mp.show()
