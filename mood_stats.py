import csv


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