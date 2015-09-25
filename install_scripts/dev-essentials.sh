#!/usr/bin/env bash

# dirs
mkdir -p $HOME/Workspaces

apt-get install -y vim
apt-get install -y curl

# git
apt-get install -y git
git config --global user.name "Jafnee"
git config --global user.email Jafnee@users.noreply.github.com

# zsh
apt-get install -y zsh
sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
chsh -s /usr/bin/zsh