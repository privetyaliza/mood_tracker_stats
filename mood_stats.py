import csv
from datetime import date, datetime
import calendar


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
    col_of_period = 0
    monthly_sums = {month: 0 for month in calendar.month_name[1:]}

    if period == 'year':
        col_of_period = 1
        days_in_month = 0

    elif period == 'month':
        col_of_period = input('Enter the number of the month you want to proceed with. For current month, press Enter:')
        if col_of_period == '':
            col_of_period = datetime.now().month + 1
            days_in_month = datetime.now().day
        else:
            col_of_period = int(col_of_period) + 1
            days_in_month = calendar.monthrange(datetime.now().year, col_of_period-1)[1]

    elif period == 'all_months':
        next(data)

        for row in data:
            if row[0] == '-':
                break
            for month_num, value in enumerate(row[2:], start=1):
                month_name = calendar.month_name[month_num]
                monthly_sums[month_name] += int(value) * coefficients[row[0]]

        for month, total_sum in monthly_sums.items():
            monthly_sums[month] = total_sum

        return monthly_sums
    
    foutput.seek(0)
    next(data)
    for row_num, row in enumerate(data, start=1):
        if row_num <= 17:
            sum_of_moods += int(row[col_of_period]) * coefficients[row[0]]
        else:
            break

    foutput.close()

    return sum_of_moods, days_in_month


def year_formula():
    today = date.today()
    day_of_year = today.timetuple().tm_yday

    sum_of_moods, _ = formula('year')
    satisfaction = round(sum_of_moods/day_of_year * 100)

    return satisfaction


def monthly_formula():
    sum_of_moods, days_in_month = formula('month')
    satisfaction = round(sum_of_moods/days_in_month * 100)

    return satisfaction


def all_months():
    months = formula('all_months')
    for month, total_sum in months.items():
        days_in_month = calendar.monthrange(datetime.now().year, list(calendar.month_name).index(month))[1]
        months[month] = total_sum / days_in_month * 100
    
    for key, value in months.items():
        print(f'{key}: {round(value)}%')
    return
        


def main():
    while True:
        choice = input('Enter "y" if you want to see results for the whole year, "m" if you want to see it for some month, and q for quitting:')
        if choice == 'y':
            print(f"Overall satisfaction with life on {date.today()}: {year_formula()}%")
        elif choice == 'm':
            print(f"Overall satisfaction with life on the given month: {monthly_formula()}%")
        elif choice == 'am':
            all_months()
        elif choice == 'q':
            return 0


if __name__ == "__main__":
    main()