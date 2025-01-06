from Database import Database
import matplotlib.pyplot as plt

db = Database()

all_datapoints = db.get_all_data()
points_to_check = sorted(list(set(all_datapoints)))
processed_points = [0] * len(points_to_check)

def process_data(index, point):
    for i in all_datapoints:
        if point <= i:
            processed_points[index] += point

for index, point in enumerate(points_to_check):
    process_data(index, point)

highest_index = 0
for i in processed_points:
    if i > highest_index:
        highest_index = processed_points.index(i)

print("optimal number: ", points_to_check[highest_index])
print("index: ", highest_index)

plt.plot(points_to_check, processed_points)
plt.xlabel('Data Points')
plt.ylabel('Processed Points')
plt.title('Processed Points Line Graph')
plt.show()

db.close()