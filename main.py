class Music:
    def __init__(self, name: str, artist: str, duration: str):
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

    def is_circular(self):
        if self.head is None:
            return False
        return self.head.prev == self.tail and self.tail.next == self.head

    def set_circular(self, marker):
        if marker == "yes":
            if self.head is not None and self.tail is not None:
                self.tail.next = self.head
                self.head.prev = self.tail
                print("Lista circular ativada")
        else:
            if self.head is not None and self.tail is not None:
                self.tail.next = None
                self.head.prev = None
                print("Lista circular desativada")

    def append(self, music: Music) -> None:
        new_node = Node(music)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def remove(self, name) -> None:
        current = self.head
        
        if current is None:
            return 

        while True:
            if current.data.name == name:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev

                if current == self.head: 
                    self.head = current.next
                    if self.head == current: 
                        self.head = None
                        self.tail = None
                if current == self.tail: 
                    self.tail = current.prev

                self.size -= 1
                return

            current = current.next
            if current == self.head: 
                break

    def __len__(self):
        return self.size

    def move(self, index, item):
        if self.head is None:
            raise ValueError("A lista está vazia!")

    
        current = self.head
        found = False

        while True:
            if current.data.name == item:
                found = True
                break
            current = current.next
            if current == self.head:  
                break

        if not found:
            raise ValueError("Item não encontrado na lista!")

      
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev

        if current == self.head: 
            self.head = current.next
        if current == self.tail: 
            self.tail = current.prev

        if index == 0:
          
            current.next = self.head
            if self.head:
                self.head.prev = current
            self.head = current
            current.prev = self.tail 
            self.tail.next = current
        else:
            temp = self.head
            for i in range(index):
                if temp is None or (temp.next == self.head and i < index - 1):
                    raise IndexError("Índice fora do intervalo!")
                temp = temp.next

        
            current.next = temp
            current.prev = temp.prev
            
            if temp.prev:
                temp.prev.next = current
            temp.prev = current
            
            if temp == self.head:
                self.head = current

    def get_player(self):
        return Player(self)

    def list_all(self) -> None:
        current = self.head
        if current is None:
            print("Playlist vazia!")
            return

        while current:
            print("----------MÚSICA-----------")
            print(f"Nome: {current.data.name}")
            print(f"Artista: {current.data.artist}")
            print(f"Duração: {current.data.duration}")
            current = current.next

            if current == self.head: 
                break


class Player:
    def __init__(self, playlist: Playlist):
        self.playlist = playlist
        self.current = playlist.head

    def play(self):
        if self.current is None:
            print('Você chegou ao fim da playlist!')
            return
        
        print(f'Tocando {self.current.data.name} por {self.current.data.artist} ({self.current.data.duration})...')
        self.current = self.current.next



lista = Playlist()


lista.append(Music("Borbulhas de Amor", "Fagner", "4:15"))
lista.append(Music("Boate Azul", "Leno Brega", "3:20"))
lista.append(Music("Seu amor me pegou", "Pablo Vittar", "2:30"))
lista.append(Music("Garota de Ipanema", "Tom Jobim", "3:12"))
lista.append(Music("Apenas Mais Uma de Amor", "Luan Santana", "3:45"))
lista.append(Music("Evidências", "Chitãozinho e Xororó", "4:23"))
lista.append(Music("Eu Sei Que Vou Te Amar", "Vinicius de Moraes", "3:37"))
lista.append(Music("Cazuza", "O Tempo Não Para", "4:25"))
lista.append(Music("Despacito", "Luis Fonsi", "3:47"))
lista.append(Music("Shallow", "Lady Gaga e Bradley Cooper", "3:36"))


lista.list_all()

lista.set_circular("yes")

print("########### TENTANDO REMOVER #######################")
lista.remove("Boate Azul")
lista.list_all()

print("########### TENTANDO MOVER #######################")
lista.move(0, "Seu amor me pegou")
lista.list_all()



print("########### TENTANDO TOCAR A MUSICA #######################")

player = lista.get_player()

for i in range(11):
    player.play()