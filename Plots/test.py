import numpy as np
import matplotlib.pyplot as plt
#hyperparameters
runs = 5
batch_size = 512
epoch = 200
t_update = 10
g = 0.8
max_steps = 300
dt = 0.0375

target = [0.5,0]
deviation = 0.075
target_area = [[target[0]-deviation,target[0]+deviation],
               [target[1]-deviation,target[1]+deviation]]
U0 = 0.4
lstm_hidden_size = 0#8
plt.rcParams.update({'font.size': 13})

# k_b = 1.380649e-23 #J/K
# Temp = 273 #K
# xi_R = 1e-3 #m/s
rotational_diffusion = 0.075 #k_b*Temp/xi_R
char_length = 1
vorticity = 0

# file_path1 = './Plots/Runs_avg_loss.txt'


data = np.loadtxt('Runs_avg_loss.txt',delimiter='\n')
print(len(data))


# Runs_avg_loss = []
# with open(file_path1,'r') as file:
#     Runs_avg_loss.append(file.read())

# file_path2 = './Plots/Runs_avg_succ.txt'
# Runs_avg_succ = []
# with open(file_path2,'r') as file:
#     Runs_avg_succ.append(file.read())
# print(len(Runs_avg_loss))
# fig, ax1 = plt.subplots()
# ax2 = ax1.twinx()
# X = np.linspace(0,epoch,epoch)

# ax1.plot(X,Runs_avg_loss, label = 'Mean Episode Loss')
# ax2.scatter(X, Runs_avg_succ, label = 'Mean Success',c='orange',marker='.')

# ax1.set_xlabel('Episode',fontsize=15)
# ax1.set_ylabel('Episode Mean Loss',fontsize=15)
# ax2.set_ylabel('% Average Success Rate',fontsize=15)
# ax2.set_yticks([0,25,50,75,100])
# ax1.set_title(r'$D_R$ = '+ str(rotational_diffusion),fontsize=15)
# # ax1.legend(bbox_to_anchor=(1,-0.1))
# # ax2.legend(bbox_to_anchor=(1,-0.5))
# plt.show()
# # name = 'DR = ' + str(rotational_diffusion) + ', batch_size = ' + str(batch_size) + ', U0 = ' + str(U0)
# # plt.savefig(fname = name, dpi=300)