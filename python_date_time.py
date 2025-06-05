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
