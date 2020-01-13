import os, csv

# Set path for file
csv_path = os.path.join("..", "Resources", "election_data.csv")

# Open the CSV
with open(csv_path, newline='', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    for row in csv_reader:
        print(row)

# total_votes = [0]
# profit_loss = [1] 

# total_month = len[date]
# print(total_month)
# Bonus
# ------------------------------------------
# # Set variable to check if we found the video
# found = False


#     for row in csvreader:
#         if row[0] == video:
#             print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])
