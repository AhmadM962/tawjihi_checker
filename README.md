# tawjihi_checker

This Python script checks the availability of a website and plays an alarm sound when the website is detected as live. It uses the 'requests' library to check the website's status and the 'pygame' library to play the alarm sound.

Requirements

- Python 3.x
- 'requests' library
- 'pygame' library

You can install the required libraries using the following commands:

pip install requests
pip install pygame

Usage

1. Clone or download this repository to your local machine.

2. Make sure you have Python and the required libraries installed.

3. Replace "http://tawjihi.jo/" with the URL of the website you want to monitor in the 'website_url' variable.

4. Replace "alarm12.mp3" with the path to your desired alarm sound file. Ensure that the sound file is in the same directory as the script or provide the correct path.

5. Open a terminal or command prompt, navigate to the directory containing the script, and run the following command:

python website_monitoring.py

6. The script will continuously check the website's status. When the website is detected as live, it will play the alarm sound.

7. To stop the script, press 'Ctrl+C' in the terminal.

Notes

- The code assumes that the alarm sound file is in the same directory as the script. Adjust the path accordingly if needed.
- The effectiveness of monitoring depends on the website's behavior and network conditions.

Disclaimer

This script is provided for educational purposes only. Use it responsibly and ensure that you have the right to monitor the website you're checking. Be mindful of the potential impact on network traffic when repeatedly checking a website's status.
