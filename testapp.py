import eel
import fnirs
import time

eel.init('web')
root = fnirs.Fnirs()

@eel.expose
def start():
    while True:
        if root.line:
            if root.line[0] == '-1':
                break
            root.get_avg()
            eel.update_values(root.new, root.change)
        root.next_line()
        time.sleep(0.1)

eel.start('index.html')
