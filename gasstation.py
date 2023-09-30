def can_complete_circuit(gas, cost):
    n = len(gas)
    total_gas = 0  # Total gas in the tank
    current_gas = 0  # Gas in the tank at the current station
    start_station = 0  # Starting station

    for i in range(n):
        # Calculate the difference between gas and cost at the current station
        diff = gas[i] - cost[i]

        # Update the total gas in the tank and the gas at the current station
        total_gas += diff
        current_gas += diff

        # If we run out of gas at the current station, reset the starting station
        if current_gas < 0:
            current_gas = 0
            start_station = i + 1

    # If the total gas is non-negative, it means we can complete the circuit
    if total_gas >= 0:
        return start_station
    else:
        return -1


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
result = can_complete_circuit(gas, cost)
print(result)  # Output: 3 (starting from station 3, we can complete the circuit)
