numbers = 24 * 60 * 60
unit = "seconds"

def days_to_units(days, custom_message):
    print(f"{days} days are {days * numbers} {unit}")
    print(custom_message)


days_to_units(20, " awesome!!")



#my example

hours_in_day = 24
days_in_year = 365
name = "hours!"

def hours_to_year(years):
    print(f"{years} year has {years * days_in_year} days in a year and {hours_in_day * years * days_in_year}")


hours_to_year(20)
hours_to_year(65)

