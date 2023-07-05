import eel
import fnir
import time

eel.init('web')

@eel.expose
def start():
    line, nir_file = fnir.open_file()
    while True:
        if line:
            if line[0] == '-1':
                break
            average = fnir.get_avg(line)
            eel.update_values(average)
        line = fnir.next_line(nir_file)

eel.start('index.html')
