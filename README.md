# PhD-Thesis

## Installation

1. Get the main LaTeX package used, [ltstyle](https://github.com/lucastorterotot/ltstyle), by following [its installation instructions](https://github.com/lucastorterotot/ltstyle/blob/master/README.md).

2. Get [some usefull scripts](https://gitlab.com/lucastorterotot/scripts), following [installation instructions](https://gitlab.com/lucastorterotot/scripts/blob/master/README.md).

3. Fork this repository and clone it locally:
```
cd ~/Documents/
git clone YOUR_FORKED_REPO
cd PhD-Thesis/
```

4. Eventually, get mine:
```
git remote add lucas git@github.com:lucastorterotot/PhD-Thesis.git
```

5. To make LaTeX `\input{}` working on any computer, define the `\homedir` command:
```
echo "\IfFileExists{"$(pwd)"/"$(ls README.md)"}{\def\homedir{"$HOME"}}{}" >> homedirs.tex
```