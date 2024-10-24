# ONLY FOR ESP32 WROOM-32 microcontroller
# DONT USE IT FOR RASPBERRY PI 4

import network, os, gc, sys

def getDeviceInfo():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    ssid = wlan.config('essid') if wlan.isconnected() else "Not connected"
    
    memFree = gc.mem_free() / (1024**2)
    memAlloc = gc.mem_alloc() / (1024**2)
    memTotal = memFree + memAlloc
    
    fsStat = os.statvfs('/')
    storageTotal = (fsStat[0] * fsStat[2]) / (1024**2)
    storageFree = (fsStat[0] * fsStat[3]) / (1024**2)
    
    return {
        "SSID": ssid,
        "RAM": f"{round(memAlloc, 2)} / {round(memTotal, 2)} MB",
        "Storage": f"{round(storageTotal - storageFree, 2)} / {round(storageTotal, 2)} MB",
        "CPU Hz": sys.platform
    }

def printInfo():
    for k, v in getDeviceInfo().items():
        print(f"{k}: {v}")
    del k, v