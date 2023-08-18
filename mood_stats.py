import csv


input_file = "mood_tracker.csv"
output_file = "clean_data.csv"

with open(input_file, 'r') as finput, open(output_file, 'w', newline='') as foutput:
    input_content = csv.reader(finput)
    output_content = csv.writer(foutput)
    useless_content = '"'
    for row in input_content:
        print(row)
        clean_row = row[:14]
        output_content.writerow(clean_row)