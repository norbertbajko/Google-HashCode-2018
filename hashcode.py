import copy

unreachable_penalty = -1000000000
distance_penalty_multiplier = 3
input_file = 'd_metropolis.in'
output_file = 'd.txt'


class Car:
    def __init__(self, num):
        self.index = num
        self.x = 0
        self.y = 0
        self.time_to_pickup = []
        self.bonus = []
        self.profit = []

        self.wait_time = 0
        self.actual_ride = -1

        self.empty = True
        self.busy = False
        self.waiting = False

    def calc_time_to_pickup(self):
        self.time_to_pickup = [-1] * len(rides)
        for available in available_rides_index:
            self.time_to_pickup[available] = self.calc_travel_dist(
                self.x, self.y, rides[available][0], rides[available][1])

    def calc_bonus(self):
        self.bonus = [0] * len(rides)
        for available in available_rides_index:
            if self.time_to_pickup[available] < (rides[available][-2] - actual_step):
                self.bonus[available] += bonus

    def calc_profit(self):
        self.profit = []
        for available in available_rides_index:
            if (self.time_to_pickup[available] + ride_profit[available]) < number_of_steps:
                tmp = []
                tmp.append(available)

                if (self.time_to_pickup[available] + ride_profit[available] + actual_step) >= rides[available][-1]:
                    tmp.append(unreachable_penalty)
                else:
                    tmp.append((self.bonus[available] + ride_profit[available] - distance_penalty_multiplier *
                                (rides[available][-2] - actual_step)) - self.time_to_pickup[available])

                tmp.append(self.time_to_pickup[available])

                self.profit.append(tmp)
        self.profit = sorted(self.profit, key=lambda x: (x[1], -x[2]), reverse=True)

    def calc_travel_dist(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def check(self):
        if not self.busy:
            self.calc_time_to_pickup()
            self.calc_bonus()
            self.calc_profit()
        if self.waiting:
            self.profit = []
            self.wait_time -= 1
            if self.wait_time == 0:
                self.waiting = False

    def next_step(self):
        if not self.waiting:
            if not self.empty:
                offset = 2
            else:
                offset = 0

            # print('on the way', rides[self.actual_ride][0 + offset] - self.x,
            # rides[self.actual_ride][1 + offset] - self.y)
            if (rides[self.actual_ride][0 + offset] - self.x) != 0:
                if rides[self.actual_ride][0 + offset] > self.x:
                    self.x += 1
                else:
                    self.x -= 1
            elif (rides[self.actual_ride][1 + offset] - self.y) != 0:
                if rides[self.actual_ride][1 + offset] > self.y:
                    self.y += 1
                else:
                    self.y -= 1

    def on_point(self):
        if not self.waiting:
            if self.empty:
                if self.x == rides[self.actual_ride][0] and self.y == rides[self.actual_ride][1]:
                    if actual_step >= rides[self.actual_ride][-2]:
                        self.empty = False
                    else:
                        self.waiting = True
                        self.wait_time = abs(actual_step - rides[self.actual_ride][-2])
                # else:
                #     None
                #     print('to pickup')
            else:
                if self.x == rides[self.actual_ride][2] and self.y == rides[self.actual_ride][3]:
                    self.busy = False
                    self.empty = True
                # else:
                #     None
                #     print('with passanger')

        # else:
        #     None
        #     print('waiting', self.wait_time)


data = []
with open(input_file, 'r') as f:
    for line in f:
        data.append(line)

data = [[int(y) for y in x.split()] for x in data]
data = list(filter(None, data))


rows, cols, num_of_vehicles, number_of_rides, bonus, number_of_steps = data[0]
# print(rows, cols, num_of_vehicles, number_of_rides, bonus, number_of_steps)

rides = data[1:]

available_rides = [1] * len(rides)
available_rides_index = [i for i in range(len(available_rides)) if available_rides[i] == 1]

ride_profit = [abs(x[0] - x[2]) + abs(x[1] - x[3]) for x in rides]


results = [[] for i in range(num_of_vehicles)]
fleet = [Car(x) for x in range(num_of_vehicles)]

available_rides_index = [i for i in range(len(rides))]
finished = False


for round_counter in range(number_of_steps):
    # print(round_counter)
    actual_step = copy.deepcopy(round_counter)

    for car in fleet:
        car.check()

    for i in range(len(fleet)):
        # print(len([x for x in fleet if not x.busy]), len(available_rides_index))
        if len(available_rides_index) == 0:
            # print('zero remaining job')
            finished = True
            break
        if len([x for x in fleet if not x.busy]) == 0:
            # print('zero free car')
            break
        max_profits = []
        for not_busy_car in [x for x in fleet if not x.busy]:
            # print('job given', len([x for x in fleet if not x.busy]), len(available_rides_index))
            not_busy_car.check()
            # print(not_busy_car.index, not_busy_car.profit, not_busy_car.actual_ride,
            # not_busy_car.empty, not_busy_car.waiting, not_busy_car.busy)
            max_profits.append([
                not_busy_car.index, not_busy_car.profit[0][0],
                not_busy_car.profit[0][1]
            ])
        if len(max_profits) > 0:
            max_profits.sort(key=lambda x: x[1], reverse=True)
            # print(max_profits[0])
            # if actual_step > 0:
            #     print(max_profits[0])
            #     print(actual_step)
            # print(available_rides_index)
            # print()
            max_uber = max_profits[0][0]
            max_ride = max_profits[0][1]

            fleet[max_uber].actual_ride = max_ride

            fleet[max_uber].busy = True

            print('job done', len(available_rides_index))
            available_rides_index.remove(max_ride)
            results[max_uber].append(max_ride)
    if finished:
        break
    for car in fleet:
        if car.busy:
            car.next_step()
            car.on_point()

# summa = 0
# for x in results:
#     summa += len(x)
# print(summa)
# print(results)


def save_file(filename, results):
    with open(filename, 'w') as f:
        for index in range(len(results)):
            line = ' '.join(str(x) for x in [len(results[index])] + results[index]) + '\n'
            f.write(line)


save_file(output_file, results)
