#python date time
#Python Dates
import datetime
# Example of using the datetime module to get the current date and time
def get_current_datetime():
    return datetime.datetime.now()
# Example of using the get_current_datetime function
def main_datetime():
    current_datetime = get_current_datetime()
    print(f"Current Date and Time: {current_datetime}")
if __name__ == "__main__":
    main_datetime()
#date output
# Example of using the datetime module to format a date
def format_date(date):
    return date.strftime("%Y-%m-%d %H:%M:%S")
# Example of using the format_date function
def main_format_date():
    current_datetime = get_current_datetime()
    formatted_date = format_date(current_datetime)
    print(f"Formatted Date: {formatted_date}")
if __name__ == "__main__":
    main_format_date()
# timedelta output
# Example of using the datetime module to calculate a future date
def calculate_future_date(days):
    current_datetime = get_current_datetime()
    future_date = current_datetime + datetime.timedelta(days=days)
    return future_date
# Example of using the calculate_future_date function
def main_calculate_future_date():
    future_date = calculate_future_date(10)
    print(f"Future Date (10 days later): {future_date}")
if __name__ == "__main__":
    main_calculate_future_date()
# time output
# Example of using the datetime module to get the current time
def get_current_time():
    return datetime.datetime.now().time()
#Creating Date Objects
def main_get_current_time():
    current_time = get_current_time()
    print(f"Current Time: {current_time}")
if __name__ == "__main__":
    main_get_current_time()
# Example of creating a specific date object
def create_specific_date(year, month, day):
    return datetime.date(year, month, day)
# Example of using the create_specific_date function
def main_create_specific_date():
    specific_date = create_specific_date(2023, 10, 1)
    print(f"Specific Date: {specific_date}")
if __name__ == "__main__":
    main_create_specific_date()



