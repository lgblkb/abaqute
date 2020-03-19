from __future__ import absolute_import
import os
import sys
# run_script(r'main.py')
print sys.executable
from abaqute import settings



# python_packages_path=os.path.join(settings.get_parent(sys.executable,2),'Lib','site-packages')
# print python_packages_path

abaqus_environment={'SYSTEMROOT':'C:\\Windows','ABQLMHANGLIMIT':'0','VIRTUAL_ENV':'C:\\Users\\lgblkb\\virtualenvs\\abaqute',
                    'FED_DSLS_LICENSE_CONFIG':'C:\\ProgramData\\DassaultSystemes\\Licenses\\DSLicSrv.txt',
                    'ABAQUS_LANG':'English_United States.1252',
                    'COMSPEC':'C:\\Windows\\system32\\cmd.exe','ANSYS_SYSDIR':'winx64',
                    'PYTHONPATH':'C:\\SIMULIA\\CAE\\2019;C:\\SIMULIA\\CAE\\2019\\win_b64;C:\\SIMULIA\\CAE\\2019\\win_b64\\code;C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\bin;C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\bin\\SMAExternal;C:\\SIMULIA\\CAE\\2019\\win_b64\\CAEresources;C:\\SIMULIA\\CAE\\2019\\win_b64\\SMA;C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\python2.7\\lib;C:\\SIMULIA\\CAE\\2019\\win_b64\\tools\\SMApy\\python2.7\\lib;C:\\SIMULIA\\CAE\\2019\\win_b64\\tools\\SMApy\\python2.7\\lib\\lib-tk;C:\\SIMULIA\\CAE\\2019\\win_b64\\tools\\SMApy\\python2.7\\lib\\site-packages;C:\\SIMULIA\\CAE\\2019\\win_b64\\tools\\SMApy\\python2.7\\DLLs;.;C:\\SIMULIA\\CAE\\2019;C:\\SIMULIA\\CAE\\2019\\win_b64;C:\\SIMULIA\\CAE\\2019\\win_b64\\code;C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\bin;C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\bin\\SMAExternal;C:\\SIMULIA\\CAE\\2019\\win_b64\\CAEresources;C:\\SIMULIA\\CAE\\2019\\win_b64\\SMA;C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\python2.7\\lib;C:\\SIMULIA\\CAE\\2019\\win_b64\\tools\\SMApy\\python2.7\\lib;C:\\SIMULIA\\CAE\\2019\\win_b64\\tools\\SMApy\\python2.7\\lib\\lib-tk;C:\\SIMULIA\\CAE\\2019\\win_b64\\tools\\SMApy\\python2.7\\lib\\site-packages;C:\\SIMULIA\\CAE\\2019\\win_b64\\tools\\SMApy\\python2.7\\DLLs;.;C:\\Users\\lgblkb\\PycharmProjects\\abaqute',
                    'SOLVER_PATH_BASE':'C:\\Program Files\\Dassault Systemes\\SimulationServices\\V6R2019x\\win_b64',
                    'ABAQUS_DISABLE_FPE':'ON',
                    'ABQ_DLALLOCATOR':'1','ABAQUS_PY_TRANSLATION_DICTIONARY':'Configuration/Xresources/en_US/en_US_PyDict.py',
                    'HOMEDRIVE':'C:',
                    'SYSTEMDRIVE':'C:','PYCHARM_HOSTED':'1','CUSTOMWORKSPACE':'',
                    'P_SCHEMA':'C:\\Program Files\\ANSYS Inc\\ANSYS Student\\v194\\AISOL\\CADIntegration\\Parasolid\\PSchema',
                    'CATCOMMANDPATH':'C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\command','LSTC_LICENSE':'ANSYS','OS':'Windows_NT',
                    'ABAQUS_MESSAGE_SERVER':'','ABAQUSLM_LICENSE_FILE':'27800@localhost',
                    'CATDICTIONARYPATH':'C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\dictionary',
                    'ABAQUS_SEQ':'2018_09_25-00.41.51 157541',
                    'PYTHONUNBUFFERED':'1',
                    'ABA_BLA_LIBRARY_PATH':'C:\\SIMULIA\\CAE\\2019;C:\\SIMULIA\\CAE\\2019\\win_b64;C:\\SIMULIA\\CAE\\2019\\win_b64\\code;C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\bin;C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\bin\\SMAExternal;C:\\SIMULIA\\CAE\\2019\\win_b64\\CAEresources;C:\\SIMULIA\\CAE\\2019\\win_b64\\SMA;C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\bin\\SMAExternal\\Interop;C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\bin\\SMAExternal\\Elysium',
                    'ABA_PATH_BASE':'C:\\SIMULIA\\CAE\\2019\\win_b64;','PYVERDIRNAME':'python2.7',
                    'TEMP':'C:\\Users\\lgblkb\\AppData\\Local\\Temp',
                    'COMMONPROGRAMFILES(X86)':'C:\\Program Files (x86)\\Common Files','ABQ_IGNORE_FPE':'0',
                    'ABAQUS_MESSAGING_MECHANISM':'DIRECT',
                    'HOMEPATH':'\\Users\\lgblkb','PROCESSOR_LEVEL':'6','ABQLMIMPL':'FLEXNET',
                    'DRIVERDATA':'C:\\Windows\\System32\\Drivers\\DriverData','LOGONSERVER':'\\\\DESKTOP-MGC46N5',
                    'LOCALAPPDATA':'C:\\Users\\lgblkb\\AppData\\Local','ABA_HOME':'C:\\SIMULIA\\CAE\\2019\\win_b64',
                    'APPDATA':'C:\\Users\\lgblkb\\AppData\\Roaming',
                    'ABA_PATH':'C:\\SIMULIA\\CAE\\2019;C:\\SIMULIA\\CAE\\2019\\win_b64;C:\\SIMULIA\\CAE\\2019\\win_b64\\code;C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\bin;C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\bin\\SMAExternal;C:\\SIMULIA\\CAE\\2019\\win_b64\\CAEresources;C:\\SIMULIA\\CAE\\2019\\win_b64\\SMA',
                    'CATDEFAULTENVIRONMENT':'Env','_OLD_VIRTUAL_PROMPT':'$P$G','TMP':'C:\\Users\\lgblkb\\AppData\\Local\\Temp',
                    'ABA_LIBRARY_PATHNAME':'PATH','COMPUTERNAME':'DESKTOP-MGC46N5',
                    '_OLD_VIRTUAL_PATH':'C:\\SIMULIA\\Commands;C:\\Program Files\\Microsoft MPI\\Bin\\;C:\\Program Files (x86)\\Intel\\iCLS Client\\;C:\\Program Files\\Intel\\iCLS Client\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\CMake\\bin;C:\\Users\\lgblkb\\AppData\\Local\\Programs\\Python\\Python37-32\\Scripts\\;C:\\Users\\lgblkb\\AppData\\Local\\Programs\\Python\\Python37-32\\;C:\\Users\\lgblkb\\AppData\\Local\\Microsoft\\WindowsApps;',
                    'ABQLMQUEUE':'30','USERDOMAIN':'DESKTOP-MGC46N5',
                    'SMASVT_ROOT_PATH':'C:\\SIMULIA\\CAE\\2019;C:\\SIMULIA\\CAE\\2019\\win_b64;C:\\SIMULIA\\CAE\\2019\\win_b64\\code;C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\bin;C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\bin\\SMAExternal;C:\\SIMULIA\\CAE\\2019\\win_b64\\CAEresources;C:\\SIMULIA\\CAE\\2019\\win_b64\\SMA',
                    'ABA_MPI_LIBRARY_PATH':'C:\\SIMULIA\\CAE\\2019;C:\\SIMULIA\\CAE\\2019\\win_b64;C:\\SIMULIA\\CAE\\2019\\win_b64\\code;C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\bin;C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\bin\\SMAExternal;C:\\SIMULIA\\CAE\\2019\\win_b64\\CAEresources;C:\\SIMULIA\\CAE\\2019\\win_b64\\SMA;C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\bin\\SMAExternal\\Interop;C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\bin\\SMAExternal\\Elysium',
                    'COMMONPROGRAMFILES':'C:\\Program Files\\Common Files','ABA_COMMAND':'abq2019.bat','DISPLAY':':0.0',
                    'ANS_OLD_ATTACH':'1',
                    'ABAQUS_SUPPORTED_LOCALE':'en_US','PROCESSOR_ARCHITECTURE':'AMD64',
                    'ANSYS194_DIR':'C:\\Program Files\\ANSYS Inc\\ANSYS Student\\v194\\ANSYS','ALLUSERSPROFILE':'C:\\ProgramData',
                    'USERDOMAIN_ROAMINGPROFILE':'DESKTOP-MGC46N5','PROGRAMW6432':'C:\\Program Files','USERNAME':'lgblkb',
                    'PROMPT':'(abaqute) $P$G',
                    'ONEDRIVE':'C:\\Users\\lgblkb\\OneDrive','PLUGIN_CENTRAL_DIR':'C:\\SIMULIA\\CAE\\plugins\\2019',
                    'IDEA_INITIAL_DIRECTORY':'C:\\Program Files\\JetBrains\\PyCharm 2019.2.1\\bin',
                    'PATHEXT':'.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC','WINDIR':'C:\\Windows',
                    'NUMBER_OF_PROCESSORS':'8',
                    'TOSCA_INSTALL_PATH':'C:\\SIMULIA\\Tosca\\2019\\win_b64\\code\\command\\ToscaStructure.bat',
                    'PUBLIC':'C:\\Users\\Public',
                    'USERPROFILE':'C:\\Users\\lgblkb','PYTHONIOENCODING':'UTF-8',
                    'PSMODULEPATH':'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules',
                    'AWP_ROOT194':'C:\\Program Files\\ANSYS Inc\\ANSYS Student\\v194',
                    'PROCESSOR_IDENTIFIER':'Intel64 Family 6 Model 158 Stepping 9, GenuineIntel',
                    'PROGRAMFILES':'C:\\Program Files',
                    'PROCESSOR_REVISION':'9e09',
                    'PATH':'C:\\SIMULIA\\CAE\\2019\\win_b64\\tools\\SMApy\\python2.7\\lib\\site-packages\\pywin32_system32;C:\\SIMULIA\\CAE\\2019;C:\\SIMULIA\\CAE\\2019\\win_b64;C:\\SIMULIA\\CAE\\2019\\win_b64\\code;C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\bin;C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\bin\\SMAExternal;C:\\SIMULIA\\CAE\\2019\\win_b64\\CAEresources;C:\\SIMULIA\\CAE\\2019\\win_b64\\SMA;C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\bin\\SMAExternal\\Interop;C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\bin\\SMAExternal\\Elysium;C:\\Users\\lgblkb\\virtualenvs\\abaqute\\Scripts;C:\\SIMULIA\\Commands;C:\\Program Files\\Microsoft MPI\\Bin\\;C:\\Program Files (x86)\\Intel\\iCLS Client\\;C:\\Program Files\\Intel\\iCLS Client\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\CMake\\bin;C:\\Users\\lgblkb\\AppData\\Local\\Programs\\Python\\Python37-32\\Scripts\\;C:\\Users\\lgblkb\\AppData\\Local\\Programs\\Python\\Python37-32\\;C:\\Users\\lgblkb\\AppData\\Local\\Microsoft\\WindowsApps',
                    'FED_LICENSE_SERVER_TYPE':'DSFLEX',
                    'ABQ_LC_ALL':'LC_COLLATE=en;LC_CTYPE=English_United States.1252;LC_MONETARY=en;LC_NUMERIC=C;LC_TIME=en',
                    'PROGRAMFILES(X86)':'C:\\Program Files (x86)','MSMPI_BIN':'C:\\Program Files\\Microsoft MPI\\Bin\\',
                    'SESSIONNAME':'Console',
                    'ABAQUS_DISABLE_MONITORING':'','PROGRAMDATA':'C:\\ProgramData',
                    '_NT_SYMBOL_PATH':'C:\\SIMULIA\\CAE\\2019;C:\\SIMULIA\\CAE\\2019\\win_b64;C:\\SIMULIA\\CAE\\2019\\win_b64\\code;C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\bin;C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\bin\\SMAExternal;C:\\SIMULIA\\CAE\\2019\\win_b64\\CAEresources;C:\\SIMULIA\\CAE\\2019\\win_b64\\SMA;C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\bin\\SMAExternal\\Interop;C:\\SIMULIA\\CAE\\2019\\win_b64\\code\\bin\\SMAExternal\\Elysium',
                    'CADOE_LIBDIR194':'C:\\Program Files\\ANSYS Inc\\ANSYS Student\\v194\\CommonFiles\\Language\\en-us',
                    'ABQLMUSER':'lgblkb',
                    'DSY_TENANT':'OnPremise','ABAQUS_TRANSLATION_DICTIONARY':'Configuration/Xresources/en_US/en_US_Dict.py',
                    'ABA_COMMAND_FULL':'C:\\SIMULIA\\Commands\\abq2019.bat',
                    'COMMONPROGRAMW6432':'C:\\Program Files\\Common Files',
                    'FED_DSFLEX_LICENSE_CONFIG':'27800@localhost'}

# for k,v in environment.items():
# 	print k
