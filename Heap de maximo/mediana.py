import heapq

def mediana(heap):
    heap_bajo = []
    heap_alto = []
    longitud = len(heap)

    for i in range(longitud):
        numero = heapq.heappop(heap) * -1

        if len(heap_alto) == 0 or numero >= heap_alto[0]:
            heapq.heappush(heap_alto, numero)

        else:
            heapq.heappush(heap_bajo, numero * -1)

        if len(heap_alto) - len(heap_bajo) == 2:
            heapq.heappush(heap_bajo, heapq.heappop(heap_alto))

        elif len(heap_bajo) - len(heap_alto) == 2:
            heapq.heappush(heap_alto, heapq.heappop(heap_bajo) * -1)

    if len(heap_alto) == len(heap_bajo):
        return (heapq.heappop(heap_alto) + heapq.heappop(heap_bajo) * -1) / 2.0

    elif len(heap_alto) > len(heap_bajo):
        return heapq.heappop(heap_alto)
        
    else:
        return heapq.heappop(heap_bajo) * -1
