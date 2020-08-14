import csv
import json
import os

stage_data = []
fields = ['stage_name', 'number_of_ledges', 'hasCeiling',
          'hasWallInfinite', 'hasRandom', 'hasWater', 'hasHurt', 'hasIce', 'hasSymmetry', 'hasTransform', 'has2D']
csvFilename = "empty_data.csv"

for subdir, dirs, files in os.walk(r'stage'):
    for filename in files:
        filepath = subdir + os.sep + filename

        if filepath.endswith(".json"):
            # Opening JSON file
            with open(filepath) as json_file:
                data = json.load(json_file)
                row = {}
                for field in fields:
                    row[field] = ""
                row['stage_name'] = data[0]['stage']
                stage_data.append(row)

# writing to csv file
with open(csvFilename, 'w') as csvFile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvFile, fieldnames=fields)

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(stage_data)