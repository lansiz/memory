import numpy as np
import matplotlib.pyplot as plt

initial_strength = 0.55
stimulus = 0.8
# plasticity function: one fixed point, monotonically increasing
f = lambda xs: 0.9 * xs + 0.05
# plasticity function: one f.p., monotonically decreasing
# f = lambda xs: -1 * xs + 1
# plasticity function: three f.p., non-monotonic
# f = lambda xs: 0.5 * np.sin(4 * np.pi * xs) + 0.5
record_len = 1000
iterations = 200000


class Fire_Together_Record(object):
    """
    calculate the fire-together probability from
    the firing history.
    """

    def __init__(self):
        self.pos = 0
        self.records = np.array([False] * record_len, dtype=bool)

    def get_fire_together_prob(self):
        return float(self.records.sum()) / record_len

    def record_a_fire_together(self, together):
        self.records[self.pos] = together
        self.pos = (self.pos + 1) % record_len


recorder = Fire_Together_Record()
x = stimulus
s = initial_strength
sl = []
for i in range(iterations):
    # strength trajectory
    sl.append(s)

    # option 1: calculate fire-together probability from firing history
    """
    # store the firing history
    if np.random.rand() < x and np.random.rand() < s:
        # fire together, record it
        recorder.record_a_fire_together(True)
    else:
        # fail to fire together, record it
        recorder.record_a_fire_together(False)
    # init fire-together probability before using it
    if i < record_len:
        continue
    xs = recorder.get_fire_together_prob()
    """

    # option 2: calculate fire-together probability by simply doing x * s
    xs = x * s

    # calculate target strength
    target_strength = f(xs)
    # update strength towards target
    strength_gap = target_strength - s
    s = s + 0.0001 * strength_gap
    # keep s in [0,1]
    s = np.max([0, s])
    s = np.min([1, s])

plt.plot(sl)
plt.xlabel("iterations")
plt.ylabel("s (strength)")
print("stimulus[%f] -------- g --------> strength@fp[%f]:" % (stimulus, sl[-1]))
plt.savefig("trajectory.png")
plt.show()
