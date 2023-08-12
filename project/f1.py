#Ahmad M , 2023/8/12, **Wish me luck:)**
import requests
import time
import pygame


def check_website(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.ConnectionError:
        return False


def main():
    website_url = "http://tawjihi.jo/"  
    alarm_sound_path = "alarm12.mp3"  # Replace with the path to your alarm sound file

    pygame.init()
    pygame.mixer.init()
    alarm_sound = pygame.mixer.Sound(alarm_sound_path)

    while True:
        while not check_website(website_url):
            print("Website is not live. Checking again in 1 second.")
            time.sleep(1)

        print("Website is live!")
        alarm_sound.play()
        time.sleep(5)  # Wait for 1 second before checking again


if __name__ == "__main__":
    main()
