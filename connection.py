# ONLY FOR ESP32 - WROOM32 microcontroller
# DON NOT USE IT FOR RASPBERRY PI 4

import network
import time
from data import wifi

class Connection:
    def __init__(self, ssid="", password=""):
        self.network = network.WLAN(network.STA_IF)
        self.networkList = []
        self.ssid = ssid
        self.password = password

    def scan(self):
        if not self.network.active():
            self.network.active(True)
        print("Scanning for available networks...")
        self.networkList = self.network.scan()

    def getNetworkList(self):
        return self.networkList

    def injectData(self):
        self.ssid = wifi["ssid"]
        self.password = wifi["password"]

    def connect(self, timeOut=10):
        if timeOut <= 0:
            timeOut = 5

        if self.network.isconnected():
            print(f"Already connected to {self.ssid}")
            return True
        
        if not self.network.active():
            self.network.active(True)

        print(f"Connecting to {self.ssid}...")
        self.network.connect(self.ssid, self.password)

        times = 0
        sleepTime = 1
        while times < timeOut:
            if self.network.isconnected():
                print(f"Successfully connected to {self.ssid}")
                return True
            else:
                print(f"Attempt {times + 1}/{timeOut}: Retrying in {sleepTime} second(s)...")
                time.sleep(sleepTime)
                sleepTime = min(sleepTime * 2, 10)
                times += 1

        print(f"Failed to connect to {self.ssid} within {timeOut} seconds.")
        return False

    def disconnect(self):
        if self.network.isconnected():
            print(f"Disconnecting from {self.ssid}...")
            self.network.disconnect()
            time.sleep(3)
        self.network.active(False)
        print("WiFi disabled.")

