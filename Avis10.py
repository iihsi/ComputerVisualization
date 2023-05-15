import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

w = 2
Y, X = np.mgrid[-w:w:100j, -w:w:100j]
U = -Y
V = X

fig = plt.figure(figsize=(5, 5))
gs = gridspec.GridSpec(nrows=3, ncols=2, height_ratios=[1, 1, 0])
seed_points = np.array([[1], [0]])

ax = fig.add_subplot(gs[0, 0])
ax.streamplot(X, Y, U, V, density=[0.5, 1], start_points=seed_points.T)
ax.plot(seed_points[0], seed_points[1], 'bo')
ax.set(xlim=(-w, w), ylim=(-w, w))

plt.tight_layout()
plt.show()