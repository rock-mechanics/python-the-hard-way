class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_day = Song(["happy birthday to you", "I donj't want to get sued", "So I will stop right there"])

bulls_on_parade = Song(["They rally around the family", "With pockets full of shell"])

happy_day.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
