[Setup]
AppName=H.A.R.I.S.
AppVersion=1.0
DefaultDirName={pf}\H.A.R.I.S
DefaultGroupName=H.A.R.I.S.
OutputDir=Output
OutputBaseFilename=H.A.R.I.S.Setup
SetupIconFile=h-icon.ico
Compression=lzma
SolidCompression=yes

[Files]
Source: "app\H.A.R.I.S.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\H.A.R.I.S."; Filename: "{app}\H.A.R.I.S.exe"; WorkingDir: "{app}"
Name: "{commondesktop}\H.A.R.I.S."; Filename: "{app}\H.A.R.I.S.exe"; Tasks: desktopicon; WorkingDir: "{app}"

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"

[Run]
Filename: "{app}\H.A.R.I.S.exe"; Description: "Launch H.A.R.I.S."; Flags: nowait postinstall skipifsilent