import string
import math
from datetime import datetime, timedelta

class PasswordStrengthChecker:
    
    def __init__(self):
        self.common_passwords = {
            '123456', 'password', 'qwerty', 'admin',
            '123456789', '12345', '1234', '12345678'
        }
        
    def check_strength(self, password):
        score = 0
        feedback = []
        
        if password.lower() in self.common_passwords:
            feedback.append("❌ This is a commonly used password")
            return 0, feedback
        
        if len(password) < 8:
            feedback.append("❌ Password is too short")
        elif len(password) >= 12:
            score += 2
            feedback.append("✅ Good length")
        else:
            score += 1
            feedback.append("⚠️ Password could be longer")
            
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in string.punctuation for c in password)
        
        if has_upper:
            score += 1
            feedback.append("✅ Contains uppercase letters")
        else:
            feedback.append("❌ Missing uppercase letters")
            
        if has_lower:
            score += 1
            feedback.append("✅ Contains lowercase letters")
        else:
            feedback.append("❌ Missing lowercase letters")
            
        if has_digit:
            score += 1
            feedback.append("✅ Contains numbers")
        else:
            feedback.append("❌ Missing numbers")
            
        if has_special:
            score += 1
            feedback.append("✅ Contains special characters")
        else:
            feedback.append("❌ Missing special characters")
            
        return score, feedback
    
    def estimate_crack_time(self, password):
        char_set_size = 0
        if any(c.islower() for c in password):
            char_set_size += 26
        if any(c.isupper() for c in password):
            char_set_size += 26
        if any(c.isdigit() for c in password):
            char_set_size += 10
        if any(c in string.punctuation for c in password):
            char_set_size += len(string.punctuation)
            
        possibilities = char_set_size ** len(password)
        
        crack_times = {
            "Home Computer (1M/s)": possibilities / 1_000_000,
            "High-end GPU (1B/s)": possibilities / 1_000_000_000,
            "Supercomputer (1T/s)": possibilities / 1_000_000_000_000
        }
        
        return crack_times

def format_time(seconds):
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds/60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds/3600:.2f} hours"
    elif seconds < 31536000:
        return f"{seconds/86400:.2f} days"
    elif seconds < 31536000*100:
        return f"{seconds/31536000:.2f} years"
    else:
        return "centuries"

def main():
    checker = PasswordStrengthChecker()
    
    print("=== Password Strength Checker and Crack Time Estimator ===")
    print("\nEnter 'quit' to exit the program")
    
    while True:
        password = input("\nEnter a password to check: ")
        
        if password.lower() == 'quit':
            break
            
        print("\n" + "="*50)
        score, feedback = checker.check_strength(password)
        crack_times = checker.estimate_crack_time(password)
        
        print(f"\nStrength Score: {score} out of 6")
        if score < 3:
            print("Verdict: Weak Password ❌")
        elif score < 5:
            print("Verdict: Moderate Password ⚠️")
        else:
            print("Verdict: Strong Password ✅")
            
        print("\nFeedback:")
        for item in feedback:
            print(item)
            
        print("\nEstimated crack times:")
        for method, seconds in crack_times.items():
            print(f"{method}: {format_time(seconds)}")
        
        print("\n" + "="*50)

main()