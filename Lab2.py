def display_main_menu():
    print('Enter some numbers separated by commas (eg.5,67,32)')

def get_user_input():
   numbers = input("Enter numbers:")
   list = numbers.split(",")
   for i in range(0,len(list)):
       list[i] = float(list[i])

   return list



def calc_average_temperature(num_list):
    total = 0
    for i in range (0,len(num_list)):
        total = total + num_list[i]
    average = total/len(num_list)
    print (average)






def main():
    print("ET0735  (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average_temperature(num_list)

if __name__ == "__main__":
    main()

