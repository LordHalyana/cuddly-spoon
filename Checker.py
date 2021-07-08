import wmi
import time
 
# Initializing the wmi constructor
f = wmi.WMI()

localtime = time.asctime(time.localtime(time.time()))

whitelist = ["System", "System Idle Process", "smss.exe", "csrss.exe", "lsass.exe", 'notepad.exe', "winlogon.exe", "fontdrvhost.exe", "services.exe", "wininit.exe", "Registry", "dwm.exe", "Memory Compression", "DSAService.exe", "PnkBstrA.exe", "SurSvc.exe", "IpOverUsbSvc.exe", "LMS.exe", "lghub_updater.exe", "ServiceLayer.exe", "CueLLAccessService.exe", "MsMpEng.exe", "AdobeUpdateService.exe", "AGSService.exe", "AGMService.exe", "dasHost.exe", "OriginWebHelperService.exe", "WmiPrvSE.exe", "GamingServicesNet.exe", "GamingServices.exe", "NisSrv.exe", "CropAssistService.exe", "DSAUpdateService.exe", "sihost.exe", "taskhostw.exe", "DSATray.exe", "LockApp.exe", "SearchIndexer.exe", "SettingSyncHost.exe", "UserOOBEBroker.exe", "StartMenuExperienceHost.exe", "ShellExperienceHost.exe", "unsecapp.exe", "AdobeNotificationClient.exe", "backgroundTaskHost.exe", "powershell.exe", "nvsphelper64.exe", "ApplicationFrameHost.exe", "SgrmBroker.exe", "XtuService.exe", "ICCProxy.exe", "SecurityHealthService.exe", "twitchstudiostreamdeck.exe", "WinStore.App.exe", "esrv_svc.exe", "isa.exe", "esrv.exe", "TextInputHost.exe", "SystemSettings.exe", "audiodg.exe", "rundll32.exe", "SearchApp.exe", "SearchProtocolHost.exe", "SearchFilterHost.exe", "CodeHelper.exe", "winpty-agent.exe", "jhi_service.exe", "opera_crashreporter.exe", "nordvpn-service.exe", "Corsair.Service.exe", "Corsair.Service.CpuIdRemote64.exe", "Corsair.Service.DisplayAdapter.exe","nvcontainer.exe", "NVDisplay.Container.exe","RuntimeBroker.exe", "QtWebEngineProcess.exe", "explorer.exe","Code.exe", "svchost.exe", "opera.exe", "Discord.exe", "steamwebhelper.exe", "py.exe", "python.exe", "dllhost.exe", "Agent.exe", "Battle.net.exe", "cmd.exe", "Spotify.exe", "steam.exe", "SteamService.exe", "StreamDeck.exe", "", "iCUE.exe", "lghub.exe", "lghub_agent.exe", "Svive Triton TKL connect.exe", "NVIDIA Share.exe", "NVIDIA Web Helper.exe", "Focusrite Notifier.exe", "Taskmgr.exe", "conhost.exe", "IntelSoftwareAssetManagerService.exe"]
blacklist = ["com.barraider.audiometer.exe", "com.barraider.spotify.exe", "YourPhone.exe", "spoolsv.exe", "FileCoAuth.exe", "Video.UI.exe", "voicemodplugin.exe", "Microsoft.Photos.exe", "ctfmon.exe", "FastBootService.exe", "MSIRegisterService.exe", "ECO_Service.exe", "MSI_LiveUpdate_Service.exe"]

# Printing the header for the later columns
print("pid   Process name")
 
# Iterating through all the running processes
for process in f.Win32_Process():

    #if process is whitelisted it will not print.
    if process.Name in whitelist:
        continue

    if process.Name in blacklist:
        #Placeholder print for blacklist until i fix
        print(localtime +"        ##### Blacklisted Program  KILLING: " + process.Name)
        process.Terminate()
        continue
     
    # Displaying the P_ID and P_Name of the process and path
    print(f"{process.ProcessId:<10} {process.Name}        {localtime}        {process.ExecutablePath}")
