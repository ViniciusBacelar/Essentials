""" 
        Author: Vinicius Bacelar
        Version: 2.0
        GitHub: @ViniciusBacelar
"""


def essentials():

    # import library
    import os

    print("======Start Script======")
   
    # Update your repositories

    def update():
        os.system("sudo apt-get update")

    # Autoremove

    def autoremove():
        os.system("sudo apt autoremove")

    # Upgrade
    def upgrade():
        os.system("sudo apt-get full-upgrade -y")

    # Utilities

    def utilities():
        os.system(
            "sudo apt install unace rar unrar p7zip-rar p7zip sharutils uudeview mpack arj cabextract lzip lunzip plzip")

    # Download Git

    def git():
        os.system("sudo apt-get install git")

    # Download PHP

    def php():
        os.system("sudo apt-get install php")

    # Download Apache2

    def apache2():
        os.system("sudo apt-get install apache2")


    # Install Snap Suport

    def snap():
        os.system("sudo apt install snapd && sudo snap install snap-store")

    # Install Flatpak Suport

    def flatpak():
        os.system("sudo apt install flatpak && sudo apt install gnome-software-plugin-flatpak && flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")

    # Upgrade your programs

    def upgrade():
        os.system("sudo apt-get -y full-upgrade && sudo apt-get -y dist-upgrade")

    # Sublime

    def sublime():
        sublime = str(
            input("Install Sublime-text3? Y/y or N/n? ")).strip().upper()
        if (sublime == "Y") or (sublime == "YES"):
            os.system("sudo snap install sublime-text --classic")
        elif (sublime == "N") or (sublime == "NO"):
            print("OK")
        else:
            print("Incorrect answer")

    # Insomnia

    def insomnia():
        insomnia = str(input("Install Insomnia? Y/y or N/n? ")).strip().upper()
        if (insomnia == "Y") or (insomnia == "YES"):
            os.system("sudo snap install insomnia")
        elif (insomnia == "N") or (insomnia == "NO"):
            print("OK")
        else:
            print("Incorrect answer")

    # Visual Studio Code

    def visual_studio_code():
        visual_studio = str(
            input("Install Visual Studio code? Y/y or N/n? ")).strip().upper()
        if (visual_studio == "Y") or (visual_studio == "YES"):
            os.system("sudo snap install code --classic")
        elif (visual_studio == "N") or (visual_studio == "NO"):
            print("OK")
        else:
            print("Incorrect answer")


    # VLC

    def vlc():
        vlc = str(input("Install VLC? Y/y or N/n? ")).strip().upper()
        if(vlc == "Y") or (vlc == "YES"):
            os.system("sudo apt-get install -y vlc")
        elif(vlc == "N") or (vlc == "NO"):
            print("OK")
        else:
            print("Incorrect answer")

    # qBittorrent

    def bittorrent():
        bittorrent = str(
            input("Install Bittorrent? Y/y or N/n? ")).strip().upper()
        if (bittorrent == "Y") or (bittorrent == "YES"):
            os.system(
                "sudo add-apt-repository ppa:qbittorrent-team/qbittorrent-stable && sudo apt-get install qbittorrent")
        elif(bittorrent == "N") or (bittorrent == "NO"):
            print("OK")
        else:
            print("Incorrect answer")

    # Steam

    def steam():
        steam = str(input("Install Steam? Y/y or N/n? ")).strip().upper()
        if(steam == "Y") or (steam == "YES"):
            os.system("flatpak install flathub com.valvesoftware.Steam")
        elif(steam == "N") or (steam == "NO"):
            print("OK")
        else:
            print("Incorrect answer")

    # Discord

    def discord():
        discord = str(input("Install Discord? Y/y or N/n? ")).strip().upper()
        if(discord == "Y") or (discord == "YES"):
            os.system("flatpak install flathub com.discordapp.Discord")
        elif(discord == "N") or (discord == "NO"):
            print("OK")
        else:
            print("Incorrect answer")

    # Chrome

    def chrome():
        chrome = str(input("Install Chrome? Y/y or N/n? ")).strip().upper()
        if(chrome == "Y") or (chrome == "YES"):
            os.system(
                "wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O chrome.deb")
            os.system("sudo dpkg -i chrome.deb")
            os.system("sudo apt-get install -f")
        elif(chrome == "N") or (chrome == "NO"):
            print("OK")
        else:
            print("Incorrect answer")

    # Docker

    def docker():
        docker = str(input("Install Docker? Y/y or N/n? ")).strip().upper()
        if(docker == "Y") or (docker == "YES"):
            os.system("sudo apt install docker.io")
        elif(docker == "N") or (docker == "NO"):
            print("OK")
        else:
            print("Incorrect answer")

    # Spotify

    def spotify():
        spotify = str(input("Install Spotify? Y/y or N/n? ")).strip().upper()
        if(spotify == "Y") or (spotify == "YES"):
            os.system("snap install spotify")
        elif(spotify == "N") or (spotify == "NO"):
            print("OK")
        else:
            print("Incorrect answer")

    # Link GitHub

    def github():
        os.system('python3 -m webbrowser -t "https://github.com/ViniciusBacelar"')

    # Main function

    def main():
        update()
        upgrade()
        autoremove()
        utilities()
        git()
        snap()
        flatpak()
        php()
        apache2()

    # Function install apps

    def app():
        sublime()
        insomnia()
        visual_studio_code()
        vlc()
        spotify()
        bittorrent()
        docker()
        steam()
        discord()
        chrome()

    # Function final

    def end():
        update()
        upgrade()
        autoremove()
        github()

    # Functions Start
    main()
    app()
    end()

    print("======End Script======")


essentials()
