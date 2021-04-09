# Setting up Environments

Once you've installed Python successfully on your system, you can start using it with **[virtual environments](https://docs.python.org/3/tutorial/venv.html)**.<br>Using virtual environments is an ideal way of running and executing Python. Running Python this way doesn't affect the "**default**" modules (*builtin python apps* in layman term).

**Note:** We'll address "**virtual environment**" as **venv** in short.

## On Linux and Mac

### Installation

- Open up Terminal and install virtual environment packages and type:
  ```bash
  pip3 install virtualenv virtualenvwrapper --no-warn-script-location
  ```
  <p align="center">
    <img src="https://github.com/xames3/cheat_sheet/blob/assets/media/pip-install-venv.png?raw=true">
  </p>
- Once the installation is complete, type `nano ~/.bashrc`. This will open in your `.bashrc` file in **[Nano](https://github.com/xames3/cheat_sheet/blob/master/editors/nano.md)**.
- Go to the end of the file and add below lines:
  ```bash
  # To setup virtual environments:
  export WORKON_HOME=$HOME/environments
  export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
  export VIRTUALENVWRAPPER_VIRTUALENV=$HOME/.local/bin/virtualenv
  source $HOME/.local/bin/virtualenvwrapper.sh
  ```
  <p align="center">
    <img src="https://github.com/xames3/cheat_sheet/blob/assets/media/setup-venv.png?raw=true">
  </p>

This will setup and install all your virtual environments in `~/environments/` directory. In case you want to change the path of the venvs, update `export WORKON_HOME` in the above lines.

And done!

### Usage

- Open up Terminal and type `mkvirtualenv <YOUR VENV NAME>`. This creates a blank virtual environment. I'm creating venv called as "**env**", so I'll type "**mkvirtualenv env**".
  <p align="center">
    <img src="https://github.com/xames3/cheat_sheet/blob/assets/media/mk-venv.png?raw=true">
  </p>
- Once the virtual environment is created, use it by typing `workon <YOUR VENV NAME>`, in my case "**workon env**".
  <p align="center">
    <img src="https://github.com/xames3/cheat_sheet/blob/assets/media/venv-venv.png?raw=true">
  </p>

## On Windows

### Installation

- Open up CMD or PS and install virtual environment package and type:
  ```bash
  pip3 install virtualenv
  ```
  <p align="center">
    <img src="https://github.com/xames3/cheat_sheet/blob/assets/media/win-pip-install-venv.PNG?raw=true">
  </p>

### Usage

- Open up CMD or PS and type `virtualenv <YOUR VENV NAME>`. This creates a blank virtual environment. I'm creating venv called as "**venv**", so I'll type "**virtualenv venv**".<br><br>
  <p align="center">
    <img src="https://github.com/xames3/cheat_sheet/blob/assets/media/win-setup-venv.PNG?raw=true">
  </p><br>
- Once the virtual environment is created, use it by typing `<YOUR VENV NAME>\Scripts\activate` and **Enter**.<br><br>
  <p align="center">
    <img src="https://github.com/xames3/cheat_sheet/blob/assets/media/win-venv-venv.PNG?raw=true">
  </p>

In order to get out of the virtual environment, type `deactivate` this deactivates the venv.
