train_passenger = []
for num in range(10):
    disembarking_passengers,passenger = map(int,input().split(" "))
    train_passenger.append([disembarking_passengers,passenger])


def current_Passenger(train_passenger):
    passenger = 0
    passengers = []
    for i in range(10):
        passenger += train_passenger[i][1] - train_passenger[i][0]
        passengers.append(passenger)
    current_Passenger_cnt = max(passengers)
    return current_Passenger_cnt

print(current_Passenger(train_passenger))