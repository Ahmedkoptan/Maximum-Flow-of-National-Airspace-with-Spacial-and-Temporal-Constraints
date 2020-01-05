import pandas as pd
import numpy as np
ua_flights = pd.read_csv('Unitedflights.csv')
aa_flights = pd.read_csv('AAflights.csv')
dl_flights = pd.read_csv('Dlflights.csv')

#i=0
#for index, flight in aa_flights[aa_flights['airline']=='United Airlines'].iterrows():
#    if ((ua_flights['flightn'] == "UA "+str(flight['flightn'])) & (ua_flights['dep_time'] == str(flight['dep_time']).lower()) & (ua_flights['arr_time'] == str(flight['arr_time']).lower()) & (ua_flights['arr_port'] == str(flight['arr_port'])) & (ua_flights['dep_port'] == str(flight['dep_port']))).any():
#        print("Found flight")
#        i += 1
#        print(i)
#    else:
#        print("Could not find flight",flight)

ua_flights['dep_time'] = ua_flights['dep_time'].replace(to_replace='([p])[.]([m])[.]',value='PM',regex=True).replace(to_replace='([a])[.]([m])[.]',value='AM',regex=True)
ua_flights['arr_time'] = ua_flights['arr_time'].replace(to_replace='([p])[.]([m])[.]',value='PM',regex=True).replace(to_replace='([a])[.]([m])[.]',value='AM',regex=True)

ua_flights.to_csv('Unitedflights.csv', index=False, header=True)


all_data = pd.concat([aa_flights, ua_flights], axis=0)

#append capacities to all_data
capacities = pd.read_csv('Capacities.csv')


L = []
for index, capacity in all_data.iterrows():
    L.append(capacities[capacities['labels']==capacity['craft_type']]['capacities'].values[0])

all_data.insert(7, "capacities", L)



#convert AM and PM to 24 hour system
for i in range(len(all_data)):
    all_data['arr_time'].iloc[i] = pd.to_datetime(all_data['arr_time'].iloc[i]).strftime('%H:%M')
    all_data['dep_time'].iloc[i] = pd.to_datetime(all_data['dep_time'].iloc[i]).strftime('%H:%M')


dl_flights = dl_flights.rename(columns={"number": "flightn", "depart": "dep_time","origin":"dep_port","arrive":"arr_time","destination":"arr_port","type":"craft_type","capacity":"capacities"})
for index, flight in dl_flights.iterrows():
    dl_flights.at[index,'flightn'] = dl_flights.at[index,'flightn'].strip()
    dl_flights.at[index, 'dep_time'] = pd.to_datetime(dl_flights.at[index, 'dep_time']).strftime('%H:%M')
    dl_flights.at[index, 'arr_time'] = pd.to_datetime(dl_flights.at[index, 'arr_time']).strftime('%H:%M')

L = []
for index, flight in dl_flights.iterrows():
    #L.append(capacities[capacities['labels']==capacity['craft_type']]['capacities'].values[0])
    L.append("Delta Airlines")

dl_flights.insert(1, "airline", L)

all_data = pd.concat([all_data, dl_flights], axis=0)


L = []
for index, capacity in all_data.iterrows():
    L.append(capacities[capacities['labels']==capacity['craft_type']]['capacities'].values[0])

all_data.drop('capacities',axis =1)
all_data.insert(7, "capacities", L)


#save all_data csv
all_data.to_csv('AllFlights.csv',index=False,header=True)
