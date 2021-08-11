import numpy as np
import time
import multiprocessing as mp
import math

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

def merge(*args): # 可変長変数
    left, right = args[0] if len(args) == 1 else args # 三項演算子
    l, r = 0, 0
    merged_list = []

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

def parallel_mergesort(data):
    processes = mp.cpu_count() # cpuの数を調べる
    pool = mp.Pool(processes=processes) # process作成
    size = int(math.ceil(float(len(data)) / processes)) # data数 / process数

    # 等分したdataを要素とした2次元配列を作成
    data = [data[i * size:(i + 1) * size] for i in range(processes)]
    data = pool.map(mergesort, data) # 並列分割
    
    while len(data) > 1:
        extra = data.pop() if len(data) % 2 == 1 else None # 三項演算子
        data = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
        data = pool.map(merge, data) + ([extra] if extra else []) # 並列
    return data[0]

if __name__ == "__main__":
    element_num = 10**8 # 要素数
    np.random.seed(0) # 乱数固定

    # ndarray -> list
    A = np.random.randint(0, 100, element_num).tolist()

    # 時間計測
    start = time.time()
    A = parallel_mergesort(A)
    end = time.time() - start
    # print(A)
    print(end)