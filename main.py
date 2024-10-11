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
        self.size = 0
    

    def is_circular(self):
        if self.head is None:
            return False

        return self.head.prev == self.tail and self.tail.next == self.head

    def set_circular(self, marcador):
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
            self.head = newNode
        else:
            tail = self.tail
            tail.next = newNode
            newNode.prev = tail.prev
        self.size += 1

        

    def remove(self, name) -> None:
        current = self.head
        before = None
        while current is not None and current.next != self.head:
            if current.data.name != name:
                before = current
                current = current.next
            else:
                break
    
        if before:
            before.next = current.next

            # Caso de lista circular
            if current == self.head:
                self.head = current.next
        else:
            #Cabeça
            self.head = current.next

        if current.next:
            current.next.prev = before
        
        self.size = self.size - 1


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

    def get_player(self):
        return Player(self)

    def list_all(self) -> None:
        tail = self.tail 
        current = self.head
        while current is not None:
            print("----------MUSIC-----------")
            print(current.data.name)
            print(current.data.artist)
            print(current.data.duration)

            if current == tail:
                break

            current = current.next

class Player:
    def __init__(self, playlist: Playlist):
        self.playlist = playlist
        self.current = playlist.head

    def play(self):
        if self.current == None:
            print('You have reached the end of the playlist!')
            return
        
        print(f'Playing {self.current.data.name} by {self.current.data.artist} ({self.current.data.duration})...')

        self.current = self.current.next


lista = Playlist()

lista.append(Music("Borbulhas de Amor", "Fagner", "4:15"))
lista.append(Music("Boate Azul", "Leno Brega", "3:20"))
lista.append(Music("Seu amor me pegou", "Pablo Vittar", "2:30"))
lista.list_all()

lista.set_circular("yes")

player = lista.get_player()

print("###########TENTANDO REMOVER #######################")
lista.remove("Boate Azul")
lista.list_all()
len(lista)

print("###########TENTANDO MOVER #######################")
lista.move(0, "Seu amor me pegou")
lista.set_circular("yes")

lista.list_all()