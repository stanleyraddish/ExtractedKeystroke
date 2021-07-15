from pynput.keyboard import Listener, Key
import time

start = time.time()
pwd = "hatyellow"
pwdLen = len(pwd)
pressIndex = 0 # expected pwd index of next key press
timeStack = []
keyStack = []
stackSize = 0

#-----Data Record Options--------------
write = False
fileName = "worddata4.txt" # File to write to
outputString = "T: 0 0 0 1 0;"
#-----Data Record Options--------------

def on_press(key):
    global pwd, pressIndex, timeStack, keyStack, stackSize
#     print("press", pwd[pressIndex], " curr:", key.char)
    if hasattr(key, "char") and key.char == pwd[pressIndex]:
        timeStack.append(time.time())
        keyStack.append(key.char)
        pressIndex += 1
        stackSize += 1
    else:
        print("\nYou mispelled the password!")
        print(f"Please type the password: {pwd}")
        pressIndex = 0
        timeStack = []
        keyStack = []
        stackSize = 0

def on_release(key):
    global pwd, pressIndex, timeStack, keyStack, stackSize, pwdLen
    if pressIndex != 0:
#     print("release", " curr:", key.char)
        timeStack.append(time.time())
        keyStack.append(key.char)
        stackSize += 1
        if stackSize == 2 * pwdLen:
            return False

def writeData(times, keys, pwdLen):
    intervals = [0] * (pwdLen * 2 - 1) # First pwdLen elements will be intervals between press and release for each key
                                       # Last pwdLen elements will be intervals between last release and next press
    assert(len(times) == len(keys) and len(keys) == 2 * pwdLen)
    scaletime = 10 # multiplies time (1000 multiplier converts to milliseconds)
    tmpkeys = keys.copy()
    lastReleaseTime = 0
    latestPressIndex = -1
    for i in range(pwdLen):
        char = tmpkeys[0]
        tmpkeys.remove(char) # remove both press and release copies from temp list
        tmpkeys.remove(char)
        pressI = keys.index(char, latestPressIndex + 1) # get array index of key press
        releaseI = keys.index(char, pressI + 1) # get array index of key release
        intervals[i] = round((times[releaseI] - times[pressI]) * scaletime, 2)
        if i != 0:
            intervals[i + pwdLen - 1] = round((times[pressI] - lastReleaseTime) * scaletime, 2)
        lastReleaseTime = times[releaseI]
        latestPressIndex = pressI
    print("Time data:", intervals)
    global fileName, write
    if write:
        writetoFile(fileName, intervals)
    assert(tmpkeys == [])

def writetoFile(fname, times):
    global outputString
    f = open(fname, "a")
    l1 = "I:"
    l2 = outputString
    for i in range(len(times)):
        l1 += f" {times[i]}"
    l1 += "\n"
    f.write(l1)
    f.write(l2 + "\n\n")
    f.close()
    print(len(open(fname).readlines()) / 3)
    
    
while True:
#     print(pressIndex, releaseIndex)
    if stackSize == 2 * pwdLen and pressIndex == pwdLen:
        print([round(timeStack[i] - start, 2) for i in range(2*pwdLen)])
        print(keyStack)
        writeData(timeStack, keyStack, pwdLen)
        pressIndex = 0
        timeStack = []
        keyStack = []
        stackSize = 0
    print(f"\nPlease type the password: {pwd}")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


