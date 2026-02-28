import random

class Playlist: 
  def __init__(self, name):
    self.name = name 
    self.songs = []

  def add_song(self, song):
    if song in self.songs: 
      print(f"\n{song} is already in {self.name}.")
    else:
      self.songs.append(song)
      print(f"\n{song} has been added to {self.name}.")

  def remove_song(self, song):
    if song in self.songs: 
      self.songs.remove(song)
      print(f"\n{song} has been removed from {self.name}.")
    else:
      print(f"{song} is not in {self.name}.")

  def song_count(self):
    if not self.songs: 
      print(f"\n{self.name} is empty! Add some songs.")
    else:
      print(f"There are {len(self.songs)} songs in {self.name}.")

  def shuffle(self):
    if not self.songs:
      print(f"\n{self.name} is empty! Add some songs.")
    elif len(self.songs) <= 1: 
      print(f"\nThere is only one song in {self.name}! Add more to shuffle.")
    else:
      random.shuffle(self.songs)
      print(f"\n{self.name} has been shuffled:")
      for i, song in enumerate(self.songs, 1):
        print(f"{i}. {song}")
  
  def show_all(self):
    if not self.songs: 
      print(f"\n{self.name} is empty! Add some songs.")
    else:
      print(f"\nPlaylist: {self.name}")
      for i, song in enumerate(self.songs, 1): 
        print(f"{i}. {song}")

def print_error(e):
  print(f"Error: {e}") 

def get_choice(): 
  while True: 
    try:
      choice = int(input("\nPlaylist Menu:\n1. Add Song\n2. Remove Song\n3. Song Count\n4. Shuffle Songs\n5. Show Playlist\n6. Quit\n"))
      if choice < 1 or choice > 6: 
        raise ValueError("Please select between 1 and 6")
    except ValueError as e:
      print_error(e)
      continue
    else: return choice
      
def song_name(choice): 
  if choice == 1: word = "Add"
  elif choice == 2: word = "Remove" 

  while True: 
    try: 
      name = input(f"\n{word} song: ")
      if name == '':
        raise ValueError("Name can't be left empty.")
    except ValueError as e:
      print_error(e)
      continue
    else: return name

def playlist_name():
  while True: 
    try:
      name = input("Playlist name: ")
      if name == '': 
        raise ValueError("Name can't be left empty.")
    except ValueError as e:
      print_error(e)
      continue
    else: return name

def main(): 
  playlist = Playlist(playlist_name()) 

  while True: 
    choice = get_choice() 

    if choice == 1:
      name = song_name(choice)
      playlist.add_song(name)
    
    elif choice == 2: 
      if not playlist.songs:
        print(f"{playlist.name} has no songs to remove.")
      else:
        name = song_name(choice)
        playlist.remove_song(name)
    
    elif choice == 3: 
      playlist.song_count() 
    
    elif choice == 4:
      playlist.shuffle()
    
    elif choice == 5:
      playlist.show_all()
    
    elif choice == 6: break

if __name__ == "__main__":
  main() 

