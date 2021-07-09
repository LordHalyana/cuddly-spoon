import wmi
import time
 
# Initializing the wmi constructor
f = wmi.WMI()

localtime = time.asctime(time.localtime(time.time()))

whitelist = ["System", "System Idle Process", "smss.exe", 'notepad.exe', "WWAHost.exe", "sppsvc.exe", "spoolsv.exe", "smartscreen.exe", "csrss.exe", "ctfmon.exe", "lsass.exe", "winlogon.exe", "fontdrvhost.exe", "services.exe", "FastBootService.exe", "MSIRegisterService.exe", "ECO_Service.exe", "MSI_LiveUpdate_Service.exe", "wininit.exe", "Registry", "dwm.exe", "Memory Compression", "DSAService.exe", "PnkBstrA.exe", "SurSvc.exe", "IpOverUsbSvc.exe", "LMS.exe", "lghub_updater.exe", "ServiceLayer.exe", "CueLLAccessService.exe", "MsMpEng.exe", "AdobeUpdateService.exe", "AGSService.exe", "AGMService.exe", "dasHost.exe", "OriginWebHelperService.exe", "WmiPrvSE.exe", "GamingServicesNet.exe", "GamingServices.exe", "NisSrv.exe", "CropAssistService.exe", "DSAUpdateService.exe", "sihost.exe", "taskhostw.exe", "DSATray.exe", "LockApp.exe", "SearchIndexer.exe", "SettingSyncHost.exe", "UserOOBEBroker.exe", "StartMenuExperienceHost.exe", "ShellExperienceHost.exe", "unsecapp.exe", "AdobeNotificationClient.exe", "backgroundTaskHost.exe", "powershell.exe", "nvsphelper64.exe", "ApplicationFrameHost.exe", "SgrmBroker.exe", "XtuService.exe", "ICCProxy.exe", "SecurityHealthService.exe", "twitchstudiostreamdeck.exe", "WinStore.App.exe", "esrv_svc.exe", "isa.exe", "esrv.exe", "TextInputHost.exe", "SystemSettings.exe", "audiodg.exe", "rundll32.exe", "SearchApp.exe", "SearchProtocolHost.exe", "SearchFilterHost.exe", "CodeHelper.exe", "winpty-agent.exe", "jhi_service.exe", "opera_crashreporter.exe", "nordvpn-service.exe", "Corsair.Service.exe", "Corsair.Service.CpuIdRemote64.exe", "Corsair.Service.DisplayAdapter.exe","nvcontainer.exe", "NVDisplay.Container.exe","RuntimeBroker.exe", "QtWebEngineProcess.exe", "explorer.exe","Code.exe", "svchost.exe", "opera.exe", "Discord.exe", "steamwebhelper.exe", "py.exe", "python.exe", "dllhost.exe", "Agent.exe", "Battle.net.exe", "cmd.exe", "Spotify.exe", "steam.exe", "SteamService.exe", "StreamDeck.exe", "", "iCUE.exe", "lghub.exe", "lghub_agent.exe", "Svive Triton TKL connect.exe", "NVIDIA Share.exe", "NVIDIA Web Helper.exe", "Focusrite Notifier.exe", "Taskmgr.exe", "conhost.exe", "IntelSoftwareAssetManagerService.exe"]
blacklist = ["com.barraider.audiometer.exe", "com.barraider.spotify.exe", "LocalBridge.exe", "YourPhone.exe", "FileCoAuth.exe", "Video.UI.exe", "voicemodplugin.exe", "Microsoft.Photos.exe"]

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

    next_scan()

process_killer()