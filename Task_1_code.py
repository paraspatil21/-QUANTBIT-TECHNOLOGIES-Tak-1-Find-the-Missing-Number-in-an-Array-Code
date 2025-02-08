def find_missing_number(arr: list) -> int:
    n = len(arr)
    max_number = n
    expected_sum = max_number * (max_number + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

arr = list(map(int, input("Enter the numbers in the array separated by spaces: ").split()))
print("The missing number is:", find_missing_number(arr))
