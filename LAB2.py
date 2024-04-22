import statistics
def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
    user_input=get_user_input()
    calc_average_temperature(user_input)
    calc_min_max_temperature(user_input)
    find_median_temperature (user_input)

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()

def get_user_input():
    userinput=input("Enter numbers =" )
    numlist=userinput.split(",")
    new_list = [float(x) for x in numlist]
    return new_list

def calc_average_temperature(user_input):
    average=sum(user_input)/len(user_input)
    print("average =", average)
    return average

def calc_min_max_temperature(user_input):
   min_num=min(user_input)
   max_num=max(user_input)
   print("max =", max_num)
   print("min =", min_num)

def find_median_temperature (user_input):
    sorted_input=sorted(user_input)
    median=statistics.median(sorted_input)
    print("median =", median)

main()

  