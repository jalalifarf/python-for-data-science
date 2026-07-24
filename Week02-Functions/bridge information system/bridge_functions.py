import csv
from file_manager import is_file_empty
header=['Bridge Name','Bridge Length','Bridge Width','Construction Year','Material','Number of Sensors']
def add_bridge():
    with open('bridges.csv',"a+", newline="", encoding="utf-8") as file:
        file.seek(0)
        writer=csv.writer(file)
        
        
        if is_file_empty('bridges.csv'):
            writer.writerow(header)

        bridge_data=[]
        for i in header:
            bridge_data.append(input(f'please enter {i}: '))
           
        writer.writerow(bridge_data) 
add_bridge()