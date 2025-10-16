def quicksort(arr):

    _quicksort(arr, 0, len(arr) - 1)

def _quicksort(arr, left, right):
    
    if left < right:  
        pi = partition(arr, left, right)  
        
        _quicksort(arr, left, pi - 1)
        
        _quicksort(arr, pi + 1, right)

def partition(arr, left, right):
   
    pivot = arr[right]  
    
    i = left - 1  

    for e in range(left, right):
        if arr[e] >= pivot:
            i = i+1

            arr[i], arr[e] = arr[e], arr[i]
    arr [i+1], arr[right], = arr[right], arr[i+1]
    return i+1


def calculo_Index_h(citacoes):
    quicksort(citacoes)
    
    print(citacoes)

    for i, citacao in enumerate(citacoes, 1):
        if citacao < i:
            return i - 1 
        
    return len(citacoes) 


citacoes = [10, 8, 5, 4, 3, 31, 15, 7]
indice_h = calculo_Index_h(citacoes)
print("Índice-h:", indice_h)