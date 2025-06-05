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
