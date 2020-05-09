""" 
        Author: Vinicius Bacelar
        Version: 1.0.1
        GitHub: @ViniciusBacelar
"""


def essentials():

    # import library
    import os

    print("======Start Script======")
    # Main tools
    # Update your repositories

    def update():
        os.system("sudo apt-get update")

    # Autoremove

    def autoremove():
        os.system("sudo apt autoremove")

    # Essential dependencies

    def dependencies():
        os.system("sudo apt-get install -y build-essential checkinstall && sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev")

    # Utilities

    def utilities():
        os.system(
            "sudo apt install unace rar unrar p7zip-rar p7zip sharutils uudeview mpack arj cabextract lzip lunzip plzip")

    # Propiertes common

    def common():
        os.system("sudo apt-get install software-properties-common")

    # Restricted Extras

    def restricted():
        os.system("sudo apt install ubuntu-restricted-extras")

    # Codecs

    def codecs():
        os.system("sudo apt install libdvd-pkg && sudo dpkg-reconfigure libdvd-pkg")

    # Tweaks

    def tweaks():
        os.system("sudo apt-get install gnome-tweaks")

    # Download Git

    def git():
        os.system("sudo apt-get install git")

    # Download Python

    def python():
        os.system(
            "sudo apt install python3-pip && sudo apt install -y build-essential libssl-dev libffi-dev python3-dev")
        os.system("sudo apt-get install git python3-dev python3-setuptools python3-numpy python3-opengl \
        libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev \
        libsdl1.2-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev \
        libtiff5-dev libx11-6 libx11-dev fluid-soundfont-gm timgm6mb-soundfont \
        xfonts-base xfonts-100dpi xfonts-75dpi xfonts-cyrillic fontconfig fonts-freefont-ttf libfreetype6-dev")
        os.system("sudo apt-get install -y python3-distutils python3-testresources")

    # Download VirtualEnv

    def virtualenv():
        os.system("sudo apt install -y python3-venv")

    # Download Ruby

    def ruby():
        os.system("sudo apt-get install ruby-full")

    # Download PHP

    def php():
        os.system("sudo apt-get install php")

    # Download Apache2

    def apache2():
        os.system("sudo apt-get install apache2")

    # Download MySql

    def mysql():
        os.system("sudo apt-get install mysql-server && mysql_secure_installation")

    # Download node

    def node():
        os.system("""curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
        sudo apt-get install -y nodejs && sudo apt-get install -y nodejs""")

    # Install Yarn

    def yarn():
        os.system("""curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
        echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
        sudo apt-get update && sudo apt-get install yarn""")

    # Install Snap Suport

    def snap():
        os.system("sudo apt install snapd && sudo snap install snap-store")

    # Install Make

    def make():
        os.system("sudo apt-get install make")

    # Install Flatpak Suport

    def flatpak():
        os.system("sudo apt install flatpak && sudo apt install gnome-software-plugin-flatpak && flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")

    # Upgrade your programs

    def upgrade():
        os.system("sudo apt-get -y full-upgrade && sudo apt-get -y dist-upgrade")

    # Install Apps

    def transport_https():
        os.system("sudo apt-get install apt-transport-https")

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

    # WPS

    def wps():
        wps = str(input("Install WPS? Y/y or N/n? ")).strip().upper()
        if(wps == "Y") or (wps == "YES"):
            os.system("flatpak install flathub com.wps.Office")
        elif(wps == "N") or (wps == "NO"):
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

    # Android Studio

    def android():
        android_studio = str(
            input("Install Android Studio? Y/y or N/n? ")).strip().upper()
        if (android_studio == "Y") or (android_studio == "YES"):
            os.system("sudo snap install android-studio --classic")
        elif (android_studio == "N") or (android_studio == "NO"):
            print("OK")
        else:
            print("Incorrect answer")

    # Webstorm

    def webstorm():
        webstorm = str(input("Install PhpStorm? Y/y or N/n? ")).strip().upper()
        if (webstorm == "Y") or (webstorm == "YES"):
            os.system("sudo snap install webstorm --classic")
        elif(webstorm == "N") or (webstorm == "NO"):
            print("OK")
        else:
            print("Incorrect answer")

    # CodeBlocks

    def codeblocks():
        codeblocks = str(
            input("Install CodeBlocks? Y/y or N/n? ")).strip().upper()
        if (codeblocks == "Y") or (codeblocks == "YES"):
            os.system("sudo apt-get install codeblocks")
        elif(codeblocks == "N") or (codeblocks == "NO"):
            print("OK")
        else:
            print("Incorrect answer")

    # RubyMine

    def rubymine():
        ruby = str(input("Install RubyMine? Y/y or N/n? ")).strip().upper()
        if(ruby == "Y") or (ruby == "YES"):
            os.system("sudo snap install rubymine --classic")
        elif(ruby == "N") or (ruby == "NO"):
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

    # PhpMyAdmin

    def myadmin():
        php = str(input("Install PhpMyAdmin? Y/y or N/n? ")).strip().upper()
        if(php == "Y") or (php == "YES"):
            os.system("sudo apt-get install phpmyadmin")
        elif(php == "N") or (php == "NO"):
            print("OK")
        else:
            print("Incorrect Answer")

    # Filezilla

    def filezilla():
        filezilla = str(
            input("Install Filezilla? Y/y or N/n? ")).strip().upper()
        if (filezilla == "y") or (filezilla == "Y") or (filezilla == "yes"):
            os.system("flatpak install flathub org.filezillaproject.Filezilla")
        elif(filezilla == "N") or (filezilla == "NO"):
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

    # VirtuaBox

    def virtualbox():
        virtualbox = str(
            input("Install VirtualBox? Y/y or N/n?")).strip().upper()
        if(virtualbox == "Y") or (virtualbox == "YES"):
            os.system("sudo apt-get install virtualbox")
        elif(virtualbox == "N") or (virtualbox == "NO"):
            print("OK")
        else:
            print("Incorrect answer")

    # PyCharm

    def pycharm():
        pycharm = str(input("Install PyCharm CE? Y/y or N/n? ")
                      ).strip().upper()
        if(pycharm == "Y") or (pycharm == "YES"):
            os.system("sudo snap install pycharm-community --classic")
        elif(pycharm == "N") or (pycharm == "NO"):
            print("OK")
        else:
            print("incorrect answer")

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
        common()
        dependencies()
        restricted()
        transport_https()
        codecs()
        tweaks()
        git()
        make()
        snap()
        flatpak()
        python()
        virtualenv()
        ruby()
        php()
        apache2()
        mysql()
        node()
        yarn()

    # Function install apps

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
        virtualbox()
        docker()
        myadmin()
        filezilla()
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
