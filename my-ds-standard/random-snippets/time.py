# How calculate time 

import time

def time_spent(time0):
    t = time.time() - time0
    t_int, t_min = int(t) // 60, t % 60
    return '{} min {:6.3f} s'.format(t_int, t_min) if t_int != 0 else '{:.3f} s'.format(t_min)

"""
HOW TO USE
t0 = time.time()
print(time_spent(t0))
"""
