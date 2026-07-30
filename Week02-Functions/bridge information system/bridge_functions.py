import csv
from file_manager import is_file_empty
HEADER=['Bridge Name','Bridge Length','Bridge Width','Construction Year','Material','Number of Sensors']
def normalize_name(name):
    return (name.strip().lower())
    
def add_bridge():
    with open('bridges.csv',"a+", newline="", encoding="utf-8") as file:
        file.seek(0)
        writer=csv.writer(file)
        
        
        if is_file_empty('bridges.csv'):
            writer.writerow(HEADER)

        bridge_data=[]
        for i in HEADER:
            bridge_data.append(input(f'please enter {i}: '))
           
        writer.writerow(bridge_data) 
        print('the bridge information has added successfuly!')

def show_bridges():
    with open('bridges.csv',"a+", newline="", encoding="utf-8") as file:
        file.seek(0)
        if is_file_empty('bridges.csv'):
            return ['there is no bridge to show'] 
        else:
            reader=csv.reader(file)
            return(list(reader))

def search_bridge():
    if is_file_empty('bridges.csv'):
        print('the bridge was not found')
        return
    bridges=show_bridges()
    bridge_name=input('please enter the bridge name: ')
    bridge_properties=None
    for rows in bridges:
        if normalize_name(rows[0]) == normalize_name(bridge_name):
            bridge_properties=rows
            break
    if bridge_properties is None:
        print('the bridge was not found')
    else:
        for i in range(len(HEADER)):
            print(f'{HEADER[i]} : {bridge_properties[i]}\n')

def update_bridge():
    if is_file_empty('bridges.csv'):
            print('there is no bridge to update')
            return
    bridge_name=input('please enter the name of bridge you want to update: ')
    print('which property you want to update?')
    for i,item in enumerate(HEADER):
        print(f'{i}-{item}')
    property_num=input('please only enter the number: ')
    try:
        property_num=int(property_num)
        if property_num < 0 or property_num >= len(HEADER):
            print('the input number is not valid')
            return
    except ValueError:
        print('the input number is not valid')
        return
    updated_property=input('please enter the updated property: ')    
    bridges=show_bridges()
    found=False
    for i, rows in enumerate(bridges):
        if normalize_name(rows[0]) == normalize_name(bridge_name):
            bridges[i][property_num]=updated_property 
            found=True
            break
    if not found:
        print('the bridge wasnot found')
        return
    with open('bridges.csv',"w", newline="", encoding="utf-8") as file:
        writer=csv.writer(file)
        writer.writerows(bridges)
    print('the file has updated successfuly!')

def delete_bridge():
    if is_file_empty('bridges.csv'):
        print('there is no bridge to delete')
        return
    bridges=show_bridges()
    bridge_name=input('please enter the bridge name you want to delete: ')
    found=False
    for i,rows in enumerate(bridges):
        if normalize_name(rows[0]) == normalize_name(bridge_name):
            del bridges[i]
            found=True
            break
    if not found:
        print('the bridge was not found')
        return
    with open("bridges.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(bridges)
    print('the bridge has deleted successfully!')
