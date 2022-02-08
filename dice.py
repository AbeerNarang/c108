import csv
import random
import plotly_express as px
import plotly.figure_factory as ff

dice_result = []
for i in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)
figure = ff.create_distplot([dice_result], ["Result"])    
figure.show()