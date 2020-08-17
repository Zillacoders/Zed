
print("Hello! Would you like me to sing a song for you?")

choice = input()

if choice == 'Yes':
    print(song)

elif choice == 'No':
    print("Goodbye")

else:
    quit()

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
