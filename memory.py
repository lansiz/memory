import numpy as np
import matplotlib.pyplot as plt

initial_strength = 0.55
stimulus = 0.8
plasticity_func = lambda xs: 0.9 * xs + 0.05


class Fire_Together_Record(object):
    def __init__(self):
        self.len = 1000
        self.pos = 0
        self.records = np.array([False] * self.len, dtype=bool)

    def get_fire_together_prob(self):
        return float(self.records.sum()) / self.len

    def record_a_fire_together(self):
        self.records[self.pos] = True
        self.pos = (self.pos + 1) % self.len


recorder = Fire_Together_Record()
x = stimulus
s = initial_strength
sl = []
for i in range(100000):
    if np.random.rand() < x and np.random.rand() < s:
        # fire together now
        recorder.record_a_fire_together()
    # init the recorder before using it
    if i < 1000: continue
    # calculate target strength
    xs = recorder.get_fire_together_prob()
    target_strength = plasticity_func(xs)
    # update strength towards target
    strength_gap = target_strength - s
    s = s + 0.0001 * strength_gap
    # keep s in [0,1]
    s = np.max([0, s])
    s = np.min([1, s])
    # strength trajectory
    sl.append(s)

plt.plot(sl)
plt.show()
