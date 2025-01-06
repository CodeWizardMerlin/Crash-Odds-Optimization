from Database import Database

#first array of every element with repeats
#second array of every element with no repeats from the dataset
#third array with the same size as the first to put results in

#use threads to process adding every data point in the data table (threads after I get it working with no threads)

#run each data from first array though the entire second array and += if the data number is less than or equal to the second array num
#add result number to the third array withth e same index as the first array number that was used
#get the index of the largest number in the third array and print the number from the first array with the same index

db = Database()
db.process_file()

all_datapoints = db.get_all_data()
points_to_check = list(set(all_datapoints))
processed_points = [0] * len(all_datapoints)

def process_data(point, index):
    for i in range(len(all_datapoints)):
        if all_datapoints[i] <= point:
            processed_points[index] += all_datapoints[i]

for i in points_to_check:
    process_data(i, points_to_check.index(i))

highest_index = 0
for i in processed_points:
    if i > highest_index:
        highest_index = processed_points.index(i)

print(points_to_check[highest_index])