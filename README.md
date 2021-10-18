# Inupdater

------------------------------------------------------------------------

[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://pypi.org/project/isort/)
[![test](https://github.com/yoannmos/Inupdater/actions/workflows/ci.yml/badge.svg)](https://github.com/yoannmos/Inupdater)
[![codecov](https://codecov.io/gh/yoannmos/Inupdater/branch/master/graph/badge.svg?token=CV7RJU2RWM)](https://codecov.io/gh/yoannmos/Inupdater)

------------------------------------------------------------------------

[Read Latest Documentation](https://yoannmos.github.io/Inupdater/) - [Browse GitHub Code Repository](https://github.com/yoannmos/Inupdater/)

------------------------------------------------------------------------

## Descriprion

This is an auto-updater for your software.

You can provide a new version of your exe in a location of your choice and user will be auto-updated when launching your app.

<!-- Check the [appexemple](https://github.com/yoannmos/Inupdater-Appexemple) repository for recomended implementation. -->

## Use

Download *launcher.exe* and add it to your dist folder.

To work, the launcher.exe should be installed in the same repo of your .exe

![Typical install Folder](docs\images\folder.PNG)

You need a settings.json with the following content in the same folder.

```txt
{
    "exe_name": "appexemple", // exe name without version
    "dist_location": "dist/", // location folder of yours dist (a dist should look like : appexemple_1.0.2 = *exe_name*_*version*)
    "version": "0.0.1" // Version auto updated, (You can keep 0.0.1 to force update in first launch)
}
```

Only version will be updated exe_name and dist location will not be updated.

### Innosetup

#### with standard program launching

To launch your program simply call the launcher instead of your program.
In InnoSetup you define your ***AppExeName*** to *launcher.exe* instead of *yourapp.exe*.

```pascal
#define AppExeName "launcher"
```

#### with registry key launching

For exemple to add a right click shortcut in background add those line to your .iss file.  

```pascal
[Files]
Source: "dist\launcher.exe"; DestDir: "{app}"; DestName: "launcher.exe"
Source: "dist\settings.json"; DestDir: "{app}"; DestName: "settings.json"
Source: "dist\appexemple.exe"; DestDir: "{app}"; DestName: "appexemple.exe"

[Registry]
Root: HKCR; Subkey: "Directory\Background\shell\{#AppName}"; ValueType: string; ValueName: ""; ValueData: "&Appexemple"; Flags: uninsdeletekey
Root: HKCR; Subkey: "Directory\Background\shell\{#AppName}\command"; ValueType: string; ValueName: ""; ValueData: "{app}\launcher.exe"; Flags: uninsdeletekey
```

## Test on an exemple

You can check the exemple repo ([Inupdater-AppExemple](https://github.com/yoannmos/Inupdater-AppExemple)) for a simple implementation of Inupdater.
