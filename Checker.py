import wmi
import time
import json
 
# Initializing the wmi constructor
f = wmi.WMI()

localtime = time.asctime(time.localtime(time.time()))

whitelist = []
blacklist = []


#Opens blacklist.json and puts data into blacklist
with open('Settings/blacklist.json') as json_file:
    data = json.load(json_file)
    for p in data:
        blacklist.append(p)

#Opens whitelist.json and puts data into Whitelist
with open('Settings/whitelist.json') as json_file:
    data = json.load(json_file)
    for p in data:
        whitelist.append(p)

#Saves blacklist to json
with open('Settings/blacklist.json', 'w') as outfile:
    json.dump(blacklist, outfile)

#Saves whitelist to json
with open('Settings/whitelist.json', 'w') as outfile:
    json.dump(whitelist, outfile)

def process_killer():

    def next_scan():
        print('Next Scan in 60 sec')
        time.sleep(60)

        check_processes()

    def check_processes():

        print('Checking Processes')

        # Printing the header for the later columns
        print("TIME                           pid            Process name                 path")

        # Iterating through all the running processes
        for process in f.Win32_Process():

            #if process is whitelisted it will not print.
            if process.Name in whitelist:
                continue

            #if process name is in blacklist it will terminate it
            if process.Name in blacklist:
                print(f" {localtime}        {process.ProcessId:<10} {process.Name}        {process.ExecutablePath}" + "                   ######APPLICATION IS IN BLACKLIST AND HAVE BEEN TERMINATED")
                process.Terminate()
                continue

            # Displaying the P_ID and P_Name of the process and path
            print(f" {localtime}        {process.ProcessId:<10} {process.Name}        {process.ExecutablePath}")

        next_scan()

    check_processes()

process_killer()