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
    print("get_user_input")
    nums_raw_input = input()
    nums_string = nums_raw_input.split(",")
    nums_float = [float(x) for x in nums_string]
    return nums_float


def calc_average_temperature(temp_readings):
    print("calc_average")
    total = 0
    num_of_readings = 0
    for num in temp_readings:
        total += num
        num_of_readings += 1
    return total / num_of_readings


def find_min_max(temp_readings):
    print("find_min_max")
    min_temp = max_temp = 0
    for num in temp_readings:
        if min_temp > num:
            min_temp = num
        if max_temp < num:
            max_temp = num
    return [min_temp, max_temp]


def sort_temperature():
    print("sort_temperature")


def calc_median_temperature():
    print("calc_median_temperature")

print(get_user_input())