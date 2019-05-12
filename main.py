import random_color as rc
import matplotlib.pyplot as plt

print("Generating random color...")

randomHex = rc.random_color()

hex = randomHex.strip('#')

rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

x = [randomHex, 'Red', 'Green', 'Blue']
y = [255, rgb[0], rgb[1], rgb[2]]

x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, y, color=[randomHex, 'red', 'green', 'blue'])

plt.title('Hex to RGB Values')
plt.ylim(0, 255)

plt.xticks(x_pos, x)

plt.show()