import numpy as np
sensor_data=np.array([12.3,11.8,13.1,12.7,11.9,12.5,13.0,12.4,11.7,12.8])
mean_value=np.mean(sensor_data)
max_value=np.max(sensor_data)
min_value=np.min(sensor_data)
std_value=np.std(sensor_data)
print("Bridge Sensor Data Analysis")
print("-" * 35)
print(f"Average: {mean_value:.2f}")
print(f"Maximum: {max_value:.2f}")
print(f"Minimum: {min_value:.2f}")
print(f"Standard deviation: {std_value:.2f}")
indices=np.where(sensor_data>mean_value)[0]
print(indices,type(indices))
print('Sensores about average:') 
for i in indices:
    print(f"Sensor {i+1}: {sensor_data[i]:.2f}")
answer = input("Do you want to see all sensor values? (y/n): ").strip().lower()
if answer == "y":
    print(sensor_data)

    