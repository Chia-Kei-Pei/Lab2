# from bmi import calculate_bmi
#
#
# def main():
#     print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
#     calculate_bmi(weight=57, height=1.73)
#
#
# if __name__ == "__main__":
#     main()

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    nums_raw_input = input()
    nums_string = nums_raw_input.split(",")
    nums_float = [float(x) for x in nums_string]
    return nums_float


def calc_average_temperature(temp_readings):
    total = 0
    num_of_readings = 0
    for num in temp_readings:
        total += num
        num_of_readings += 1
    return total / num_of_readings


def find_min_max(temp_readings):
    min_temp = max_temp = temp_readings[0]
    for num in temp_readings:
        if min_temp > num:
            min_temp = num
        if max_temp < num:
            max_temp = num
    return [min_temp, max_temp]


def sort_temperature(temp_readings):
    temp_readings.sort()
    return temp_readings


import math


def calc_median_temperature(temp_readings):
    temp_reads = sort_temperature(temp_readings)
    median_index = math.ceil(len(temp_reads) / 2) - 1
    # print("median_index = " + str(median_index))
    if len(temp_readings) % 2 == 1:
        return temp_reads[median_index]
    else:
        return 0.5 * (temp_reads[median_index] + temp_reads[median_index + 1])


# testing
display_main_menu()

temperature_list = get_user_input()
print("The temperature list is " + str(temperature_list))

print("The average temperature is " + str(calc_average_temperature(temperature_list)))

print("The min and max temperatures are " + str(find_min_max(temperature_list)))

print("The median temperature is " + str(calc_median_temperature(temperature_list)))
