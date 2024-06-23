# To maintain the health of a programmer. Following are the things implemented in this code:

# Remind user to drink a glass of water every hour.
# Remind user to look at distant objects for 20 seconds after every 20 minutes.
# Reminds user to do physical activity after every 45 minutes.

# The program will play respective ringtone for each reminder.
# The program will also log activity done in a txt file.

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # Hide pygame welcome screen.
from pygame import mixer
from time import time, strftime

def play_music(filename: str, stop_command: str) -> None:
    mixer.init()
    try:
        mixer.music.load(filename)
        mixer.music.set_volume(0.3)
        mixer.music.play()
    except Exception:
        print(f'\nOops! File "{filename}" not Found!')
        print('Make sure file is located in the same folder as the program.')
        exit()

    while True:
        print(f"Enter {stop_command} to stop the alarm or q to quit the program.")
        command: str = input('-> ')

        if command.lower() == 'q':
            exit()
        elif command.lower() == stop_command.lower():
            mixer.music.stop()
            break
        else:
            print(f"Enter {stop_command} to stop the alarm.")
            continue


def log_action(action: str) -> None:
    with open('Health log.txt', 'a') as f:
        f.write(f"{action} at {strftime('%d/%m/%y %H:%M:%S')}\n")


if __name__ == '__main__':
    print('\nWelcome!\n')
    water_timer: float = time()
    eye_timer: float = time()
    exercise_timer: float = time()

    water_reminder: int = 3600 # Remindes to drink water after 1 hour.
    eye_reminder: int = 1200 # Remindes to do eyes exercise after 20 minutes.
    exercise_reminder: int = 2700 # Remindes to do exercise after 45 minutes.

    while True:
        current_time: float = time()
        current_water_time: float = current_time - water_timer # Time since water drank.
        current_eye_time: float = current_time - eye_timer # Time since eyes exercise done.
        current_exercise_time: float = current_time - exercise_timer # Time since physical exercise done.

        if  current_water_time >= water_reminder:
            water_timer = current_time
            print('Time to drink water! Have a glass of water.')
            play_music('water.mp3', 'Drank')
            log_action('Drank water')

        if  current_eye_time >= eye_reminder:
            eye_timer = current_time
            print('Time for eye exercise! Look at distant objects for 20 seconds.')
            play_music('eye.mp3', 'EyDone')
            log_action('Did eye exercise')

        if current_exercise_time >= exercise_reminder:
            exercise_timer = current_time
            eye_timer = current_time # Since doing Physical exercise will also make the eyes relax.
            print('Time for physical exercise. Stand up and do some physical exercise.')
            play_music('physical.mp3', 'ExDone')
            log_action('Did physical exercise')
