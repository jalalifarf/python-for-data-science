# **Bridge Data Analysis & Visualization V2**
import pandas as pd
import matplotlib.pyplot as plt

bridge_names = ['Bridge 1', 'Bridge 2', 'Bridge 3', 'Bridge 4', 'Bridge 5']

bridge_lengths = [110, 140, 150, 200, 170]

construction_years = [1998, 2006, 2005, 2015, 2020]

materials = ['Concrete', 'Steel', 'Concrete', 'Steel', 'Concrete']

maximum_vibrations = [2.1, 3.5, 2.8, 5.2, 4.1]


df = pd.DataFrame({
    'name': bridge_names,
    'length': bridge_lengths,
    'year': construction_years,
    'material': materials,
    'max_vib': maximum_vibrations})


fig, ax = plt.subplots(3,1,figsize=(8,8))

# -------------------------
# Chart 1: Bridge Length Comparison
# -------------------------
ax[0].bar(df['name'], df['length'], label='Bridge Length')

ax[0].set_title('Bridge Length Comparison')
ax[0].set_xlabel('Bridge Name')
ax[0].set_ylabel('Length (m)')

ax[0].legend()
ax[0].grid()

for i, value in enumerate(df['length']):
    ax[0].annotate(f'{value}', xy=(df['name'][i], value + 5))

# -------------------------
# Chart 2: Maximum Vibration Comparison
# -------------------------
ax[1].bar(df['name'],df['max_vib'], label='Maximum Vibration')

ax[1].set_title('Maximum Vibration Comparison')
ax[1].set_xlabel('Bridge Name')
ax[1].set_ylabel('Maximum Vibration')

ax[1].legend()
ax[1].grid()

for i, value in enumerate(df['max_vib']):
    ax[1].annotate(f'{value}',xy=(df['name'][i],value+0.2))

# -------------------------
# Chart 3: Bridge Length vs Maximum Vibration
# -------------------------
ax[2].scatter(df['length'],df['max_vib'], label='Maximum Vibration')

ax[2].set_title('Bridge Length vs Maximum Vibration')
ax[2].set_xlabel('Bridge Length (m)')
ax[2].set_ylabel('Maximum Vibration')

ax[2].legend()
ax[2].grid()

for i, value in enumerate(df['max_vib']):
    ax[2].annotate(f'{value}',xy=(df['length'][i]+1,value))

print('Longest Bridge:', df['name'][df['length'].idxmax()] )
print('length:', df['length'].max(),'m')
print('Bridge with Highest Vibration:',df['name'][df['max_vib'].idxmax()])      
print('Maximum Vibration:', df['max_vib'].max())
  
plt.tight_layout()
plt.show()


