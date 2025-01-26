# Prerequisites

## Install the IDE (Integrated Development Environment)

It's recommended to use [VS Code](https://code.visualstudio.com/) or feel free to use any other IDEs that you are comfortable with.

### VS Code Installation Guide

#### Windows Installation
1. Visit https://code.visualstudio.com/
2. Download Windows installer
3. Run installer
4. Follow installation wizard:
   - Accept license agreement
   - Choose installation location
   - Select additional tasks
5. Complete installation

#### Mac Installation
1. Visit https://code.visualstudio.com/
2. Download macOS version
3. Open downloaded .zip
4. Drag VS Code to Applications folder
5. First launch:
   - Right-click VS Code
   - Select "Open"
   - Confirm application launch

#### Linux Installation
##### Ubuntu/Debian
```bash
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt update
sudo apt install code
```

##### Fedora/Red Hat
```bash
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
sudo dnf install code
```

#### Post-Installation
- Launch VS Code
- Install extensions
- Configure settings

## Git and GitHub

### Git Installation Guide

Git is our one of the main tool to use in this bootcamp and the future

#### Windows
1. Download installer from https://git-scm.com/download/win
2. Run installer
3. Choose installation options:
   - Select components
   - Choose default editor
   - Adjust PATH environment
4. Complete installation
5. Verify by running `git --version` in command prompt

#### macOS
##### Method 1: Homebrew
```bash
brew install git
```

##### Method 2: Official Installer
1. Download from https://git-scm.com/download/mac
2. Run .dmg package
3. Follow installation wizard

#### Linux
##### Ubuntu/Debian
```bash
sudo apt update
sudo apt install git
```

##### Fedora
```bash
sudo dnf install git
```

##### CentOS/RHEL
```bash
sudo yum install git
```

#### Post-Installation Configuration
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

#### Verify Installation
```bash
git --version
```

#### References

##### Git

- Learn more about Git by watching this [tutorials](https://www.youtube.com/watch?v=8JJ101D3knE&t=2s)


[![Watch the video](https://img.youtube.com/vi/8JJ101D3knE/hqdefault.jpg)](https://www.youtube.com/watch?v=8JJ101D3knE&t=2s)

##### GitHub

- [Git and GitHub Tutorial for Beginners](https://www.youtube.com/watch?v=tRZGeaHPoaw) 

[![Watch the video](https://img.youtube.com/vi/tRZGeaHPoaw/hqdefault.jpg)](https://www.youtube.com/watch?v=tRZGeaHPoaw)