import datetime

year = datetime.date.today().year


birth_year = input('What year were you born?')

print(int(year) - int(birth_year))
 