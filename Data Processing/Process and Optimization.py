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

print("optimal number: ", points_to_check[highest_index])
print("highest value: ", processed_points[highest_index])

plt.plot(points_to_check, processed_points)
plt.xlabel('Return based on chosen multiplier')
plt.ylabel('Processed Points')
plt.title('Processed Points Line Graph')
plt.show()

db.close()