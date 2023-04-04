import matplotlib.pyplot as plt
from rainflow import rainflow
import numpy as np

# array of turning points
array_ext = np.array([206.7598589,254.391586,166.3117391,209.3335139,237.7549909,179.4376781,209.3013919,224.9412731,184.6593497,207.8124842])


# calculate cycle counts with default values for lfm (0), 
#  l_ult (1e16), and uc_mult (0.5)
array_out = rainflow(array_ext)

# sort array_out by cycle range
array_out = array_out[:,array_out[0,:].argsort()]

# ---------------------------- printing/plotting ------------------------------

# print cycle range, cycle count, cycle mean, goodman-adjusted range (GAR), and
#   goodman-adjusted range with zero fixed-load mean (GAR-ZFLM)
print('\nCalculated cycle count:')
print('\n{:>7s}{:>8s}{:>8s}'.format('Range','Count','Mean'))
print('----------------------------------------------')
for i in range(len(array_out.T)):
    print('{:7.1f}{:8.1f}{:8.1f}'.format(*array_out[[0,3,1,2,4],i]))
    
# plot turning points for vizualization
plt.figure(1,figsize=(6.5,3.5))
plt.clf()

plt.plot(array_ext)
plt.grid('on')
plt.xlabel('Time')
plt.ylabel('Turning Points')
plt.title('Turning Points for Rainflow Demo - J. Rinker')
plt.tight_layout()

plt.show()