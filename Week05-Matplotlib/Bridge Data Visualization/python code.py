import matplotlib.pyplot as plt
import pandas as pd
df=pd.DataFrame({'Bridge':['Bridge 1', 'Bridge 2', 'Bridge 3', 'Bridge 4', 'Bridge 5'],
'Length':[100, 150, 130, 200, 170],
'Max_Vibration':[2.1, 3.5, 2.8, 5.2, 4.1]})

# -------------------------
# Chart 1: Maximum Vibration
# -------------------------
plt.figure(figsize=(10,6))
plt.bar(df['Bridge'],df['Max_Vibration'])
plt.title('Maximum Vibration of Bridges')
plt.xlabel('Bridge Name')
plt.ylabel('Maximum Vibration')
plt.grid()
for i,value in enumerate(df['Max_Vibration']):
    plt.text(i,value,str(value))
plt.tight_layout()
plt.savefig('Week05-Matplotlib/Bridge Data Visualization/bridge_vibration.png')
plt.show()

# -------------------------
# Chart 2: Bridge Length
# -------------------------
plt.figure(figsize=(10,6))
plt.plot(df['Bridge'], df['Length'], label='Bridge Length')
plt.title('Bridge Length')
plt.xlabel('Bridge Name')
plt.ylabel('Bridge length (m)')
plt.grid()
for i,value in enumerate(df['Length']):
    plt.text(i,value,str(value))
plt.legend()
plt.tight_layout()
plt.savefig('Week05-Matplotlib/Bridge Data Visualization/bridge_Length.png')
plt.show()

# -------------------------
# Chart 3: Bridge Length vs Maximum Vibration
# -------------------------
plt.figure(figsize=(10,6))
plt.scatter(df['Length'], df['Max_Vibration'])
plt.title('Bridge Length vs Maximum Vibration')
plt.xlabel('Bridge Length (m)')
plt.ylabel('Maximum Vibration')
plt.grid()
plt.tight_layout()
plt.savefig('Week05-Matplotlib/Bridge Data Visualization/Bridge Length vs Maximum Vibration.png')
plt.show()