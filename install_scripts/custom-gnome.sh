#!/usr/bin/env bash

apt-get install gnome-tweak-tool

# arc theme https://github.com/horst3180/Arc-theme
sudo sh -c "echo 'deb http://download.opensuse.org/repositories/home:/Horst3180/xUbuntu_15.04/ /' >> /etc/apt/sources.list.d/arc-theme.list"
wget http://download.opensuse.org/repositories/home:Horst3180/xUbuntu_15.04/Release.key
sudo apt-key add - < Release.key  
sudo apt-get update
sudo apt-get install arc-theme

# paper icons 
sudo add-apt-repository -y ppa:snwh/pulp
sudo apt-get update && sudo apt-get install -y paper-icon-theme