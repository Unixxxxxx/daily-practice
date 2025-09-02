import keyboard 
print("Press ESC to stop.....")
while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        print(f"Key {event.name} pressed")
    if event.name == 'esc':
        print("Exiting.....")
        break
