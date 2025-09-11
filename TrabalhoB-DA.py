class DynamicIntArray:
    def __init__(self, capacity=2):
        if capacity <= 0:
            raise ValueError("Capacidade inicial deve ser maior que 0.")
        self.capacity = capacity
        self.size = 0
        self.data = [0] * self.capacity

    def is_empty(self):
        return self.size == 0

    def get(self, index):
        if not (0 <= index < self.size):
            raise IndexError("Indice Fora dos Limites.")
        return self.data[index]

    def set(self, index, value):
        if not (0 <= index < self.size):
            raise IndexError("Indice Fora dos Limites.")
        self.data[index] = value

    def append(self, value):
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        self.data[self.size] = value
        self.size += 1

    def _resize(self, new_capacity):
        # O print foi mantido para que a saída dos testes continue igual
        print(f"Redimensionando de {self.capacity} para {new_capacity}")
        new_data = [0] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def __str__(self):
        return str(self.data[:self.size])

    def remove_at(self, index):
        if not (0 <= index < self.size):
            raise IndexError("Indice Fora dos Limites.")
        
        removed_value = self.data[index]
        
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
            
        self.size -= 1
        
        if self.size <= self.capacity // 4 and self.capacity > 2:
            new_capacity = max(2, self.capacity // 2)
            self._resize(new_capacity)
            
        return removed_value
    
    def index_of(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                return i
        return -1
    
    def remove(self, value):
        index = self.index_of(value)
        if index != -1:
            self.remove_at(index)
            return True
        return False

    def contains(self, value):
        return self.index_of(value) != -1
    
    def insert(self, index, value):
        if not (0 <= index <= self.size):
            raise IndexError("Indice Fora dos Limites.")
            
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
            
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
            
        self.data[index] = value
        self.size += 1