# Найти k-ый по величине элемент массива.
# Важно: нельзя просто отсортировать массив. Также не используем кучи.

def quickselect(nums, k):
    k_index = k - 1  # k → индекс с 0
    return _quickselect(nums.copy(), 0, len(nums) - 1, k_index)

def _quickselect(nums, left, right, k_index):
    if left == right:
        return nums[left]

    pivot_index = partition(nums, left, right)

    if k_index == pivot_index:
        return nums[k_index]
    elif k_index < pivot_index:
        return _quickselect(nums, left, pivot_index - 1, k_index)
    else:
        new_k_index = k_index - (pivot_index - left + 1)
        return _quickselect(nums, pivot_index + 1, right, new_k_index)

def partition(nums, left, right):
    pivot = nums[right]
    i = left
    for j in range(left, right):
        if nums[j] <= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[right] = nums[right], nums[i]
    return i
