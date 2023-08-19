# def ask_user_number_list():
#     num_list = []
#     while True:
#         num = input("Please enter a number or 'done' to finish: ")
#         if num.lower() == 'done':
#             break

#         try:
#             number = int(num)
#         except ValueError:
#             print('Invalid input')
#         else:
#             num_list.append(number)

#     return num_list


# def search_min_and_max(lst):
#     try:
#         return min(lst), max(lst)
#     except ValueError:
#         return None


# if __name__ == '__main__':
#     bounds = search_min_and_max(ask_user_number_list())
#     if bounds is None:
#         print('NO INPUT!')
#     else:
#         print('Maximum number: ', bounds[-1])
#         print('Minimum number: ', bounds[0])
# ask_user_number_list()

def list_numbers_min_max():
    my_list = list()                        # Initialize list
    inp_num = input("Enter a number:")

    while True:
        number = 0.0
        input_number = input('Enter a number: ')
    if input_number == 'done':
        break

    try:
        number = float(input_number)
    except ValueError:
        print('Invalid input')
        quit()

    my_list.append(input_number)

if my_list:
    print('Maximum: ', max(my_list) or None)
    print('Minimum: ', min(my_list) or None)