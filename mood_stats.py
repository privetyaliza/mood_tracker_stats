import csv
from datetime import date, timedelta


input_file = "mood_tracker_stats\mood_tracker.csv"
output_file = "mood_tracker_stats\clean_data.csv"

finput = open(input_file, 'r')
foutput = open(output_file, 'w', newline='')

input_content = csv.reader(finput)
output_content = csv.writer(foutput)

for row in input_content:
    clean_row = row[:14]
    output_content.writerow(clean_row)

finput.close()

coefficients = {'vo':1, 
                'su': 0.95,
                'ho': 0.85,
                'ra': 0.8,
                'gl': 0.75,
                'sp': 0.7,
                'no': 0.6,
                'st': 0.5,
                'gr': 0.4,
                'mi': 0.35,
                'tr': 0.25,
                'pl': 0.2,
                'ag': 0.2,
                'ty': 0.15,
                'st': 0.1,
                'po': 0.05,
                'ot': 0}


def compound_formula():
    today = date.today()
    day_of_year = today.timetuple().tm_yday


