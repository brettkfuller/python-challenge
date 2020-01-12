import os
import csv


# Set path for file
csvpath = os.path.join("..", "Resources", "budget_data.csv")

with open(csvpath, newline="", encoding="UTF-8")) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)


date = [0]
profit_loss = [1] 

total_month = len[date]
print(total_month)

