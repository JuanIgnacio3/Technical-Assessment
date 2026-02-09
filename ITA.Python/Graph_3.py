import matplotlib.pyplot as mp
import numpy as np

ratings = ["E", "E10+", "T", "M"]

NA = [55, 52, 48, 60]
EU = [30, 33, 35, 28]
JP = [5, 7, 10, 4]
Other = [10, 8, 7, 8]

x = np.arange(len(ratings))

mp.figure(figsize=(9, 5))

mp.bar(x, NA, label="NA")
mp.bar(x, EU, bottom=NA, label="EU")

bottom2 = np.array(NA) + np.array(EU)
mp.bar(x, JP, bottom=bottom2, label="JP")

bottom3 = bottom2 + np.array(JP)
mp.bar(x, Other, bottom=bottom3, label="Other")

mp.xticks(x, ratings)
mp.ylabel("Percentage of Global Sales (%)")
mp.xlabel("ESRB Rating")
mp.title("Regional Sales Distribution by ESRB Rating")
mp.ylim(0, 100)
mp.legend(title="Region", loc="upper right")

mp.tight_layout()
mp.show()