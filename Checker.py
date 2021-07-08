import wmi
 
# Initializing the wmi constructor
f = wmi.WMI()

whitelist = ["opera_crashreporter.exe","System", "System Idle Process", "Registry", "powershell.exe", "nordvpn-service.exe", "Corsair.Service.exe", "Corsair.Service.CpuIdRemote64.exe", "Corsair.Service.DisplayAdapter.exe","nvcontainer.exe", "NVDisplay.Container.exe","RuntimeBroker.exe", "QtWebEngineProcess.exe", "explorer.exe","Code.exe", "svchost.exe", "opera.exe", "Discord.exe", "steamwebhelper.exe", "py.exe", "python.exe", "dllhost.exe", "Agent.exe", "Battle.net.exe", "cmd.exe", "Spotify.exe", "steam.exe", "SteamService.exe", "StreamDeck.exe", "", "iCUE.exe", "lghub.exe", "lghub_agent.exe", "Svive Triton TKL connect.exe", "NVIDIA Share.exe", "NVIDIA Web Helper.exe", "Focusrite Notifier.exe", "Taskmgr.exe", "conhost.exe", "IntelSoftwareAssetManagerService.exe"]
blacklist = ["com.barraider.audiometer.exe", "com.barraider.spotify.exe"]

# Printing the header for the later columns
print("pid   Process name")
 
# Iterating through all the running processes
for process in f.Win32_Process():

    #if process is whitelisted it will not print.
    if process.Name in whitelist:
        continue

    if process.Name in blacklist:
        #Placeholder print for blacklist until i fix
        print(" ##### Blacklisted Program Below. will Kill process later. Placeholder space  ####")
     
    # Displaying the P_ID and P_Name of the process
    print(f"{process.ProcessId:<10} {process.Name}")