from collections import abc
import json
import csv
import os

stage_data = []
fields = ['stage_name', 'min_left_blast_zone', 'min_right_blast_zone', 'min_top_blast_zone', 'min_bottom_blast_zone',
          'max_left_blast_zone', 'max_right_blast_zone', 'max_top_blast_zone', 'max_bottom_blast_zone',
          'number_of_ledges', 'stage_width', 'min_edge_to_side_blast_zone', 'max_edge_to_side_blast_zone', 'hasCeiling',
          'hasWallInfinite', 'hasRandom', 'hasWater', 'hasHurt',
          'hasIce',
          'hasWalkOffs', 'hasSymmetry', 'hasTransform', 'has2D']
csvFilename = "stage_data.csv"


def material_in_stage(stage_dict, material):
    match = "\'material\': \'" + material + "\'"
    match2 = "\"material\": \"" + material + "\""
    if match in str(stage_dict) or match2 in str(stage_dict):
        return True


def find_min(current, new):
    if current == "" or current > new:
        return new
    else:
        return current


def find_max(current, new):
    if current == "" or float(current) < new:
        return new
    else:
        return current


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
                min_bounding_box_left = round(data[0]['collisions'][0]['boundingBox'][0][0])
                max_bounding_box_right = round(data[0]['collisions'][0]['boundingBox'][1][0])
                ledge_to_blast = []
                for level in data:
                    blast_zones = level['blast_zones']
                    row['min_left_blast_zone'] = find_min(row['min_left_blast_zone'], round(blast_zones[0], 0))
                    row['max_left_blast_zone'] = find_max(row['max_left_blast_zone'], round(blast_zones[0], 0))
                    row['min_right_blast_zone'] = find_min(row['min_right_blast_zone'], round(blast_zones[1], 0))
                    row['max_right_blast_zone'] = find_max(row['max_right_blast_zone'], round(blast_zones[1], 0))
                    row['min_top_blast_zone'] = find_min(row['min_top_blast_zone'], round(blast_zones[2], 0))
                    row['max_top_blast_zone'] = find_max(row['max_top_blast_zone'], round(blast_zones[2], 0))
                    row['min_bottom_blast_zone'] = find_min(row['min_bottom_blast_zone'], round(blast_zones[3], 0))
                    row['max_bottom_blast_zone'] = find_max(row['max_bottom_blast_zone'], round(blast_zones[3], 0))
                    for collision in level['collisions']:
                        min_bounding_box_left = find_min(min_bounding_box_left,
                                                         round(collision['boundingBox'][0][0], 0))
                        max_bounding_box_right = find_max(max_bounding_box_right,
                                                          round(collision['boundingBox'][1][0], 0))
                    if min_bounding_box_left <= row['min_left_blast_zone']:
                        row['hasWalkOffs'] = True
                        min_bounding_box_left = row['min_left_blast_zone']
                    if max_bounding_box_right >= row['max_right_blast_zone']:
                        row['hasWalkOffs'] = True
                        max_bounding_box_right = row['max_right_blast_zone']
                    ledge_to_blast.append(abs(round(blast_zones[0], 0) - min_bounding_box_left))
                    ledge_to_blast.append(abs(round(blast_zones[1], 0) - max_bounding_box_right))
                row['min_edge_to_side_blast_zone'] = min(ledge_to_blast)
                row['max_edge_to_side_blast_zone'] = max(ledge_to_blast)
                row['stage_width'] = round(max_bounding_box_right - min_bounding_box_left, 0)
                stage_data.append(row)

# writing to csv file
with open(csvFilename, 'w') as csvFile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvFile, fieldnames=fields)

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(stage_data)
