import pygame
import os

# Initialize pygame
pygame.init()


pygame.display.set_mode((200, 100))

# Set the directory where your music files are stored
music_dir = "/Users/amitaryan/Documents/GitHub/music_player_project"

music_files = [f for f in os.listdir(music_dir) if f.endswith(".mp3")]


pygame.mixer.init()


def play_music(file):
    pygame.mixer.music.load(os.path.join(music_dir, file))
    pygame.mixer.music.play()

# Create a function to stop music
def stop_music():
    pygame.mixer.music.stop()

# Main loop
while True:
    print("\nMusic Player Menu:")
    print("1. Play Music")
    print("2. Stop Music")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        print("Available music files:")
        for i, file in enumerate(music_files):
            print(f"{i + 1}. {file}")

        selection = int(input("Enter the number of the file you want to play: ")) - 1

        if 0 <= selection < len(music_files):
            play_music(music_files[selection])
        else:
            print("Invalid selection.")

    elif choice == "2":
        stop_music()

    elif choice == "3":
        pygame.quit()
        quit()
