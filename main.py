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

    def is_circular(self) -> bool:
        if self.head is None:
            return False
        else:
            return self.head.prev is not None

    def insert_at_end(self, music: Music) -> None:
        newNode = Node(self.data)
        if not self.head:
            self.head = newNode
        else: 
            current = self.head
            while current.next != self.head:
                    current = current.next
            current.next = newNode
            newNode.prev = current
            newNode.next = self.head
            self.head.prev = newNode
                    

    def remove(self, music: Music) -> None:
        newNode = Node(self.data)
        current = newNode

        while current.data.name != music.name:
            previous = current
            current = current.next
            if current.data.name == music.name:
                break
        if current.data.name == music.nameÇ
            previous.next = current.next
        
        else: 
            print("Musica não encontrada!\n")
            



    def move_music(self, from_pos: int, dest_pos: int) -> None:
        pass

    def list_all() -> None:
        pass
