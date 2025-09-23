from stack import Stack

class QueueUsingStacks:
    def __init__(self):
        self.pilha_principal = Stack()
        self.pilha_aux = Stack()

    def enqueue(self, data):
        self.pilha_principal.push(data)

    def dequeue(self):
        if self.is_empty():
            return "Fila vazia"
        if self.pilha_aux.is_empty():
            while not self.pilha_principal.is_empty():
                self.pilha_aux.push(self.pilha_principal.pop())
        return self.pilha_aux.pop()

    def is_empty(self):
        return self.pilha_principal.is_empty() and self.pilha_aux.is_empty()

    def __str__(self):
        temp_principal = Stack()
        temp_aux = Stack()
        result = []

        while not self.pilha_aux.is_empty():
            val = self.pilha_aux.pop()
            result.append(val)
            temp_aux.push(val)

        while not self.pilha_principal.is_empty():
            val = self.pilha_principal.pop()
            temp_principal.push(val)

        while not temp_principal.is_empty():
            val = temp_principal.pop()
            result.append(val)
            self.pilha_principal.push(val)

        while not temp_aux.is_empty():
            self.pilha_aux.push(temp_aux.pop())

        if not result:
            return "Fila vazia"

        result[0] = f"{result[0]} (Início)"
        result[-1] = f"{result[-1]} (Fim)"
        return "\n↓\n".join(str(x) for x in result)


if __name__ == "__main__":
    fila = QueueUsingStacks()

    print("\nInserindo: 10, 20, 30")
    fila.enqueue(10)
    fila.enqueue(20)
    fila.enqueue(30)

    print(fila)

    print("\nRemovendo dois elementos:")
    print(fila.dequeue())
    print(fila.dequeue())
    fila.enqueue(40)

    print("\nEstado atual da fila:")
    print(fila)

    print("\nA fila está vazia?", fila.is_empty())

    print("\nRemovendo mais um elemento:")
    print(fila.dequeue())

    print("\nA fila está vazia?", fila.is_empty())

    print(" ")
    print(fila)
