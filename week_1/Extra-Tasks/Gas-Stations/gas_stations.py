def gas_stations(distance, tank_size, stations):
    result = []
    gas_station = []
    count_km = 0
    find_one_if_stations = 0

    while True:
        if count_km + tank_size >= distance:
            break

        for i in stations:
            if i < count_km + tank_size:
                # purvite dve stanci
                gas_station.append(i)
            # izbirame da sprem na maksimalno dalechnata stanciq
            find_one_if_stations = max(gas_station)
        result.append(find_one_if_stations)
        # kolko km sme izminali obshto
        count_km = find_one_if_stations

    return result
