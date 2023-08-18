import csv
from datetime import date


input_file = "mood_tracker_stats\mood_tracker.csv"
output_file = "mood_tracker_stats\clean_data.csv"

with open(input_file, 'r', encoding='utf-8') as finput, open(output_file, 'w', newline='', encoding='utf-8') as foutput:
    input_content = csv.reader(finput)
    output_content = csv.writer(foutput)

    for row in input_content:
        clean_row = [cell if cell != '' else '0' for cell in row[:14]]  # Replace empty spaces with '0'
        output_content.writerow(clean_row)


finput.close()
foutput.close()

coefficients = {'восхитительно': 1, 
                'супер': 0.95,
                'хорошо': 0.85,
                'глубоко': 0.75,
                'работоспособно': 0.8,
                'спокойно': 0.7,
                'нормально': 0.6,
                'мимо': 0.35,
                'странно': 0.5,
                'тревожно': 0.25,
                'грустно': 0.4,
                'тяжело': 0.15,
                'плохо': 0.2,
                'стрессово': 0.1,
                'по-больному': 0.05,
                'агрессивно': 0.2,
                'отвратительно': 0}


def compound_formula():
    today = date.today()
    day_of_year = today.timetuple().tm_yday

    foutput = open(output_file, 'r', encoding='utf-8')
    data = csv.reader(foutput)

    sum_of_moods = 0

    next(data)
    for row_num, row in enumerate(data, start=1):
        if row_num <= 17:

            sum_of_moods += int(row[1]) * coefficients[row[0]]
            print(sum_of_moods)
        else:
            break



compound_formula()