import wmi
 
# Initializing the wmi constructor
f = wmi.WMI()

whitelist = ["Code.exe", "svchost.exe", "opera.exe", "Discord.exe", "steamwebhelper.exe", "py.exe", "python.exe", "dllhost.exe", "Agent.exe", "Battle.net.exe", "cmd.exe", "Spotify.exe", "steam.exe"]
# Printing the header for the later columns
print("pid   Process name")
 
# Iterating through all the running processes
for process in f.Win32_Process():

    if process.Name in whitelist:
        continue
     
    # Displaying the P_ID and P_Name of the process
    print(f"{process.ProcessId:<10} {process.Name}")