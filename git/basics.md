<!-- markdownlint-disable MD033 MD041 -->
# Git

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
