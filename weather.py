import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    # """Takes a temperature and returns it in string format with the degrees
    #     and celcius symbols.

    # Args:
    #     temp: A string representing a temperature.
    # Returns:
    #     A string contain the temperature and "degrees celcius."
    # """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):

    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """

    return datetime.fromisoformat(iso_string).strftime("%A %d %B %Y")




def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    # temp_in_fahrenheit = float()

    return round((float(temp_in_farenheit)-32)*5/9, 1)

    # return temp_in_fahrenheit

    # return round(float((temp_in_farenheit-32)*5/9), 1)



def calculate_mean(weather_data):

    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """

    return sum(map(float, weather_data))/len(weather_data)



def load_data_from_csv(csv_file):
    with open(csv_file, encoding="utf-8") as my_file:
        reader = csv.reader(my_file)
        next(reader)
        my_list = []
        for line in reader:
            if line != []:
                my_list.append(line)

        for line in my_list:
            line[1] = int(line[1])
            line[2] = int(line[2]) 

        
        # my_list = list(map(int, reader))
        # y = ''.join(my_list)
        # z = int(y)




        return my_list

    """Reads a csv file and stores the data in a list.

    
    
    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """


    


def find_min(weather_data):

    min_data = None
    count = 0
    position = 0

    if len(weather_data) == 0:
        return ()
    
    for data in weather_data:
        float_data = float(data) 

        if min_data == None:
            min_data = float_data
        
        elif float_data < min_data:
            min_data = float_data
            position = count

        elif float_data == min_data:
            position = count


        count = count + 1


            
    return min_data, position


    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    pass


def find_max(weather_data):

    max_data = None
    count = 0
    position = 0

    if len(weather_data) == 0:
        return ()
    
    for data in weather_data:
        float_data = float(data) 

        if max_data == None:
            max_data = float_data
        
        elif float_data > max_data:
            max_data = float_data
            position = count

        elif float_data == max_data:
            position = count


        count = count + 1


            
    return max_data, position
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    
    low_temp_in_f = []
    high_temp_in_f = []
    insert_date = []

    low_temp_in_c = []
    high_temp_in_c = []
    
    for row in weather_data:
        insert_date.append(row[0])
        low_temp_in_f.append(row[1])
        high_temp_in_f.append(row[2])



    for item in low_temp_in_f:
        low_temp_in_c.append(convert_f_to_c(item))

    for item in high_temp_in_f:
        high_temp_in_c.append(convert_f_to_c(item))

    low_temp, low_index = find_min(low_temp_in_c)
    high_temp, high_index = find_max(high_temp_in_c)
    
    date_text_low = (convert_date(weather_data[low_index][0]))
    date_text_high = (convert_date(weather_data[high_index][0]))

    mean_low = round(calculate_mean(low_temp_in_c), 1)
    mean_high = round(calculate_mean(high_temp_in_c), 1)


    return (f"{len(weather_data)} Day Overview\n  The lowest temperature will be {low_temp}{DEGREE_SYBMOL}, and will occur on {date_text_low}.\n  The highest temperature will be {high_temp}{DEGREE_SYBMOL}, and will occur on {date_text_high}.\n  The average low this week is {mean_low}{DEGREE_SYBMOL}.\n  The average high this week is {mean_high}{DEGREE_SYBMOL}.\n")
    



    # insert_date = []
    # insert_min = []
    # insert_max = []
    # min_in_c = []
    # max_in_c = []
    # min_temp = []
    # max_temp = []
    # mean_min = []
    # mean_max = []


    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    summary = ""

    for value in weather_data:
        insert_date_text = convert_date(value[0])
        insert_min = (format_temperature(convert_f_to_c(value[1])))
        insert_max = (format_temperature(convert_f_to_c(value[2])))
        summary += (
                        f"---- {insert_date_text} ----\n"
                        f"  Minimum Temperature: {insert_min}\n"
                        f"  Maximum Temperature: {insert_max}\n\n"
                    )

    return summary

