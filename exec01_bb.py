def buscaLinear(arr, target):
    print (arr)
    for e in range(len(arr)):
        if arr[e] == target:
            return e
    return "não encontrado"
        
arr = [93, 67, 4, 8, 91, 76, 95, 1, 63, 96]
target = 9

print("Target encontrado na posição: ",buscaLinear(arr, target))

##B)

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
        if arr[e] <= pivot:
            i = i+1

            arr[i], arr[e] = arr[e], arr[i]
    arr [i+1], arr[right], = arr[right], arr[i+1]
    return i+1

def buscaB(arr, target):

    quicksort(arr)

    inicio = 0
    fim = len(arr) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if arr[meio] == target:
            return meio
        elif arr[meio] < target:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1


print("Target encontrado na posição: ", buscaB(arr, target))