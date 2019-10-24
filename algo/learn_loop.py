# Write a function that takes a list of integer, 
# and then returns True if there is at least 1 negative number in the list.
# Otherwise, it should return false.
def process_list(list):
    for i in list:
        print(i)
        if i < 0:
            print ("found a negative number. Returning")
            return True
    # print ("No negative found")
    return False

# Write a function that takes a list of integer, 
# and then returns True if there is at least 1 even number in the list.
# Otherwise, it should return false.
def process_list2(list):
    return None

# Write a function that takes a list of integer, 
# and then returns True if there is at least 1 one number in the list.
# Otherwise, it should return false.
def process_list3(list):
    return None


# Write a function that takes a list of integer, 
# and then returns True if there is at least 2 negtive numbers in the list.
# Otherwise, it should return false.
def process_list4(list):
    return None

list1 = [ 10, 1, 1000, -2, 3, 5, 7 ]
list2 = [ 10, 1, 1000, 3, 5, 7 ]

# if __name__== "__main__":
print(process_list(list1))
print(process_list(list2))
