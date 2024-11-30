from random import random
import csv

class Homework():
    def __init__(self,blue,red,green):
        self.blue = blue
        self.red = red
        self.green = green

    def blue_balls(self):
        for _ in range(self.blue):
            ball = random()
            if (0 <= ball) and (ball <= 0.2):
                pass
            elif (0.2 < ball) and (ball <= 0.6):
                self.blue -= 1
                self.red += 1
            else :
                self.blue -= 1
                self.green += 1 
        return f"{self.blue}, {self.red}, {self.green}"

    def red_balls(self):
        for _ in range(self.red):
            ball = random()
            if (0 <= ball) and (ball <= 0.2):
                self.blue += 1
                self.red -= 1
            elif (0.2 < ball) and (ball <= 0.6):
                pass
            else :
                self.red -= 1
                self.green += 1
        return f"{self.blue}, {self.red}, {self.green}"        

    def green_balls(self):
        for _ in range(self.green):
            ball = random()
            if (0 <= ball) and (ball <= 0.2):
                self.blue += 1
                self.green -= 1
            elif (0.2 < ball) and (ball <= 0.6):
                self.green -= 1
                self.red += 1
            else :
                pass
        return f"{self.blue}, {self.red}, {self.green}" 

homework = Homework(20,20,20)
with open("simulation.csv","w",newline='') as file:
    writer = csv.writer(file)
    labels = ["Time","Blue","Red","Green"]
    writer.writerow(labels)
    for time in range(101):
        homework.blue_balls()
        homework.red_balls()
        data = [str(time)]
        y = 3
        for x in homework.green_balls().split(","):
            if y % 3 == 0:
                data.append(" " + str(x)) 
            else:
                data.append(str(x))
            y += 1  
        writer.writerow(data)
