Sublime Text 2 Open With Vim
============================
Open current file with vim on terminal.
This script works only for Linux.

Installation
------------

    $ cd ~/.config/sublime-text-2/Packages/
    $ git clone https://github.com/itiut/sublime-text-2-open-with-vim OpenWithVim


Usage
-----

add the following to `User/Default (OSX).sublime-keymap`:

    { "keys": ["ctrl+shift+alt+i"], "command": "open_with_vim" }
