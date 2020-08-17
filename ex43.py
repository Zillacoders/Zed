class song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

Hit_mebaby = song(["My loneliness is killing me",
                    "I must confess!",
                    "I still believe!"])

killing_thename = song(["Some of those who work forces",
                        "Are the same that burn crosses."])

Hit_mebaby.sing_me_a_song()

killing_thename.sing_me_a_song()
