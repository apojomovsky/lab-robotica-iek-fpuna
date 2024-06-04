from roboticstoolbox import jtraj
import matplotlib.pyplot as plt
import numpy as np

# Puntos inicial y final
q_start = [0, 0, 0, 0, 0, 0]
q_end = [np.pi/2, -np.pi/4, np.pi/4, 0, np.pi/2, 0]

# Generar la trayectoria
traj = jtraj(q_start, q_end, 50)

# Visualizar la trayectoria
for i in range(len(q_start)):
    plt.plot(traj.q[:, i], label=f'Joint {i+1}')
plt.legend()
plt.xlabel('Time steps')
plt.ylabel('Joint angles (rad)')
plt.title('Joint Trajectory')
plt.show()
