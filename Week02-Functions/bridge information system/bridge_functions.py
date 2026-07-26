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

def show_bridges():
    with open('bridges.csv',"a+", newline="", encoding="utf-8") as file:
        file.seek(0)
        if is_file_empty('bridges.csv'):
            print('there is no bridge to show') 
        else:
            reader=csv.reader(file)
            return(list(reader))

def search_bridge():
    if is_file_empty('bridges.csv'):
        print('the bridge was not found')
    else:
        bridges=show_bridges()
        bridge_name=input('please enter the bridge name: ')
        bridge_properties=[]
        for rows in bridges:
            if rows[0].strip().lower() == bridge_name.strip().lower():
                bridge_properties=rows
                break
        if bridge_properties==[]:
            print('the bridge was not found')
        else:
            for i in range(len(header)):
                print(f'{header[i]} : {bridge_properties[i]}\n')
