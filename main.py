class Music:
    def __init__(self, name: str, artist: str, duration: int):
        self.name = name
        self.artist = artist
        self.duration = duration

class Node:
    def __init__(self, data: Music):
        self.data = data
        self.prev = None
        self.next = None
      
class Playlist:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0 

    def is_circular(self, marcador):
        if marcador == "yes":
            self.tail.next = self.head
            self.head.prev = self.tail
            print("Lista circular ativada")
        else:
            self.head.prev is not None
            print("Lista circular desativada")
        
        


    def append(self, music: Music) -> None:
        newNode = Node(music)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.size += 1

        

    def remove(self, name) -> None:
        current = self.head
        temp = None
        while current is not None:
            if current.data.name != name:
                temp = current
                current = current.next
            break
        
        temp.next = current.next
        current.next = temp
        current.next.prev = temp
        temp.prev = current
        self.size = self.size-1


    def __len__(self):
        return self.size
    


    def move(self, index, item):
        current = self.head
        prev = None
        while current is not None:
            if current.data.name == item:
                break
            prev = current
            current = current.next
        else:
            raise IndexError("List index out of range!")

        if prev is not None:
            prev.next = current.next
        else:
            self.head = current.next

        temp = self.head
        prev = None
        for i in range(index):
            if temp is None:
                raise IndexError("List index out of range!")
            prev = temp
            temp = temp.next

        if prev is not None:
            prev.next = current
        else:
            self.head = current
        current.next = temp



    def list_all(self) -> None:
        current = self.head
        while current is not None:
            print("----------MUSIC-----------")
            print(current.data.name)
            print(current.data.artist)
            print(current.data.duration)
            current = current.next






lista = Playlist()

lista.append(Music("Borbulhas de Amor", "Fagner", "4:15"))
lista.append(Music("Boate Azul", "Leno Brega", "3:20"))
lista.append(Music("Seu amor me pegou", "Pablo Vittar", "2:30"))
lista.list_all()

print("###########TENTANDO REMOVER #######################")
lista.list_all()
len(lista)
print("###########TENTANDO MOVER #######################")
lista.move(1, "Seu amor me pegou")
lista.list_all()
lista.is_circular("yes")
