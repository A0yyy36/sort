import PySimpleGUI as sg
import time
import random

#表示部
layout = [[sg.T("ソートの処理時間比較")], 
          [sg.T("要素数"), sg.I("100", k = "n")], 
          [sg.B("実行", k = "btn")], 
          [sg.T("Arr is Good")],
          [sg.T(k = "insertion_sort_good")], 
          [sg.T(k = "selection_sort_good")], 
          [sg.T(k = "bubble_sort_good")], 
          [sg.T(k = "quick_sort_good")], 
          [sg.T(k = "merge_sort_good")],
          [sg.T("Arr is Bad")], 
          [sg.T(k = "insertion_sort_bad")], 
          [sg.T(k = "selection_sort_bad")], 
          [sg.T(k = "bubble_sort_bad")], 
          [sg.T(k = "quick_sort_bad")], 
          [sg.T(k = "merge_sort_bad")]]
win = sg.Window("ソート比較アプリ", layout, 
                font = (None, 14), size = (500, 500))

#ソート処理
def sort():
    n = int(v["n"])    
    
    def insertion_sort(arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def selection_sort(arr):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    def quick_sort_mid(arr, low, high):
        if low < high:
            pi = partition_mid(arr, low, high)
            quick_sort_mid(arr, low, pi)
            quick_sort_mid(arr, pi + 1, high)

    def partition_mid(arr, low, high):
        pivot = arr[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while arr[i] < pivot:
                i += 1
            j -= 1
            while arr[j] > pivot:
                j -= 1
            if i >= j:
                return j
            arr[i], arr[j] = arr[j], arr[i]

    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            merge_sort(L)
            merge_sort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    def measure_time(sort_function, arr):
        start = time.time()
        sort_function(arr)
        end = time.time()
        return end - start

    def measure_time_quick(sort_function, arr):
        start = time.time()
        sort_function(arr, 0, len(arr) - 1)
        end = time.time()
        return end - start
    
    arr_good = list(range(n))
    arr_bad = list(range(n, 0, -1))

    # 挿入ソートの処理時間を計測
    insertion_sort_good_time = measure_time(insertion_sort, arr_good[:])
    insertion_sort_bad_time = measure_time(insertion_sort, arr_bad[:])

    # 選択ソートの処理時間を計測
    selection_sort_good_time = measure_time(selection_sort, arr_good[:])
    selection_sort_bad_time = measure_time(selection_sort, arr_bad[:])

    # バブルソートの処理時間を計測
    bubble_sort_good_time = measure_time(bubble_sort, arr_good[:])
    bubble_sort_bad_time = measure_time(bubble_sort, arr_bad[:])

    # クイックソートの処理時間を計測
    quick_sort_good_time = measure_time_quick(quick_sort_mid, arr_good[:])
    quick_sort_bad_time = measure_time_quick(quick_sort_mid, arr_bad[:])

    # マージソートの処理時間を計測
    merge_sort_good_time = measure_time(merge_sort, arr_good[:])
    merge_sort_bad_time = measure_time(merge_sort, arr_bad[:])

    insertion_sort_good = f"　挿入ソートの処理時間: {insertion_sort_good_time:.6f}秒"
    selection_sort_good = f"　選択ソートの処理時間: {selection_sort_good_time:.6f}秒"
    bubble_sort_good = f"バブルソートの処理時間: {bubble_sort_good_time:.6f}秒"
    quick_sort_good = f"クイックソートの処理時間: {quick_sort_good_time:.6f}秒"
    merge_sort_good = f"　マージソートの処理時間: {merge_sort_good_time:.6f}秒"
    insertion_sort_bad = f"　挿入ソートの処理時間: {insertion_sort_bad_time:.6f}秒"
    selection_sort_bad = f"　選択ソートの処理時間: {selection_sort_bad_time:.6f}秒"
    bubble_sort_bad = f"バブルソートの処理時間: {bubble_sort_bad_time:.6f}秒"
    quick_sort_bad = f"クイックソートの処理時間: {quick_sort_bad_time:.6f}秒"
    merge_sort_bad = f"　マージソートの処理時間: {merge_sort_bad_time:.6f}秒"

    win["insertion_sort_good"].update(insertion_sort_good)
    win["selection_sort_good"].update(selection_sort_good)
    win["bubble_sort_good"].update(bubble_sort_good)
    win["quick_sort_good"].update(quick_sort_good)
    win["merge_sort_good"].update(merge_sort_good)
    win["insertion_sort_bad"].update(insertion_sort_bad)
    win["selection_sort_bad"].update(selection_sort_bad)
    win["bubble_sort_bad"].update(bubble_sort_bad)
    win["quick_sort_bad"].update(quick_sort_bad)
    win["merge_sort_bad"].update(merge_sort_bad)

#実行部
while True:
    e, v = win.read()
    if e == "btn":
        sort()
    if e == None:
        break
win.close()