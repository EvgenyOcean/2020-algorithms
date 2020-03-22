#Could be an alternative for the task in dynamic.py. Although it won't work perfectly, but still acceptable. 
#Here is the classic case where I might wanna use greedy algorithm: 
#1. Find coverage or All of sth

states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "са", "az"])

stations = {} 
stations["kone"] = set(["id", "nv", "ut"]) 
stations["ktwo"] = set(["wa", "id", "mt"]) 
stations["kthree"] = set(["or", "nv", "са"])
stations["kfour"] = set(["nv", "ut"]) 
stations["kfive"] = set(["ca", "az"])

needed_stations = []

def finding_stations(stations, states_needed):
    while states_needed:
        best_station_seq = set()
        best_station_name = ''
        for station_name, states_covering in stations.items():
            check = states_needed & states_covering
            if len(check) > len(best_station_seq):
                best_station_seq = check
                best_station_name = station_name

        states_needed -= best_station_seq
        needed_stations.append(best_station_name)

finding_stations(stations, states_needed)
print(needed_stations)

