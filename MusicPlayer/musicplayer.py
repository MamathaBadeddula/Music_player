import pygame

def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def main():
    file_path = "C:\\Users\\Ruthvika\\Downloads\\Ay Pilla.mp3"  

    while True:
        user_input = input("Enter 'play' to start playing the music or 'stop' to stop: ")

        if user_input == "play":
            play_music(file_path)
        elif user_input == "stop":
            stop_music()
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
