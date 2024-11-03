## Install as admin
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
wsl.exe --install
wsl --set-default-version 2

## To run
ubuntu

## Update
sudo apt update && apt upgrade -y

