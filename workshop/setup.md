# Setup

There are a few things you need to get working on your machine in order to easily follow this workshop. However, don't worry as it's all gonna be [open source](https://en.wikipedia.org/wiki/Open_source), won't require a lot of storage and will be explained in detail.

While same parts and section will be do-able via `cloud computing`, which is nice and easy to follow in an interactive manner, it's not recommended as getting `Python` & friends to work reliably on your machine is going to be very beneficial. This holds true for the course and especially beyond. Via installing these tools, you will be equipped to basically continue right away and start using them in your everyday research workflow. This even applies if you won't continue with `python` (We certainly hope you do.) and instead work with `R` (of course also cool), `matlab` (weeeeeeeell...) or what have you.  Having that in mind and integrating other tools/resources focusing open and reproducible science, you will find a rather comprehensive set of install instructions below. While not all of them might be totally necessary for the workshop, they all will help you a great deal going further and are especially useful/needed if we have to hold the workshop virtually.

Don't worry, you got this!

![logo](https://media1.tenor.com/images/f72cb542d6b3e3c3421889e0a3d9628d/tenor.gif?itemid=4533805)\
<sub><sup><sub><sup>https://media1.tenor.com/images/f72cb542d6b3e3c3421889e0a3d9628d/tenor.gif?itemid=4533805</sup></sub></sup></sub>


## General things

There are a few computing requirements for the course that are absolutely necessary (beyond the few software packages you should install, described below):

1. You must have administrator access to your computer (i.e., you must be able to install things yourself without requesting IT approval).
2. You must have at least 20 GB of free disk space on your computer (but we would recommend more, to be safe).
3. If you are using Windows you must be at least using Windows 10; Windows 7 and 8 will not be sufficient for this course.

If you foresee any of these being a problem please reach out to one of the instructors for what steps you can take to ensure you are ready for the workshop start.

## Required software

To get the most out of the course, we ask that you arrive with the following software already installed:

- A command-line shell: `Bash`
- A version control system: [Git](https://git-scm.com/) 
- A remote-capable text editor: [VSCode](https://code.visualstudio.com/)
- `Python 3` via `Miniconda`
- A [github.com](https://github.com/) account with an [SSH key connection](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
- A `modern browser` (e.g. [Chrome](https://www.google.com/chrome/index.html), or [Firefox](https://www.mozilla.org/en-CA/firefox/new/))

If you already have all of the above software tools/packages installed, or are confident you’ll be able to install them by the time the course starts, you can jump straight to [checking your install](#checking-your-install).
The rest of this page provides more detail on installation procedures for each of the above elements, with separate instructions for each of the three major operating systems (`Windows`, `Mac OS`, and `Linux`).

### Some quick general notes on instructions

- There is no difference between `Enter` and `Return` in these instructions, so just press whatever the equivalent on your keyboard is whenever one is stated
- If you already have some of these things installed on your computer already that should (theoretically) be okay.
  However, you need to make sure that you are able to complete the steps described in [checking your install](#checking-your-install) without issue.
  - For example, having multiple different `Python` installations on your computer can lead to incredibly frustrating issues that are very difficult to debug.
    As such, if you have already installed `Python` via some other application (not `Miniconda`/`Anaconda`), it's strongly encouraged to uninstall it before following the instructions below.
    You _must_ have `Python` installed via `Miniconda` for this course.

### OS-specific installation instructions

Select the tab that corresponds to your operating system and follow the instructions therein.

````{tab-set}
```{tab-item} Windows
**Windows Subsystem for Linux (WSL)**

NB: The instructors unfortunately didn't have access to a `windows OS` and thus couldn't test the installation instructions directly. Therefore, chances are respective users might run into a few hiccups here and there. If that's the case, please just let us know and we will try our best to solve it.

1. Search for `Windows Powershell` in your applications; right click and select `Run as administrator`.
   Select `Yes` on the prompt that appears asking if you want to allow the app to make changes to your device.
2. Type the following into the Powershell and then press `Enter`:

        Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux

3. Press `Enter` again when prompted to reboot your computer.
4. Once your computer has rebooted, open the Microsoft Store and search for "Ubuntu."
   Install the program labelled "Ubuntu 22.04" (not "Ubuntu 16.04" or "Ubuntu") by clicking the tile, pressing `Get`, and then `Install`.
5. Search for and open Ubuntu from your applications.
   There will be a slight delay (of a few minutes) while it finishes installing.
6. You will be prompted to `Enter new UNIX username`.
   You can use any combination of alphanumeric characters here for your username, but a good choice is `<first_initial><last_name>` (e.g., `jsmith` for John Smith).
   You will then be prompted to enter a new password.
   (Choose something easy to remember as you will find yourself using it frequently.)
7. Right click on the top bar of the Ubuntu application and select "Properties".
   Under the "Options" tab, under the "Edit Options" heading, make sure the box reading "Use Ctrl+Shift+C/V as Copy/Paste" is checked.
   Under the "Terminal" tab, under the "Cursor Shape" heading, make sure the box reading "Vertical Bar" is checked.
   Press "Okay" to save these settings and then exit the application.

(The above step-by-step WSL instructions are distilled from [here](https://docs.microsoft.com/en-us/windows/wsl/install-win10) and [here](https://docs.microsoft.com/en-us/windows/wsl/initialize-distro).
If you have questions during the installation procedure those resources may have answers!)

From this point on whenever the instructions specify to "open a terminal" please assume you are supposed to open the Ubuntu application.

**Bash shell**

You already have it, now that you’ve installed the WSL!

**Git**

You already have it, now that you’ve installed the WSL!

**VSCode**

1. Go to https://code.visualstudio.com/ and click the download button, then run the `.exe` file.
1. Leave all the defaults during the installation with the following exception:
      - Please make sure the box labelled "Register Code as an editor for supported file types" is selected

**VSCode extensions**

1. Open the Ubuntu application.
1. Type `code .` into the terminal and press `Enter`.
   You should see a message reading "Installing VS Code Server" and then a new windows will open up.
1. Press `Ctrl+Shift+P` in the new window that opens and type "Extensions: Install extensions" into the search bar that appears at the top of the screen.
   Select the appropriate entry from the dropdown menu that appears (there should be four entries; simply select the one that reads "Extensions: Install extensions").
1. A new panel should appear on the left-hand side of the screen with a search bar.
   Search for each of the following extensions and press `Install` for the first entry that appears. (The author listed for all of these extensions should be "Microsoft".)
      - Python (n.b., you will need to reload VSCode after installing this)


**Python**

1. Open a new terminal and type the following lines (separately) into the terminal, pressing `Enter` after each one:

        wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
        bash Miniconda3-latest-Linux-x86_64.sh

1. A license agreement will be displayed and the bottom of the terminal will read `--More--`.
   Press `Enter` or the space bar until you are prompted with "Do you accept the license terms? [yes|no]."
   Type `yes` and then press `Enter`
1. The installation script will inform you that it is going to install into a default directory (e.g., `/home/$USER/miniconda3`).
   Leave this default and press `Enter`.
1. When you are asked "Do you wish the installer to initialize Miniconda3 by running conda init? [yes|no]," type `yes` and press `Enter`.
   Exit the terminal once the installation has finished.
1. Re-open the Ubuntu application.
   Type `which python` into the terminal and it should return a path (e.g., `/home/$USER/miniconda3/bin/python`).
   - If you do not see a path like this then please try typing `conda init`, closing your terminal, and repeating this step.
     If your issue is still not resolved skip the following step and contact an instructor on the #help-installation channel on the BHS Slack.
1. Type the following to remove the installation script that was downloaded:

        rm ./Miniconda3-latest-Linux-x86_64.sh


**Python packages**

Open a terminal and type the following commands:

        conda config --append channels conda-forge
        conda config --set channel_priority strict


**Git configuration**

After installing Git, please run these commands one after another in your terminal (it doesn’t matter in which directory you currently are) to check and complete your setup (you can just copy-paste the commands):

`git --version`

→ this tells you if the installation was successful by telling you the version number of git you installed.

`git config --global user.name "Example Name"`

→ put in your real name. You have to set the quotation marks around your name otherwise git can’t read it.

`git config --global user.email example@example.com`

→ choose your preferred email.

`git config --global init.defaultBranch main`

→ this makes sure that your default branch is main, which is currently used by most users as their default branch. Don’t worry about what it means, we will talk about that in the workshop ☺

`git config --global core.editor ExampleEditor`

→ this sets a default text editor when working with git. Just type in the editor you want to use. My recommendation is to use nano or vim. You don’t have to download anything, it’s already on your machine as it is a command-line editor. So, it’s super convenient for working with git, as
the git commands are also run in the command-line. It simply means that when writing commit messages you can do it in one window (i.e., your terminal) and you don't have to bother with a new window opening and making sure it's really closed etc. But of course, you can use any text editor you want. Just as an example, for making nano your gloab git-editor
type `git config --global core.editor nano`. 

`git config --global pull.rebase false`

`git config --global pull.merge true`

→ this makes sure that your merges are shown in the commit history which is nice if you just start learning to use Git. When you're more experienced, git rebase is also a very nice command (we'll learn about that in the course!).

`cat ~/.gitconfig`

→ checks if your configuration was successful. It should give you this output:


      [user] name = Your Name email = yourname@yourplace.org
      [core] editor = YourEditor
      [init] defaultBranch = main
      [pull] rebase = false merge = true
```

```{tab-item} Linux
**Bash shell**

You already have it!
Depending on which version of Linux you’re running you may need to type `bash` inside the terminal to access it.
To check whether this is necessary, follow these steps:

1. Open a terminal and type `echo $SHELL`.
   If it reads `/bin/bash` then you are all set!
   If not, whenever the instructions read "open a terminal," please assume you are to open a terminal, type `bash`, and the proceed with the instructions as specified.

**Git**

You may already have it; try typing `sudo apt-get install git` (Ubuntu, Debian) or `sudo yum install git` (Fedora) inside the terminal.
If you are prompted to install it follow the instructions on-screen to do so.

**VSCode**

1. Go to https://code.visualstudio.com/ and click the download button for either the .deb (Ubuntu, Debian) or the .rpm (Fedora, CentOS) file.
1. Double-click the downloaded file to install VSCode.
   (You may be prompted to type your administrator password during the install).

**VSCode extensions**

1. Open the Visual Studio Code application.
1. Press `Ctrl+Shift+P` in the new window that opens and type "Extensions: Install extensions" into the search bar that appears at the top of the screen.
   Select the appropriate entry from the dropdown menu that appears (there should be four entries; simply select the one that reads "Extensions: Install extensions").
1. A new panel should appear on the left-hand side of the screen with a search bar.
   Search for each of the following extensions and press `Install` for the first entry that appears. (The author listed for all of these extensions should be "Microsoft".)
      - Python (n.b., you will need to reload VSCode after installing this)

**Python**

1. Open a new terminal and type the following lines (separately) into the terminal, pressing `Enter` after each one:

        wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
        bash Miniconda3-latest-Linux-x86_64.sh


1. A license agreement will be displayed and the bottom of the terminal will read `--More--`.
   Press `Enter` or the space bar until you are prompted with "Do you accept the license terms? [yes|no]."
   Type `yes` and then press `Enter`
1. The installation script will inform you that it is going to install into a default directory (e.g., `/home/$USER/miniconda3`).
   Leave this default and press `Enter`.
1. When you are asked "Do you wish the installer to initialize Miniconda3 by running conda init? [yes|no]," type `yes` and press `Enter`.
   Exit the terminal once the installation has finished.
1. Re-open a new terminal.
   Type `which python` into the terminal and it should return a path (e.g., `/home/$USER/miniconda3/bin/python`).
   - If you do not see a path like this then please try typing `conda init`, closing your terminal, and repeating this step.
     If your issue is still not resolved skip the following step and contact an instructor on the #help-installation channel of the BHS Slack.
1. Type the following to remove the installation script that was downloaded:

        rm ./Miniconda3-latest-Linux-x86_64.sh

**Python packages**

Open a terminal and type the following commands:

        conda config --append channels conda-forge
        conda config --set channel_priority strict

**Git configuration**

After installing Git, please run these commands one after another in your terminal (it doesn’t matter in which directory you currently are) to check and complete your setup (you can just copy-paste the commands):

`git --version`

→ this tells you if the installation was successful by telling you the version number of git you installed.

`git config --global user.name "Example Name"`

→ put in your real name. You have to set the quotation marks around your name otherwise git can’t read it.

`git config --global user.email example@example.com`

→ choose your preferred email.

`git config --global init.defaultBranch main`

→ this makes sure that your default branch is main, which is currently used by most users as their default branch. Don’t worry about what it means, we will talk about that in the workshop ☺

`git config --global core.editor ExampleEditor`

→ this sets a default text editor when working with git. Just type in the editor you want to use. My recommendation is to use nano or vim. You don’t have to download anything, it’s already on your machine as it is a command-line editor. So, it’s super convenient for working with git, as
the git commands are also run in the command-line. It simply means that when writing commit messages you can do it in one window (i.e., your terminal) and you don't have to bother with a new window opening and making sure it's really closed etc. But of course, you can use any text editor you want. Just as an example, for making nano your gloab git-editor
type `git config --global core.editor nano`. 

`git config --global pull.rebase false`

`git config --global pull.merge true`

→ this makes sure that your merges are shown in the commit history which is nice if you just start learning to use Git. When you're more experienced, git rebase is also a very nice command (we'll learn about that in the course!).

`cat ~/.gitconfig`

→ checks if your configuration was successful. It should give you this output:


      [user] name = Your Name email = yourname@yourplace.org
      [core] editor = YourEditor
      [init] defaultBranch = main
      [pull] rebase = false merge = true
```

```{tab-item} MacOs
**Bash shell**

You already have it!
Depending on which version of Mac OS you’re running you may need to type `bash` inside the terminal to access it.
To check whether this is necessary, follow these steps:

1. Open a terminal and type `echo $SHELL`.
   If it reads `/bin/bash` then you are all set!

**Note:** If you are using Mac Catalina (10.15.X) then it is possible your default shell is NOT CORRECT.
To set the default to bash, type `chsh -s /bin/bash` in the terminal, enter your password when prompted, and then close + re-open the terminal.

**Another note:** Every time the instructions say *"close terminal and open a new one"* you have to make sure that your terminal is **REALLY CLOSED**. If you press the *x* in the terminal app, your terminal window disappears but it is very likely it is still running in the background (a feature known in MacOS). Go to the terminal icon in your dock and *quit* the app with a right click on the app icon. 

**And a last note:** When downloading apps from the internet and not from the app store, you might get a complaint saying that the app is "not from a verified developer" and will not be able to install it. Don't worry, of course everything we ask you to install is verified and not harmful. To be able to install the software anyway, you need to do a *right click on the app package* and then click *open with installation program*. Then you will see an extra button saying "open anyway" which you need to press. And there you go...

**Git**

You may already have it!
Try opening a terminal and typing `git --version`.
If you do not see something like “git version X.XX.X” printed out, then follow these steps: 

1. Follow [this link](https://sourceforge.net/projects/git-osx-installer/files/git-2.23.0-intel-universal-mavericks.dmg/download?use_mirror=autoselect) to automatically download an installer.
1. Double click the downloaded file (`git-2.23.0-intel-universal-mavericks.dmg`) and then double click the `git-2.23.0-intel-universal-mavericks.pkg` icon inside the dmg that is opened.
1. Follow the on-screen instructions to install the package.

**VSCode**

1. Go to https://code.visualstudio.com/ and click the download button.
1. Unzip the downloaded file (e.g., `VSCode-darwin-stable.zip`) and moving the resulting `Visual Studio Code` file to your Applications directory.

**VSCode extensions**

1. Open the Visual Studio Code application
1. Type `Cmd+Shift+P` and then enter "Shell command: Install 'code' command in PATH" into the search bar that appears at the top of the screen.
   Select the highlighted entry.
   A notification box should appear in the bottom-right corner indicating that the command was installed successfully.
1. Type `Cmd+Shift+P` again and then enter "Extensions: Install extensions" into the search bar.
   Select the appropriate entry from the dropdown menu that appears (there should be four entries; simply select the one that reads "Extensions: Install extensions").
1. A new panel should appear on the left-hand side of the screen with a search bar.
   Search for each of the following extensions and press `Install` for the first entry that appears. (The author listed for all of these extensions should be "Microsoft".)
      - Python (n.b., you will need to reload VSCode after installing this)


**Python**

1. Open a new terminal and type the following lines (separately) into the terminal, pressing `Enter` after each one:

        curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
        bash Miniconda3-latest-MacOSX-x86_64.sh


1. A license agreement will be displayed and the bottom of the terminal will read `--More--`.
   Press `Enter` or the space bar until you are prompted with "Do you accept the license terms? [yes|no]."
   Type `yes` and then press `Enter`
1. The installation script will inform you that it is going to install into a default directory (e.g., `/home/$USER/miniconda3`).
   Leave this default and press `Enter`.
1. When you are asked "Do you wish the installer to initialize Miniconda3 by running conda init? [yes|no]," type `yes` and press `Enter`.
   Exit the terminal once the installation has finished.
1. Re-open a terminal.
   Type `which python` into the terminal and it should return a path (e.g., `/home/$USER/miniconda3/bin/python`).
   - If you do not see a path like this then please try typing `conda init`, closing your terminal, and repeating this step.
     If your issue is still not resolved skip the following step and contact an instructor on the #help-installation channel of the BHS Slack.
1. Type the following to remove the installation script that was downloaded:

        rm ./Miniconda3-latest-MacOSX-x86_64.sh


**Python packages**

Open a terminal and type the following commands:

        conda config --append channels conda-forge
        conda config --set channel_priority strict


**Git configuration**

After installing Git, please run these commands one after another in your terminal (it doesn’t matter in which directory you currently are) to check and complete your setup (you can just copy-paste the commands):

`git --version`

→ this tells you if the installation was successful by telling you the version number of git you installed.

`git config --global user.name "Example Name"`

→ put in your real name. You have to set the quotation marks around your name otherwise git can’t read it.

`git config --global user.email example@example.com`

→ choose your preferred email.

`git config --global init.defaultBranch main`

→ this makes sure that your default branch is main, which is currently used by most users as their default branch. Don’t worry about what it means, we will talk about that in the workshop ☺

`git config --global core.editor ExampleEditor`

→ this sets a default text editor when working with git. Just type in the editor you want to use. My recommendation is to use nano or vim. You don’t have to download anything, it’s already on your machine as it is a command-line editor. So, it’s super convenient for working with git, as
the git commands are also run in the command-line. It simply means that when writing commit messages you can do it in one window (i.e., your terminal) and you don't have to bother with a new window opening and making sure it's really closed etc. But of course, you can use any text editor you want. Just as an example, for making nano your gloab git-editor
type `git config --global core.editor nano`. 

`git config --global pull.rebase false`

`git config --global pull.merge true`

→ this makes sure that your merges are shown in the commit history which is nice if you just start learning to use Git. When you're more experienced, git rebase is also a very nice command (we'll learn about that in the course!).

`cat ~/.gitconfig`

→ checks if your configuration was successful. It should give you this output:


      [user] name = Your Name email = yourname@yourplace.org
      [core] editor = YourEditor
      [init] defaultBranch = main
      [pull] rebase = false merge = true

Please run the two following commands so that the .DS_Store files are always ignored by Git. You don’t need it ever and it just makes troubles.

`echo .DS_Store >> ~/.gitignore_global`

`git config --global core.excludesfile ~/.gitignore_global`
```
````

### Modern web browser

Please install [Chrome](https://www.google.com/chrome/index.html) or [Firefox](https://www.mozilla.org/en-CA/firefox/new/).
(Safari might also work.)
Microsoft Edge is not modern, despite what Microsoft might try and otherwise tell you.

Yeah, you did! Great job!

![logo](https://media1.tenor.com/images/d5ebabf248130ec3842ed3b8627fd4f2/tenor.gif?itemid=4770158)\
<sub><sup><sub><sup>https://media1.tenor.com/images/d5ebabf248130ec3842ed3b8627fd4f2/tenor.gif?itemid=4770158</sup></sub></sup></sub>

## Getting the course content

Now that you have installed the required software (or not) to follow the course, it's time to gather the respective materials.


<img src="https://upload.wikimedia.org/wikipedia/commons/e/ea/Conda_logo.svg" alt="conda logo" width="300"/>\
<sub><sup><sub><sup>https://upload.wikimedia.org/wikipedia/commons/e/ea/Conda_logo.svg</sup></sub></sup></sub>

By installing `Python` on your system (i.e. specifically `Conda`) and setting up the appropriate environment, you will be able to open all the `Jupyter Notebooks` and go through the whole content of the course locally. 

To get things up and running, please follow these steps:

NB: The instructions are written for unix-based OS, e.g. `linux` and `macOS`. Please remember to update the paths for `windows OS` respectively, ie `\` instead of `/` and so on.

There are two options to set up the computational environment and get the course content. Please try the first option, ie `environment.yml` first and only if it does not work for you, try the second option, ie `requirements.txt`.

````{tab-set}
```{tab-item} Option 1 - environment.yml

1. Create a directory dedicated only for work before and during the school, e.g. `Desktop/Clean_Repro_Code_Neuromatch`. 
2. Download the materials in this repository via [this link](https://github.com/peerherholz/Clean_Repro_Code_Neuromatch/-/archive/main/Clean_Repro_Code_Neuromatch-main.zip?path=school/materials) and unzip them to directory you just created, e.g. `Desktop/Clean_Repro_Code_Neuromatch`.
3. Download the [`environment.yml`](https://github.com/peerherholz/Clean_Repro_Code_Neuromatch/-/raw/main/environment.yml?ref_type=heads) file (e.g. with right mouse click -> Save As) and also save it in the directory you just created . Make sure that the file ends with `.yml` and not `.txt`.
4. Open up a `conda terminal`,   `WSL` (or any other `terminal`), and create a new `conda environment` with the following command: `conda env create -f /path/to/file/environment.yml` - For example `conda env create -f ~/Desktop/environment.yml`
5. Next, open up a `conda terminal` (or any other `terminal`), activate the `conda environment` with `conda activate Clean_Repro_Code_Neuromatch` (or on older `conda environment managers` with `source activate Clean_Repro_Code_Neuromatch` for `mac` and `linux` and `activate Clean_Repro_Code_Neuromatch` for `windows`).
6. Finally, via the `terminal`, move to the folder where you've put all the unzipped content of this workshop, e.g. with the command `cd ~/Desktop/Clean_Repro_Code_Neuromatch` and run the command `jupyter notebook`. If the `notebook server` isn't automatically opened in a new browser window, please copy-paste either the `http://127.0.0.1:8888/...` or the `http://localhost:8888/...` path into a new browser window and press `Enter`. You should now see the `jupyter notebook server` (looking like a file browser and displaying the content of the directory). 
```

```{tab-item} Option 2 - requirements.txt
1. Create a directory dedicated only for work before and during the school, e.g. `Desktop/Clean_Repro_Code_Neuromatch`. 
2. Download the materials in this repository via [this link](https://github.com/peerherholz/Clean_Repro_Code_Neuromatch/-/archive/main/Clean_Repro_Code_Neuromatch-main.zip?path=school/materials) and unzip them to directory you just created, e.g. `Desktop/Clean_Repro_Code_Neuromatch`.
3. Download the [`requirements.txt`](https://github.com/peerherholz/Clean_Repro_Code_Neuromatch/-/blob/main/requirements.txt?ref_type=heads) file (e.g. with right mouse click -> Save As) and also save it in the directory you just created . Make sure that the file ends with `.txt` and not `.yml`.
4. Open up a `conda terminal`,   `WSL` (or any other `terminal`), and create a new `conda environment` with the following command: `conda create -n Clean_Repro_Code_Neuromatch python=3.10.6`.
5. Next, open up a `conda terminal` (or any other `terminal`), activate the `conda environment` with `conda activate Clean_Repro_Code_Neuromatch` (or on older `conda environment managers` with `source activate Clean_Repro_Code_Neuromatch` for `mac` and `linux` and `activate Clean_Repro_Code_Neuromatch` for `windows`).
6. Run `conda config --set channel_priority flexible`
7. Now run the following command to install all required `python packages`, pointing to the `requirements.txt` you downloaded before: `pip install -r /path/to/requirements.txt`. For example, `pip install -r Desktop/Clean_Repro_Code_Neuromatch/requirements.txt`.
8. Finally, via the `terminal`, ie `WSL` on `windows OS`, move to the folder where you've put all the unzipped content of this workshop, e.g. with the command `cd ~/Desktop/Clean_Repro_Code_Neuromatch` and run the command `jupyter notebook`. If the `notebook server` isn't automatically opened in a new browser window, please copy-paste either the `http://127.0.0.1:8888/...` or the `http://localhost:8888/...` path into a new browser window and press `Enter`. You should now see the `jupyter notebook server` (looking like a file browser and displaying the content of the directory). 
```
````

## Support


````{tip}
If the instructions aren't working and you have spent more than 15-20 minutes troubleshooting on your own, reach out with the exact problems you're having.
One of the instructors will try and get back to you quickly to help resolve the situation.
````