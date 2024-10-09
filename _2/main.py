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

    def is_circular(self) -> bool:
        if self.head is None:
            return False
        else:
            return self.head.prev is not None

    def insert_at_end(self, music: Music) -> None:
        newNode = Node(music)
        if self.head is None:
            self.head = self.tail = newNode
            return
        
        current = self.tail
        while current.next is not None:
            current = current.next

        current.next = newNode
        newNode.prev = current
        # self.tail.prev = newNode
                    

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


    def move_music(self, from_pos: int, dest_pos: int) -> None:
        pass

    def list_all(self) -> None:
        current = self.head

        while current is not None:
            print("----------MUSIC-----------")
            print(current.data.name)
            print(current.data.artist)
            print(current.data.duration)

            current = current.next
            
        pass


list_playlist = Playlist()

list_playlist.insert_at_end(Music("Borbulhas de Amor", "Fagner", "4:15"))
list_playlist.insert_at_end(Music("Boate Azul", "Leno Brega", "3:20"))
list_playlist.insert_at_end(Music("Seu amor me pegou", "Pablo Vittar", "2:30"))
list_playlist.list_all()

print("###########TENTANDO REMOVER#######################")
list_playlist.remove("Boate Azul")
list_playlist.list_all()


