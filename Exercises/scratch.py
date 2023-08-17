# def exercise_4_6():
#     def computepay(h, r):
#         # base conditional for overtime pay
#         if h > 40:
#             return 40*r + (h-40)*1.5*r
#         else:
#             return h*r
#     # input hours and rate per hour 
#     h = input("Enter Hours: ")
#     r = input("Enter rate per hour: ")
#     # ensure input is of type float 
#     try:
#         h = float(h)
#         r = float(r)
#     except:
#         print("Error. Hint: Use a float")
#         exit()
#     # logic into function and print
#     p = computepay(h,r)
#     print("Pay",p)

# exercise_4_6()
        
# n = 5
# while n > 0:
#     print(n)
#     n = n-1
# print('Blastoff!')

# def greet(lang):
#     if lang == 'es':
#         return 'hola'
#     elif lang == 'fr':
#         return 'Bonjour'
#     else:
#         return 'Hello'

# print(greet('en'), 'Michael')

# n = 5 
# while n > 0:
#     print(n)
#     n = n -1 
# print("Blastoff")
# print(n)

# for i in [5,4,3,2,1]:
#     print(i)
# print('Blastoff!')

# friends = ['tammy', 'john', 'wowzey']
# for friend in friends:
#     print('happy wow day:', friend)
# print('doneskeez')

# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('Done!')     

# finishing iterations with continue 
# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

# count = 0 
# print("Before", count)
# for thing in [9,41,12,3,74,15]:
#     count = count+1
#     print(count, thing)
# print('After', count)

 # running count and total 
num = 0
tot = 0.0
while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        fval = float(sval)
    except:
        print("Invalid input")
        continue
    # print(fval)
    num = num + 1
    tot = tot + fval
# print('All Done')
print(tot, num, tot/num)
