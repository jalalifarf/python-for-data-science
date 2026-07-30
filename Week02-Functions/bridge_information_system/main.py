from bridge_functions import (
    add_bridge,
    show_bridges,
    search_bridge,
    update_bridge,
    delete_bridge,
)
menu_options=['Add a new bridge','Show all bridges','Search a bridge','update a bridge','Delete a bridge','Exit']

while True:
    print('====== Bridge Information System ======')
    for i, item in enumerate(menu_options):
        print(f'{i+1}. {item}')
    action=input('please enter the number of your desired action: ')
    try:
        action=int(action)
        if action<=0 or action>len(menu_options):
           print('the input is not valid') 
           continue
    except ValueError:
        print('the input is not valid')
        continue
    if action==1:
        add_bridge()
    elif action==2:
        bridges=show_bridges()
        for rows in bridges:
            print(rows)
    elif action==3:
        search_bridge()
    elif action==4:
        update_bridge()
    elif action==5:
        delete_bridge()
    else:
        break


