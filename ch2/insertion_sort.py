input = [4, 9, 21, 7, 5, 1, 65]


def insertion_sort(input):
    sorted = [input[0]]
    for x in input[1:]:
        inserted = False
        for i, y in enumerate(sorted):
            if x < y:
                sorted.insert(i, x)
                inserted = True
                break
        if not inserted:
            sorted.append(x)
    return sorted


def insertion_sort_in_place(input):
    for i in range(1, len(input)):
        for j in range(i):
            if input[i] < input[j]:
                temp = input.pop(i)
                input.insert(j, temp)
                break


# My try at CLRS Version
def insertion_sort_in_place2(input):
    for i in range(1, len(input)):
        key = input[i]
        for j in range(i-1, -1, -1):
            input[j+1] = input[j]
            if key > input[j]:
                input[j+1] = key
                break


# CLRS Version
def insertion_sort_in_place3(input):
    for i in range(1, len(input)):
        key = input[i]
        j = i - 1
        while j >= 0 and input[j] > key:
            input[j+1] = input[j]
            j = j - 1
        input[j+1] = key


def insertion_sort_in_place_nonincreasing(input):
    for i in range(1, len(input)):
        key = input[i]
        j = i - 1
        while j >= 0 and input[j] < key:
            input[j+1] = input[j]
            j = j - 1
        input[j+1] = key


if __name__ == "__main__":
    print(insertion_sort(input))
    input2 = input.copy()
    input3 = input.copy()
    input4 = input.copy()
    insertion_sort_in_place(input2)
    print(input2)
    insertion_sort_in_place2(input3)
    print(input3)
    insertion_sort_in_place3(input4)
    print(input4)
    insertion_sort_in_place_nonincreasing(input4)
    print(input4)
