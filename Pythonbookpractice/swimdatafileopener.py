import statistics 
FN = 'Darius-13-100m-Fly.txt'

FOLDER='swimdata\\'

with open(FOLDER+FN) as file:
    lines=file.readlines()

swimmer,age,distance,stroke = FN.removesuffix(' .txt').split('-')

times =lines[0].strip().split(',')
converts =[]
for t in times:
    minutes, rest = t.split(":")
    seconds, hundredths = rest.split(".")
    converts.append((int(minutes)* 60 *100) + (int(seconds)*100)+ int(hundredths)) 

average = statistics.mean(converts)
average/100
mins_secs, hundredths = str(round(average/100,2)).split(".")
mins_secs = int(mins_secs)
minutes= mins_secs // 60
seconds = mins_secs - minutes*60
average = str(minutes) + ":" + str(seconds) + ":" + hundredths
print(average)