# Cybersecurity Tools Documentation

## Table of Contents

1. [Password Strength Checke] (#password-strength-checker)
2. [Caesar Cipher](#caesar-cipher)
3. [Basic Keylogger](#basic-keylogger)
4. [Advanced Keylogger](#advanced-keylogger)
5. [Image Encryption Tool](#image-encryption-tool)

## Introduction

This documentation covers a collection of cybersecurity tools developed for educational purposes. Each tool demonstrates different aspects of security concepts and programming techniques.

⚠️ **Important Notice**: These tools are for educational purposes only. Use them responsibly and only on systems you own or have explicit permission to test.

---

# 1. Password Strength Checker

## Overview

The Password Strength Checker is a Python-based tool that analyzes password security by evaluating various criteria and estimating crack times using different computational methods.

## Features

- Password complexity analysis
- Crack time estimation
- Common password detection
- Real-time feedback
- Multiple attack scenario simulations

## Technical Specifications

### Class: PasswordStrengthChecker

#### Attributes

- `common_passwords`: Set of commonly used passwords
- `LETTERS`: String containing uppercase alphabet characters

#### Methods

##### `__init__(self)`

Initializes the password checker with predefined common passwords.

##### `check_strength(self, password)`

Analyzes password strength based on multiple criteria.

**Parameters:**

- `password` (str): Password to analyze

**Returns:**

- `tuple`: (score, feedback)
  - `score` (int): 0-6 rating
  - `feedback` (list): List of improvement suggestions

**Criteria:**

1. Length check (0-2 points)
   - < 8 characters: 0 points
   - 8-11 characters: 1 point
   - ≥ 12 characters: 2 points
2. Character variety (0-4 points)
   - Uppercase letters: +1 point
   - Lowercase letters: +1 point
   - Numbers: +1 point
   - Special characters: +1 point

##### `estimate_crack_time(self, password)`

Estimates time required to crack the password using different methods.

**Parameters:**

- `password` (str): Password to analyze

**Returns:**

- `dict`: Estimated crack times for different scenarios
  - Home Computer (1M/s)
  - High-end GPU (1B/s)
  - Supercomputer (1T/s)

## Usage Example

```python
checker = PasswordStrengthChecker()
password = "MySecurePass123!"
score, feedback = checker.check_strength(password)
crack_times = checker.estimate_crack_time(password)
```

## Security Considerations

- Tool is for educational purposes only
- Does not store or transmit passwords
- Local analysis only
- Not a substitute for professional security audit

## Best Practices

1. Use passwords ≥ 12 characters
2. Mix character types
3. Avoid common patterns
4. Use unique passwords for each service

## Dependencies

- Python 3.6+
- No external libraries required

## Error Handling

- Invalid input handling
- Edge case management
- Non-ASCII character support

---

# 2.Caesar Cipher

## Overview

The Caesar Cipher implementation provides both encryption and decryption capabilities for text using the classical shift cipher algorithm.

## Features

- Text encryption/decryption
- Case preservation
- Special character handling
- Brute force decryption option

## Technical Specifications

### Class: CaesarCipher

#### Attributes

- `LETTERS`: String containing uppercase alphabet characters

#### Methods

##### `encrypt(self, message, shift)`

Encrypts a message using the Caesar Cipher algorithm.

**Parameters:**

- `message` (str): Text to encrypt
- `shift` (int): Number of positions to shift (1-25)

**Returns:**

- `str`: Encrypted message

##### `decrypt(self, message, shift)`

Decrypts a Caesar Cipher encrypted message.

**Parameters:**

- `message` (str): Encrypted text
- `shift` (int): Original shift value used for encryption

**Returns:**

- `str`: Decrypted message

##### `show_all_possibilities(self, message)`

Shows all possible shift combinations for brute force approach.

**Parameters:**

- `message` (str): Encrypted text

**Returns:**

- `list`: All possible decryptions (shift 0-25)

## Algorithm Details

### Encryption Process

1. Character processing:

   ```python
   new_position = (current_position + shift) % 26
   ```

2. Case preservation:
   ```python
   if char.isupper():
       result = encrypted_char.upper()
   else:
       result = encrypted_char.lower()
   ```

### Character Handling

- Alphabetic characters: Shifted according to cipher
- Spaces: Preserved as-is
- Special characters: Unchanged
- Case: Maintained

## Usage Example

```python
cipher = CaesarCipher()
message = "Hello, World!"
shift = 3

# Encryption
encrypted = cipher.encrypt(message, shift)

# Decryption
decrypted = cipher.decrypt(encrypted, shift)

# Brute Force
all_possibilities = cipher.show_all_possibilities(encrypted)
```

## Security Considerations

- Classical cipher (not cryptographically secure)
- Educational purposes only
- Vulnerable to:
  - Frequency analysis
  - Known plaintext attacks
  - Brute force (only 25 possibilities)

## Best Practices

1. Use for educational purposes only
2. Not suitable for sensitive data
3. Combine with other techniques for learning
4. Understand historical context

## Dependencies

- Python 3.6+
- No external libraries required

## Error Handling

- Invalid shift value handling
- Non-ASCII character support
- Edge case management

---

# 3. Basic Keylogger

## Overview

A simple keylogger implementation for educational purposes that captures and logs keyboard inputs to a file. This tool demonstrates basic input monitoring and file handling in Python.

## ⚠️ Important Notice

This tool is for **EDUCATIONAL PURPOSES ONLY**. Using keyloggers without explicit permission is illegal and unethical.

## Features

- Real-time keyboard monitoring
- Timestamp logging
- File-based storage
- Clean exit mechanism
- Special key handling

## Technical Specifications

### Class: SimpleKeylogger

#### Attributes

- `filename`: Target log file path
- `start_time`: Logging session start timestamp

#### Methods

##### `__init__(self, filename="keylog.txt")`

Initializes the keylogger with specified log file.

**Parameters:**

- `filename` (str): Path to log file (default: "keylog.txt")

##### `get_char(self, key)`

Converts key press to loggable character.

**Parameters:**

- `key`: pynput.keyboard.Key object

**Returns:**

- `str`: String representation of key

##### `on_press(self, key)`

Handles key press events.

**Parameters:**

- `key`: pynput.keyboard.Key object

##### `on_release(self, key)`

Handles key release events.

**Parameters:**

- `key`: pynput.keyboard.Key object

**Returns:**

- `bool`: False to stop listener if ESC key

##### `start(self)`

Initiates the keylogger.

## Implementation Details

### Logging Format

```python
[2025-03-26 14:30:45.123] Key: a
[2025-03-26 14:30:45.234] Key: b
[2025-03-26 14:30:45.345] Key: Key.space
```

### Key Handling

```python
def get_char(self, key):
    try:
        return key.char  # Regular character
    except AttributeError:
        return str(key)  # Special key
```

## Usage Example

```python
# Initialize keylogger
keylogger = SimpleKeylogger("my_log.txt")

# Start logging
keylogger.start()
```

## Dependencies

- Python 3.6+
- pynput library

## Installation

```bash
pip install pynput
```

## Security Considerations

- Tool can be detected by antivirus software
- Logs contain sensitive information
- Secure log file storage required
- Administrative privileges may be needed

## Best Practices

1. Use only on authorized systems
2. Secure log files
3. Clear logs regularly
4. Monitor resource usage
5. Implement secure exit mechanism

## Error Handling

- File I/O error management
- Invalid key handling
- Permission error handling
- Resource cleanup

---

# 4. Advanced Keylogger

## Overview

An enhanced keylogger implementation with advanced features including mouse tracking, system information collection, and statistical analysis.

## ⚠️ Important Notice

This tool is for **EDUCATIONAL PURPOSES ONLY**. Unauthorized use is illegal and unethical.

## Features

- Keyboard input logging
- Mouse movement tracking
- Mouse click logging
- System information collection
- Real-time statistics
- Multiple log file management
- JSON formatted logs
- Session management

## Technical Specifications

### Class: AdvancedKeylogger

#### Attributes

- `log_dir`: Directory for log files
- `keyboard_log`: Keyboard events log file
- `mouse_log`: Mouse events log file
- `statistics_log`: Statistics and system info file
- `start_time`: Session start timestamp
- `running`: Operational status flag

#### Methods

##### `__init__(self, log_dir="logs")`

Initializes the advanced keylogger.

**Parameters:**

- `log_dir` (str): Directory for storing logs

##### `on_press(self, key)`

Handles keyboard press events.

**Parameters:**

- `key`: pynput.keyboard.Key object

##### `on_click(self, x, y, button, pressed)`

Handles mouse click events.

**Parameters:**

- `x`, `y`: Click coordinates
- `button`: Mouse button
- `pressed`: Press/release flag

##### `on_move(self, x, y)`

Handles mouse movement events.

**Parameters:**

- `x`, `y`: Current coordinates

##### `update_statistics(self)`

Updates usage statistics in real-time.

## Implementation Details

### Log Structure

```python
# Keyboard Log (JSON)
{
    "timestamp": "2025-03-26 14:30:45.123",
    "event": "keypress",
    "key": "a"
}

# Mouse Log (JSON)
{
    "timestamp": "2025-03-26 14:30:45.234",
    "event": "click",
    "button": "Button.left",
    "position": {"x": 100, "y": 200}
}

# Statistics Log (JSON)
{
    "start_time": "2025-03-26 14:30:45",
    "duration_seconds": 3600,
    "keystrokes": 1000,
    "mouse_clicks": 150,
    "mouse_movements": 5000
}
```

### System Information Collection

```python
system_info = {
    "OS": platform.system(),
    "OS Version": platform.version(),
    "Machine": platform.machine(),
    "Processor": platform.processor()
}
```

## Usage Example

```python
# Initialize advanced keylogger
keylogger = AdvancedKeylogger("secure_logs")

# Start logging
keylogger.start()
```

## Dependencies

- Python 3.6+
- pynput
- json
- platform
- threading

## Installation

```bash
pip install pynput
```

## Security Considerations

- Enhanced detection risk
- Multiple log file security
- System resource usage
- Administrative privileges required
- Anti-analysis detection possible

## Best Practices

1. Secure log directory
2. Regular log rotation
3. Resource monitoring
4. Encrypted storage
5. Secure cleanup procedures

## Error Handling

- Thread management
- File system errors
- Permission issues
- Resource exhaustion
- System call failures

## Performance Considerations

- CPU usage monitoring
- Memory management
- Disk I/O optimization
- Thread synchronization
- Log file size management

## Advanced Features

1. **Statistical Analysis**

   - Keystrokes per minute
   - Click frequency
   - Activity patterns
   - Session duration

2. **System Monitoring**

   - Resource usage
   - System events
   - Error logging
   - Status reporting

3. **Data Management**
   - Log rotation
   - Data compression
   - Secure storage
   - Clean removal

---

# 5. Image Encryption Tool

## Overview

The Image Encryption Tool provides multiple methods for encrypting and decrypting images using pixel manipulation techniques.

## Features

- XOR encryption
- Pixel shuffling
- Shift cipher
- Multiple encryption methods
- Image preview capability
- Save/load functionality

## Technical Specifications

### Class: ImageEncryption

#### Attributes

- `key`: Encryption key
- `original_image`: Source image
- `encrypted_image`: Processed image

#### Methods

##### `load_image(self, image_path)`

Loads an image file for processing.

**Parameters:**

- `image_path` (str): Path to image file

**Returns:**

- `bool`: Success status

##### `save_image(self, image_array, filename)`

Saves processed image to file.

**Parameters:**

- `image_array` (numpy.ndarray): Image data
- `filename` (str): Output filename

**Returns:**

- `bool`: Success status

##### `generate_key(self)`

Generates random encryption key.

**Returns:**

- `numpy.ndarray`: Random key matching image dimensions

##### `xor_encryption(self, image, key)`

Performs XOR operation between image and key.

**Parameters:**

- `image` (numpy.ndarray): Image data
- `key` (numpy.ndarray): Encryption key

**Returns:**

- `numpy.ndarray`: Processed image

##### `pixel_shuffle(self, image, seed)`

Randomly reorganizes image pixels.

**Parameters:**

- `image` (numpy.ndarray): Image data
- `seed` (int): Random seed value

**Returns:**

- `numpy.ndarray`: Shuffled image

## Encryption Methods

### XOR Encryption

```python
encrypted = image ^ key
decrypted = encrypted ^ key  # Same operation
```

### Pixel Shuffle

```python
# Encryption
indices = np.arange(size)
np.random.shuffle(indices)
shuffled = image.flatten()[indices]

# Decryption
unshuffled = np.zeros_like(flat_image)
unshuffled[indices] = flat_image
```

### Shift Encryption

```python
# Encryption
encrypted = (image + shift) % 256

# Decryption
decrypted = (image - shift) % 256
```

## Usage Example

```python
encryptor = ImageEncryption()

# Load image
encryptor.load_image("input.jpg")

# XOR encryption
key = encryptor.generate_key()
encrypted = encryptor.xor_encryption(image, key)

# Save result
encryptor.save_image(encrypted, "output.png")
```

## Security Considerations

- Key management crucial
- Multiple encryption layers possible
- Not cryptographically secure
- Educational purposes only

## Best Practices

1. Use PNG format for encrypted images
2. Save encryption parameters
3. Test decryption immediately
4. Back up original images
5. Use strong random seeds

## Dependencies

- Python 3.6+
- NumPy
- Pillow (PIL)
- Matplotlib

## Error Handling

- Image format validation
- Memory management
- File I/O error handling
- Invalid parameter detection

## Performance Considerations

- Image size impacts processing time
- Memory usage scales with image dimensions
- Consider batch processing for multiple images

---
