#opted for a design that didnt mess about with arrays themselves and purely used pointers
# to exploit the assumption that the array is always sorted in ascending order


def func(x, arr):
    num = 0
    right_pointer = len(arr) - 1
    left_pointer = 0
    
    while left_pointer < right_pointer:
        
        sum = arr[left_pointer] + arr[right_pointer]
        
        if sum == x:
            num += 1
            left_pointer += 1
            right_pointer -= 1
        elif sum < x:
            left_pointer += 1
        elif sum > x:
            right_pointer -= 1
        
    return num
        
        
        
def main():
    X = 42
    Array =  [1, 1, 10, 32, 41]
    print(func(X, Array))

main() 