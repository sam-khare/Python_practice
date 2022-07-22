# num = input("Enter a number :")
# num = int(num)
# if num%2 == 0:
#     print(f' {num} - input number is even')
# else:
#     print(f' {num} - input number is odd ')

###############################
Indian = ['Chapati','Daal','Rice']
Chinese = ['Noodle','Soup']
dish = input("Enter your dish")
if dish in Indian:
    print(f'{dish} is an indian dish')
elif dish in Chinese:
    print(f'{dish} is an chinese dish')
else:
    print(f'{dish} is not in database')
