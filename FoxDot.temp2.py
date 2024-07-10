import pandas as pd

csv_input = pd.read_csv("C:\\Users\\riorio\\Downloads\\data.csv", encoding="shift-jis", 
                         skiprows=5, sep=",", usecols=[0,1], 
                         header=None, names=['time', 'temperature'])
time_col = pd.Series(csv_input['time'])
time_list = []
for tmp in time_col:
    new_data = tmp.split(" ")[1]
    time_list.append(new_data)
csv_input['time'] = pd.Series(time_list)
time_list = []
tmp = csv_input[csv_input['time'] == '12:00']
print(list(tmp['temperature']))
tmp = tmp['temperature'].rolling(10).mean()
data = list(tmp.dropna())
tmp = []
for n in data:
    tmp.append(float(format(n, '.1f')))
print(tmp)

p1 >> sawbass(tmp,dur=[1,1,1/4,1/4,1/2,1/2,1,1,1/3,1/3,1/3],oct=5,amp=4)
d1 >> play("-",amp=2) 
d2 >> play("xo xo o o",dur=[1,1,2,1/2,1/2,1/2,1/3,1/3,1/3])

Clock.clear()
