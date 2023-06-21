import math
import matplotlib.pyplot as plt

# sampling density
x = []
for i in range(0, 61, 1):
    x.append(i / 1000)

# pressure function
y = []
for i in x:
    y.append(6.3 * math.exp(-120 * i) + 0.7)

# check function adequate
#fig, ax = plt.subplots()
#ax.plot(x, y)

# write data to HDD
I = range(len(x))
with open('mouthPressure.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')
    for i in I:
        writer.writerow([x[i]] + [y[i]])