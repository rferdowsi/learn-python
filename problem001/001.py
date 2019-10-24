import logging


# -----------------------------------------
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

# -----------------------------------------

def find_count(list):
    counter = 0
    for element in list:
        counter += 1
    return counter

def find_sum(list):
    sum = 0
    for element in list:
        sum += element
    return sum

def find_avg(list):
    avg = find_sum(list) / find_count(list)
    return avg

def find_min(list):
    list.sort()
    min_value = list[0]
    return min_value

def find_min2(list):
    minimum = 1000 # Int.max_value
    for element in list:
        if element <= minimum:
            minimum = element
    return minimum

def find_max2(list):
    maximum= 0 # Int.max_value
    for element in list:
        if element > maximum:
            maximum = element
    return maximum

def find_max(list):
    list.sort()
    max_value = list[-1]
    return max_value

def find_even(list):
    count = 0
    for num in list:
        if num > 0 and num % 2 == 0:
            count += 1
    return count

def find_odd(list):
    count = 0
    for num in list:
        if num > 0 and num % 2 == 1:
            count += 1
    return count

def find_median(list):
    list.sort()
    if len(list) % 2 == 0:
        sum = list[int(len(list)/2)] + list[int(len(list)/2 -1)]
        return sum/2

    else:
        return list[int(len(list)/2)]


def std_dev(list):
    n = len(list)
    logging.debug('n = %d', n)
    mean = find_avg(list)
    logging.debug('mean = %d', mean)
    # ss =  sum of square deviaton
    variance = sum((x - mean) ** 2 for x in list)
    logging.debug('variance = %d', variance)

    # return ss
    answer = (variance / (n-1)) ** 0.5 
    return answer

def read_input_file(filename):
    logging.info('Reading input file = %s', filename)
    numbers = []
    with open(filename) as file_handle:
        for line in file_handle: 
            line = line.strip() #or some other preprocessing
            number = int(line)
            numbers.append(number) #storing everything in memory!

    return numbers

def write_file(filename, list):
    logging.info('Writing to output file = %s', filename)
    with open(filename, 'w') as file_handle:
        for line in list:
            file_handle.write(line)


input_old = [
    1,
    5,
    2,
    100,
    3
]


# -----------------------------------------
input = read_input_file('input2.txt')

output_list = []
output_list.append('count = %d\n' % find_count(input))
# print(output_list)
# print('count = %d\n' % find_count(input))
# print (find_count(input))
# print (find_sum(input))
# print (find_avg(input))   
# print (find_min(input))
# print (find_max(input))
# print (find_min2(input))
# print (find_max2(input))
# print (find_even(input))
# print (find_odd(input))
# print (find_median(input))
print (std_dev(input))

write_file('output.txt', output_list)
