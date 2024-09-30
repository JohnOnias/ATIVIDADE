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
        pass

    def remove_at(self, index: int) -> None:
        pass

    def move_music(self, from_pos: int, dest_pos: int) -> None:
        pass

    def list_all() -> None:
        pass
