

example_array = [2,6,3,7,1,8,11,10,9]
example2 = [3,3,3,3,1]
array1 = [1,3]
array2 = [2,4]

def swap(array, i, j):
    a = array[i]
    array[i] = array[j]
    array[j] = a

def selection_sort(array):
    index = 0
    while index < len(array):
        min_index = array.index(min(array[index:]))
        swap(array, index, min_index)
        index += 1
    return array

def bubble_sort(array):
    first_index = 0
    second_index = 1
    right_answers = 0
    while True:
        if right_answers == len(array) -1:
            break
        elif second_index == len(array):
            first_index = 0
            second_index = 1
            right_answers = 0
        else:
            if array[first_index] > array[second_index]:
                swap(array, first_index, second_index)
            else:
                right_answers += 1
            first_index += 1
            second_index += 1
    return array
    

def insertion_sort(array):
    for i in range(len(array)):
        index = i
        while index > 0:
            if array[index - 1] > array[index]:
                swap(array, index - 1, index)
            index -= 1
    return(array)


def split_array(array):
    array_of_arrays = []
    for i in array:
        array_of_arrays.append([i])
    return array_of_arrays

def merge_arrays(left_array, right_array):
    new_array = []
    left_count = 0
    right_count = 0
    while len(new_array) < len(left_array) + len(right_array):
        if left_count >= len(left_array):
            new_array.append(right_array[right_count])
            right_count += 1

        elif right_count >= len(right_array):
            new_array.append(left_array[left_count])
            left_count += 1

        elif left_array[left_count] <= right_array[right_count]:
            new_array.append(left_array[left_count])
            left_count += 1

        elif right_array[right_count] < left_array[left_count]:
            new_array.append(right_array[right_count])
            right_count += 1

    return new_array

def merge_sort(array):
    temp_array = split_array(array)
    index = 0
    while not len(temp_array) <= 1:
        if index >= len(temp_array) - 1:
            index = 0
        merged_array = merge_arrays(temp_array[index], temp_array[index + 1])
        temp_array[index] = merged_array
        temp_array.pop(index + 1)
        index += 1
    return temp_array[0]

#choose sort(example array)

