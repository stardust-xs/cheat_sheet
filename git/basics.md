<!-- markdownlint-disable MD033 MD041 -->
# Git :octocat:

This cheat sheet covers at least whatever basics you need to know about [**Git**](https://git-scm.com/).

**DISCLAIMER:** This may not cover everything that is out there about Git but I'll try my best to keep things simple and explain as much as possible.

**NOTE:** I've added hyperlinks to the topics that I won't be covering here in-depth but are **required*** for sake of "better" understanding.

## What is Git?

So, Git is a *distributed* [**Version Control System**](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control) (VCS) and not GitHub or GitLab.
It is a "thing" or a technology by itself, called as **Source Code Management** or [**SCM**](https://www.atlassian.com/git/tutorials/source-code-management) in short.

There are bunch of tools out there for doing SCM like **CVS**, **Subversion** and **Perforce** but Git outclasses them by being a **Distributed** VCS. You can find more on that [**here**](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control). But in simple terms, a distributed vcs means that every user has a **copy of their work** (cloned/forked branch) which is "distributed" by the owner (master branch).

Distributing copies in this way keeps everybody's work seperate and gives them full liberty to develop new features or fix/patch existing problems. Once the user is satisfied with the developed code or patch it can be merged with the main code.

**NOTE:** There's something called as **Centralised** VCS, personally I haven't worked with CVCS so I don't know much about it. That said the above mentioned SCM tools like **CVS**, **Subversion** (SVN) and **Perforce** are examples of Centralised VCS.

## How to get started with Git?

Okay, so if the above description of Git hasn't made any sense whatsoever it is still fine. Since stuff as dense as Git is often better understood by visualizing and by doing it. So to get started with Git, you need to install Git first.

Download and install Git onto your machine from [**here**](https://git-scm.com/downloads). The download and installation is simple and pretty straight-forward. Once you have Git on your system, verify whether its installed correctly using the `git --version` command.

<p align="center">
  <img src="https://github.com/xames3/cheat_sheet/blob/assets/media/git--version.png?raw=true">
</p>

## Configuring Git

Once Git is installed we can start using it.
To use Git, we need to configure it first. Configuring Git is similar to **logging** in wherein you need to provide your credential and other optional metadata.

I have my own preference for this and I would recommend you to follow these steps too. These following "steps" are not mandatory and can be overridden later whenever you want.

Okay, so my Git "configuration" involves 2 steps:
- Adding User and
- Adding GPG key

### Adding User

This is basically similar to logging in and saving your credentials. Although you need to enter your credentials while pulling and pushing your changes.

**NOTE:** This feature works great when integrated with VSCode.

So in order to add your Git *(GitHub/GitLab/BitBucket)* account, you need to add the below commands:
```bash
git config --global user.name "<YOUR GIT USERNAME>"
git config --global user.email "<YOUR REGISTERED EMAIL WITH GIT>"
```

<p align="center">
  <img src="https://github.com/xames3/cheat_sheet/blob/assets/media/git-add-user.png?raw=true">
</p>

### Adding GPG Key

Adding GPG key is a **totally optional** step. I honestly don't know what exactly it does, but I what I am aware off is the fact that adding a GPG key marks your commit as <span style="color:green">Verified</span> in the commit history.

<p align="center">
  <img src="https://github.com/xames3/cheat_sheet/blob/assets/media/git-add-gpg.png?raw=true">
</p>

We'll see how to setup GPG key **here**.<br>Once we've created and added our GPG key to our GitHub profile, we'll configure it with git as well with the below commands:
```bash
git config --global user.signingKey "<YOUR GPG KEY>"
git config --global commit.gpgSign true
```

<p align="center">
  <img src="https://github.com/xames3/cheat_sheet/blob/assets/media/git-configure-gpg.png?raw=true">
</p>

## Get help

If you need help with any particular command, just `git <COMMAND VERB> --help`. Here `<COMMAND VERB>` means the commands that you use in particular to perform some **action** hence the verb.

For example:
```bash
git push --help
git pull --help
git checkout --help
git ... --help
```

## Working with Git

Now that you've setup Git, lets start using it. Before we start using Git we need to pick/consider either of the 2 scenarios:
- Either you're trying to implement git in your existing/new **local** project (repository) OR
- You're trying to work on/with someone else's **remote** project.


Here, local and remote are the 2 key takeaways.<br>Local means "**locally**" available. The stuff which is literally present on your computer and that you can directly interact with whereas Remote means "**remotely**" available. Which is present far far away like on the **internet**. This is the stuff that you cannot interact directly or you need some special access/permission to fiddle around.

First is the easiest as it gets than the latter.

## Tracking your local code with Git

This part explains how to start using git in your existing/new *"non-git"* project. Now going forward for the sake of simplicity we'll call our projects as **repositories**. So we're working with our local repository or **repo** in short. Doing this will enable us to track our repo using Git. To do this we need to initialize our repo using `git init` command.


<p align="center">
  <img src="https://github.com/xames3/cheat_sheet/blob/assets/media/git-init.png?raw=true">
</p>

This will initialize an **empty** git repository, here empty doesn't implies that your **local** directory is empty rather it means the "*hypothetical*" **remote** repository (you just created by `git init`) is empty. This initialization adds a `.git` directory which holds all the metadata about the changes that you make to this repo.

<p align="center">
  <img src="https://github.com/xames3/cheat_sheet/blob/assets/media/local-repo-init.png?raw=true">
</p>

And that's it! This is how you start using git with your new/existing repository.
