import pandas as pd

csv_input = pd.read_csv("C:\\Users\\riorio\\Downloads\\data.csv", encoding="shift-jis", 
                        skiprows=5, sep=",", usecols=[0,1], 
                        header=None, names=['time', 'temperature'])
time_col = pd.Series(csv_input['time'])
time_list = []
for tmp in time_col:
    new_date = tmp.split(" ")[1]
    time_list.append(new_date)
csv_input['time'] = pd.Series(time_list)
time_col = csv_input['time']
time_list = []
times = ['0:00', '3:00', '6:00', '9:00', '12:00', '15:00', '18:00', '21:00']

for i in times:
    tmp = csv_input[time_col == i]
    tmp = tmp.mean()
    time_list.append(round(float(tmp)))

print(time_list)

p1 >> pluck(time_list, dur=1,amp=2)
p2 >> pluck([5,3,5,6,9,12,7,9], dur=1,amp=1.75)
d1 >> play("--o--oo-")

p2.stop()
d1.stop()
p1.stop()
