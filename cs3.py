from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        # Print the pressed key to the terminal
        print(f"Key pressed: {key}")
    except Exception as e:
        print(f"Error: {str(e)}")

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Start listening to keystrokes
print("Keylogger started. Press 'esc' to stop.")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()