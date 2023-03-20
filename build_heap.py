# python3


def build_heap(data):
    n = len(data)
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for i in range(n//2, -1, -1):
        min_heapify(data, i, n, swaps)

    return swaps

def min_heapify(data, i, n, swaps):
    smallest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and data[left] < data[smallest]:
        smallest = left

    if right < n and data[right] < data[smallest]:
        smallest = right

    if smallest != i:
        data[i], data[smallest] = data[smallest], data[i]
        swaps.append((i, smallest))
        min_heapify(data, smallest, n, swaps)

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
