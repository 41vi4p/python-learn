import time
import sys

def rotating_line_animation():
    spinner = ['|', '/', '-', '\\']
    duration = 10  # Duration of the animation in seconds
    start_time = time.time()
    
    try:
        while time.time() - start_time < duration:
            for symbol in spinner:
                sys.stdout.write(f'\r{symbol} ')  # \r returns to the beginning of the line
                sys.stdout.flush()
                time.sleep(0.1)  # Adjust speed here
        sys.stdout.write('\rDone!      \n')  # Clear spinner and display completion message
    except KeyboardInterrupt:
        sys.stdout.write('\rAnimation interrupted!\n')  # Handle user interruption

if __name__ == "__main__":
    rotating_line_animation()
