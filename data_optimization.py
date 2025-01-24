from database import Database
import matplotlib.pyplot as plt

db = Database()

all_datapoints = db.get_all_data()
points_to_check = sorted(list(set(all_datapoints)))
processed_points = [0] * len(points_to_check)

for index, point in enumerate(points_to_check):
    for i in all_datapoints:
        if point <= i:
            processed_points[index] += point

highest_index = 0
highest_value = 0
for index, value in enumerate(processed_points):
    if value > highest_value:
        highest_index = index
        highest_value = value

number_of_points = len(all_datapoints)
total_profit = highest_value / number_of_points

if total_profit > 1:
    print("profitable")
else:
    print("not profitable")
print("optimal number:", points_to_check[highest_index])
print("total profit was a", str(round(total_profit, 3)) + "% multiplier of collective bet ammount over", number_of_points, "plays")

plt.plot(points_to_check, processed_points)
plt.xlabel("Return based on chosen multiplier")
plt.ylabel("Processed Points")
plt.title("Processed Points Line Graph")
plt.show()

db.close()