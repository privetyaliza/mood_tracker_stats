import csv
from datetime import date, datetime


input_file = "mood_tracker_stats\mood_tracker.csv"
output_file = "mood_tracker_stats\clean_data.csv"
finput = open(input_file, 'r', encoding='utf-8')
foutput = open(output_file, 'w', newline='', encoding='utf-8')
input_content = csv.reader(finput)
output_content = csv.writer(foutput)

for row in input_content:
    clean_row = [cell if cell != '' else '0' for cell in row[:14]]
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


def formula(period):
    foutput = open(output_file, 'r', encoding='utf-8')
    data = csv.reader(foutput)

    sum_of_moods = 0
    row_of_period = 0

    if period == 'year':
        row_of_period = 1
    elif period == 'month':
        row_of_period = input('Enter the number of the month you want to proceed with. For current month, press Enter:')
        if row_of_period == '':
            row_of_period = datetime.now().month + 1
        else:
            row_of_period = int(row_of_period) + 1
    # else:
    #     return 'Incorrect input'

    next(data)
    for row_num, row in enumerate(data, start=1):
        if row_num <= 17:
            sum_of_moods += int(row[row_of_period]) * coefficients[row[0]]
            print(sum_of_moods)
        else:
            break

    foutput.close()

    return sum_of_moods, row_of_period


def year_formula():
    today = date.today()
    day_of_year = today.timetuple().tm_yday

    sum_of_moods, _ = formula('year')
    satisfaction = round(sum_of_moods/day_of_year * 100)

    return satisfaction


def monthly_formula():
    sum_of_moods, days_in_month = formula('month')
    satisfaction = round(sum_of_moods/days_in_month)

    return satisfaction


#print(f"Overall satisfaction with life on {date.today()}: {year_formula()}%")
print(monthly_formula())