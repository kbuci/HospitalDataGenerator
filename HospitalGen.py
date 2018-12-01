import numpy as np
np.random.seed(0)
wstream = open("hospitals.txt",'w')
for i in range(1,6):
    ambulances = 2**i
    spots1 = 2 * ambulances
    spots2 = 3 * ambulances
    for j in range(100):
        x1,y1 = np.random.choice(range(-50,501), spots1, replace=False), np.random.choice(range(-50,501), spots1, replace=False)
        a1 = np.random.choice(range(spots1), ambulances, replace=False)
        wstream.write('\t'.join([str(a) for a in a1]) + '\n')
        wstream.write('\t'.join([str(x) + ',' + str(y) for x,y in zip(x1,y1)]) + '\n')
    for j in range(100):
        x2,y2 = np.random.choice(range(-50,501), spots2, replace=False), np.random.choice(range(-50,501), spots2, replace=False)
        a2 = np.random.choice(range(spots2), ambulances, replace=False)
        wstream.write('\t'.join([str(a) for a in a2]) + '\n')
        wstream.write('\t'.join([str(x) + ',' + str(y) for x,y in zip(x2,y2)]) + '\n')
wstream.close()

