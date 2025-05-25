A laid-back little shell written in Python that feels right at home in your terminal.

- **Command parsing & built-ins**  
  Uses `shlex` to split your input and supports basic built-in commands like `exit`, `echo`, `cd`, `pwd`, `history`, and more.

- **Tab-completion magic**  
  Hit Tab to autocomplete both built-in commands and any executable in your `$PATH`; file-based completion inside directories too.

- **Runs real programs**  
  If it’s not a built-in, it just shells out with `subprocess.run()`, so you can still call `vim`, `git`, or anything else on your system.

- **History tracking**  
  Keeps a simple list of what you’ve typed, so `history` is always handy when you mess up a long command.

Feel free to play around, add more built-ins, or improve upon the functionalities 😊
