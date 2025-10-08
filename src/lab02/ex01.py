def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("Список пуст")
    min_n = nums[0]
    max_n = nums[0]
    for num in nums:
        if num < min_n:
            min_n = num
        if num > max_n:
            max_n = num
    return (min_n, max_n)

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))



def flatten(mat: list[list | tuple]) -> list:
    result = []
    for item in mat:
        if not isinstance(item, (list, tuple)):
            raise TypeError("Строка не строка строк матрицы")
        
        result.extend(item)
    
    return result


#print(min_max([3, -1, 5, 5, 0]))
#print(min_max([42]))
#print(min_max([-5, -2, -9]))
#print(min_max([ ]))
#print(min_max([1.5, 2, 2.0, -3.1]))
#print(flatten([[1, 2], 'ab']))



    
    
        
        
