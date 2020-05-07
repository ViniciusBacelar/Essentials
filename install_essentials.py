import os
print("Start script")
# Main tools
# Update your repositories
def update(): os.system("sudo apt-get update")

# Autoremove
def autoremove(): os.system("sudo apt autoremove")

# Propiertes common
def common(): os.system("sudo apt-get install software-properties-common")

# Restricted Extras
def restricted(): os.system("sudo apt install ubuntu-restricted-extras")

# Codecs
def codecs(): os.system("sudo apt install libdvd-pkg && sudo dpkg-reconfigure libdvd-pkg")

# Tweaks
def tweaks(): os.system("sudo apt-get install gnome-tweaks")

# Download git
def git(): os.system("sudo apt-get install git")

# Download Ruby
def ruby(): os.system("sudo apt-get install ruby-full")

# Download PHP
def php(): os.system("sudo apt-get install php")

# Download Apache2
def apache2(): os.system("sudo apt-get install apache2")

# Download MySql
def mysql(): os.system("sudo apt-get install mysql-server && mysql_secure_installation")

# Download node
def node(): os.system("""curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs""")

# Install Yarn
def yarn(): os.system("""curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt-get update && sudo apt-get install yarn""")

# Install Snap Suport
def snap(): os.system("sudo apt install snapd && sudo snap install snap-store")

# Install Flatpak Suport
def flatpak(): os.system("sudo apt install flatpak && sudo apt install gnome-software-plugin-flatpak && flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")

# Upgrade your programs
def upgrade(): os.system("sudo apt-get -y full-upgrade && sudo apt-get -y dist-upgrade")

# Install Apps
def transport_https(): os.system("sudo apt-get install apt-transport-https")

# Sublime
def sublime():
    sublime = str(input("Download Sublime-text3? Y/y or N/n? "))
    if (sublime == "y") or (sublime == "Y") or (sublime == "yes"):
        os.system("sudo snap install sublime-text --classic")
    elif (sublime == "n") or (sublime == "N") or (sublime == "no"):
        print("OK")
    else:
        print("Incorrect answer")

# WPS
def wps():
    wps = str(input("Download WPS? Y/y or N/n? "))
    if(wps == "y") or (wps == "Y") or (wps == "yes"):
        os.system("flatpak install flathub com.wps.Office")
    elif(wps == "n") or (wps == "N") or (wps == "no"):
        print("OK")
    else:
        print("Incorrect answer")

# Insomnia
def insomnia():
    insomnia = str(input("Download Insomnia? Y/y or N/n? "))
    if (insomnia == "y") or (insomnia == "Y") or (insomnia == "yes"):
        os.system("sudo snap install insomnia")
    elif (insomnia == "n") or (insomnia == "N") or (insomnia == "no"):
        print("OK")
    else:
        print("Incorrect answer")

# Visual Studio Code
def visual_studio_code():
    visual_studio = str(input("Download Visual Studio code? Y/y or N/n? "))
    if (visual_studio == "y") or (visual_studio == "Y") or (visual_studio == "yes"):
        os.system("sudo snap install code --classic")
    elif (visual_studio == "n") or (visual_studio == "N") or (visual_studio == "no"):
        print("OK")
    else:
        print("Incorrect answer")

# Android Studio
def android():
    android_studio = str(input("Download Android Studio? Y/y or N/n? "))
    if (android_studio == "y") or (android_studio == "Y") or (android_studio == "yes"):
        os.system("sudo snap install android-studio --classic")
    elif (android_studio == "n") or (android_studio == "N") or (android_studio == "no"):
        print("OK")
    else:
        print("Incorrect answer")

# Webstorm
def webstorm():
    webstorm = str(input("Download PhpStorm? Y/y or N/n? "))
    if (webstorm == "y") or (webstorm == "Y") or (webstorm == "yes"):
        os.system("sudo snap install webstorm --classic")
    elif(webstorm == "n") or (webstorm == "N") or (webstorm == "no"):
        print("OK")
    else:
        print("Incorrect answer")

# CodeBlocks
def codeblocks():
    codeblocks = str(input("Download CodeBlocks? Y/y or N/n? "))
    if (codeblocks == "Y") or (codeblocks == "y") or (codeblocks == "yes"):
        os.system("sudo apt-get install codeblocks")
    elif(codeblocks == "N") or (codeblocks == "n") or (codeblocks == "no"):
        print("OK")
    else:
        print("Incorrect answer")

# RubyMine
def rubymine():
    ruby = str(input("Download RubyMine? Y/y or N/n? "))
    if(ruby == "y") or (ruby == "Y") or (ruby == "yes"):
        os.system("sudo snap install rubymine --classic")
    elif(ruby == "n") or (ruby == "N") or (ruby == "no"):
        print("OK")
    else:
        print("Incorrect answer")

# VLC
def vlc():
    vlc = str(input("Download VLC? Y/y or N/n? "))
    if (vlc == "y") or (vlc == "Y") or (vlc == "yes"):
        os.system("sudo apt-get install -y vlc")
    elif(vlc == "n") or (vlc == "N") or (vlc == "no"):
        print("OK")
    else:
        print("Incorrect answer")

# qBittorrent
def bittorrent():
    bittorrent = str(input("Download Bittorrent? Y/y or N/n? "))
    if (bittorrent == "y") or (bittorrent == "Y") or (bittorrent == "yes"):
        os.system(
            "sudo add-apt-repository ppa:qbittorrent-team/qbittorrent-stable && sudo apt-get install qbittorrent")
    elif (bittorrent == "n") or (bittorrent == "N") or (bittorrent == "no"):
        print("OK")
    else:
        print("Incorrect answer")

# PhpMyAdmin
def myadmin():
    php = str(input("Download PhpMyAdmin? Y/y or N/n? "))
    if(php == "y") or (php == "Y") or (php == "yes"):
        os.system("sudo apt-get install phpmyadmin")
    elif(php == "n") or (php == "N") or (php == "no"):
        print("OK")
    else:
        print("Incorrect Answer")

# Filezilla
def filezilla():
    filezilla = str(input("Download Filezilla? Y/y or N/n? "))
    if (filezilla == "y") or (filezilla == "Y") or (filezilla == "yes"):
        os.system("flatpak install flathub org.filezillaproject.Filezilla")
    elif(filezilla == "n") or (filezilla == "N") or (filezilla == "no"):
        print("OK")
    else:
        print("Incorrect answer")

# Steam
def steam():
    steam = str(input("Download Steam? Y/y or N/n? "))
    if (steam == "y") or (steam == "Y") or (steam == "yes"):
        os.system("flatpak install flathub com.valvesoftware.Steam")
    elif (steam == "n") or (steam == "N") or (steam == "no"):
        print("OK")
    else:
        print("Incorrect answer")

# Discord
def discord():
    discord = str(input("Download Discord? Y/y or N/n? "))
    if (discord == "y") or (discord == "Y") or (discord == "yes"):
        os.system("flatpak install flathub com.discordapp.Discord")
    elif(discord == "n") or (discord == "N") or (discord == "no"):
        print("OK")
    else:
        print("Incorrect answer")

# Chrome
def chrome():
    chrome = str(input("Download Chrome? Y/y or N/n? "))
    if (chrome == "y") or (chrome == "Y") or (chrome == "yes"):
        os.system(
            "wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O chrome.deb")
        os.system("sudo dpkg -i chrome.deb")
        os.system("sudo apt-get install -f")
    elif(chrome == "n") or (chrome == "N") or (chrome == "no"):
        print("OK")
    else:
        print("Incorrect answer")

# Docker
def docker():
    docker = str(input("Download Docker? Y/y or N/n? "))
    if(docker == "y") or (docker == "Y") or (docker == "yes"):
        os.system("sudo apt install docker.io")
    elif(docker == "n") or (docker == "N") or (docker == "no"):
        print("OK")
    else:
        print("Incorrect answer")

#PyCharm
def pycharm():
    pycharm = str(input("Download PyCharm CE? Y/y or N/n? "))
    if (pycharm == "y") or (pycharm == "Y") or (pycharm == "yes"):
        os.system("sudo snap install pycharm-community --classic")
    elif(pycharm == "n") or (pycharm == "N") or (pycharm == "no"):
        print("OK")
    else: 
        print("incorrect answer")

#Spotify
def spotify():
    spotify = str(input("Download Spotify? Y/y or N/n? "))
    if(spotify == "y") or (spotify == "Y") or (spotify == "yes"):
        os.system("snap install spotify")
    elif(spotify == "n") or (spotify == "N") or (spotify == "no"):
        print("OK")
    else:
        print("Incorrect answer")

def main():
    update()
    upgrade()
    autoremove()
    common()
    restricted()
    transport_https()
    codecs()
    tweaks()
    git()
    snap()
    flatpak()
    ruby()
    php()
    apache2()
    mysql()
    node()
    yarn()
    
def app():
    sublime()
    wps()
    insomnia()
    visual_studio_code()
    android()
    webstorm()
    pycharm()
    codeblocks()
    rubymine()
    vlc()
    spotify()
    bittorrent()
    docker()
    myadmin()
    filezilla()
    steam()
    discord()
    chrome()
    
def end():
    update()
    upgrade()
    autoremove()
    
# Functions Start
main()
app()
end()
print("End script")
