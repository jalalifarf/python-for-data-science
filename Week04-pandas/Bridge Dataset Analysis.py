import pandas as pd
df=pd.read_csv('Week02-Functions/bridge_information_system/bridges.csv')

size=df.shape
print(f'Number of bridges :',size[0],'\n', 'columns:',list(df.columns))
df.info()
df1=df.describe()
print('the statistics of bridge length is: \n', df1.loc[['mean','min','max'],['Bridge Length']])

df_concrete = df[df['Material'] == 'Concrete']
if df_concrete.empty:
    print('There is no Concrete bridge')
else:
    print('Concrete Bridges:\n',df_concrete)

df_steel = df[df['Material'] == 'Steel']
if df_steel.empty:
    print('there is no steel bridge ')
else:
    print('Steel Bridges:\n',df_steel)


df_2000=df[df['Construction Year']>2000]
if df_2000.empty:
    print('there is no bridges that have constructed after 2000 ')
else:
    print('Bridges that have constructed after 2000:\n' ,df_2000)
    
Name=input('please enter the bridge name: ').strip().lower()
result=df[df['Bridge Name'].str.strip().str.lower()==Name]
if result.empty:
    print('the bridge was not found')
else:
    print(result)


menu_options=list(df.columns)+['Do not sort']
print('do you want to sort bridges based on:')
for i, item in enumerate(menu_options):
        print(f'{i+1}. {item}')
action=input('please enter the number of your desired action: ')
try:
    action=int(action)
    if action<=0 or action>len(menu_options):
        print('the input is not valid') 
    if 1<=action<=6:
        how_to_sort=input('do you want to sort:\n'
          '1.ascending\n'  
          '2.decending\n'
          '(please only enter the number):')
        try:
            how_to_sort=int(how_to_sort)
            if how_to_sort<=0 or how_to_sort>2:
                print('the input is not valid, it will be sort by default (ascending)') 
                sorted_df=df.sort_values(menu_options[action-1])
                print(sorted_df)
            elif how_to_sort==1:
                sorted_df=df.sort_values(menu_options[action-1])
                print(sorted_df)
            else:
                sorted_df=df.sort_values(menu_options[action-1], ascending=False)
                print(sorted_df)
        except ValueError:
            print('the input is not valid, it will be sort by default (ascending)') 
            sorted_df=df.sort_values(menu_options[action-1])
            print(sorted_df)
except ValueError:
        print('the input is not valid')

print('Average of bridges length based on material:\n', df.groupby('Material')['Bridge Length'].mean())
 

    