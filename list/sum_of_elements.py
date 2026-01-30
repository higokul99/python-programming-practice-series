# def sum_list(num_list):
#     sum = 0
#     for i in range(len(num_list)):
#         sum = sum + num_list[i]
#     return sum
#
# if __name__ == '__main__':
#     num_list = list()
#     print("Feed the Below Inputs:")
#     n = int(input("Enter the number of elements: "))
#     for i in range(n):
#         num_list.append(int(input(f"Enter element No {i+1} : ")))
#     print("The list is :", num_list)
#     print("The sum of the elements is: ", sum_list(num_list))




def sum_of_elements(mylist):
    sum = 0
    for i in mylist:
        sum =sum+i

    return sum

if __name__ == '__main__':
    mylist = [10,10,20,10]
    print(sum_of_elements(mylist))