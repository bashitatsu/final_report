import numpy as np
import time

def mergesort(num_list):
    # 分割できるまで分割
    if len(num_list) <= 1:
        return num_list

    center = int(len(num_list)/2) # 小数点以下切り捨て

    left = num_list[:center]
    right = num_list[center:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left,right)

def merge(left,right):
    merged_list = []
    l = 0
    r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged_list.append(left[l])
            l += 1
        else:
            merged_list.append(right[r])
            r += 1

    # 余りを結合
    if l < len(left):
        merged_list.extend(left[l:])
    elif r < len(right):
        merged_list.extend(right[r:])
    
    return merged_list

if __name__ == "__main__":
    element_num = 10**8 # 要素数
    np.random.seed(0) # 乱数固定

    # ndarray -> list
    A = np.random.randint(0, 100, element_num).tolist()

    # 時間計測
    start = time.time()
    A = mergesort(A)
    end = time.time() - start
    # print(A)
    print(end)