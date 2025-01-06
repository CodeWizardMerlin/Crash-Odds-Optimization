from Database import Database
import matplotlib.pyplot as plt

db = Database()

all_datapoints = db.get_all_data()
points_to_check = sorted(list(set(all_datapoints)))
processed_points = [0] * len(points_to_check)

#could optimise to be faster with threads
def process_data(index, point):
    for i in all_datapoints:
        if point <= i:
            processed_points[index] += point

for index, point in enumerate(points_to_check):
    process_data(index, point)

highest_index = 0
highest_value = 0
for index, value in enumerate(processed_points):
    if value > highest_value:
        highest_index = index
        highest_value = value

number_of_points = len(all_datapoints)
total_profit = highest_value - number_of_points
profit_per_point = total_profit / number_of_points

if total_profit > 0:
    print("profitable")
else:
    print("not profitable")
print("optimal number:", points_to_check[highest_index])
print("total profit was a", str(round(total_profit, 2)) + "% multiplier of bet ammount over", number_of_points, "plays")
print("average profit per play was", str(round(profit_per_point, 3)) + "% of inital bet")

plt.plot(points_to_check, processed_points)
plt.xlabel('Return based on chosen multiplier')
plt.ylabel('Processed Points')
plt.title('Processed Points Line Graph')
plt.show()

db.close()