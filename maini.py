def has_duplicates(numbers):

    seen = []
    for number in numbers:
        if number in seen:
            return True
        seen.append(number)
    return False

numbers = list(map(int, input().split()))
print(has_duplicates(numbers))

# assert has_duplicates([0]) True
# assert has_duplicates([0]) True
# assert has_duplicates([1]) False Для примера, с задачей не связано

def find(sorted_list, target):

    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        return left

assert has_duplicates([0]) == True