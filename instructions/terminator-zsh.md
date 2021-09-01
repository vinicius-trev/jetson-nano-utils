# Terminator - ZSH - Oh my ZSH

- How to Install
```
sudo apt install terminator
sudo update-alternatives --config x-terminal-emulator # Choose the /usr/bin/terminator

sudo apt install zsh
sh -c "$(wget --no-check-certificate https://raw.githubusercontent.com/robbyrussel/oh-my-zsh/master/tools/install.sh -O -)"
git clone https://github.com/zsh-users/zsh-autosuggestions.git $ZSH_CUSTOM/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
sed -i 's/plugins=(git)/plugins=(git zsh-autosuggestions zsh-syntax-highlighting)/g' ~/.zshrc
```

Source: https://gist.github.com/dogrocker/1efb8fd9427779c827058f873b94df95
