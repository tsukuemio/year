from datetime import datetime

def get_birth_date():
    day = input("Введите день рождения (дд): ")
    month = input("Введите месяц рождения (мм): ")
    year = input("Введите год рождения (гггг): ")
    return day, month, year

def day_of_week(day, month, year):
    birth_date = datetime(int(year), int(month), int(day))
    return birth_date.strftime("%A")

def is_leap_year(year):
    year = int(year)
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def age_in_years(year):
    current_year = datetime.now().year
    return current_year - int(year)

def print_date_with_stars(day, month, year):
    star_representations = {
        '0': " ***** \n*     *\n*     *\n*     *\n ***** ",
        '1': "   *   \n   *   \n   *   \n   *   \n   *   ",
        '2': " ***** \n      *\n ***** \n*      \n ***** ",
        '3': " ***** \n      *\n ***** \n      *\n ***** ",
        '4': "*     *\n*     *\n ***** \n      *\n      *",
        '5': " ***** \n*      \n ***** \n      *\n ***** ",
        '6': " ***** \n*      \n ***** \n*     *\n ***** ",
        '7': " ***** \n      *\n      *\n      *\n      *",
        '8': " ***** \n*     *\n ***** \n*     *\n ***** ",
        '9': " ***** \n*     *\n ***** \n      *\n ***** "
    }
    
    day_stars = [star_representations[d] for d in day]
    month_stars = [star_representations[m] for m in month]
    year_stars = [star_representations[y] for y in year]
    
    lines = ["", "", "", "", ""]
    
    for d_star in day_stars:
        d_lines = d_star.split('\n')
        for i in range(5):
            lines[i] += d_lines[i] + "  "
    
    for m_star in month_stars:
        m_lines = m_star.split('\n')
        for i in range(5):
            lines[i] += m_lines[i] + "  "
    
    for y_star in year_stars:
        y_lines = y_star.split('\n')
        for i in range(5):
            lines[i] += y_lines[i] + "  "
    
    for line in lines:
        print(line)

day, month, year = get_birth_date()
print(f"День недели: {day_of_week(day, month, year)}")
print(f"Високосный год: {'Да' if is_leap_year(year) else 'Нет'}")
print(f"Ваш возраст: {age_in_years(year)} лет")
print("Дата рождения (дд мм гггг) в виде звёздочек:")
print_date_with_stars(day, month, year)
