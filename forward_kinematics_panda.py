import roboticstoolbox as rb
import numpy as np


panda = rtb.models.ETS.Panda()
print("default angular position qr")
print(panda.qr)
print("Homogeneous Transformation Matrix")
print(panda.fkine(panda.qr))

#D-H parameters
panda_dh = rtb.models.DH.Panda()
print(panda_dh)

# plot Robot
panda.plot(panda.qr, block=True)

#plot new position
new_pos = np.array([0, 0, 0, 0, 0, 0, 0, 0])
panda.plot(new_pos, block=True)
print(panda.fkine(new_pos))
