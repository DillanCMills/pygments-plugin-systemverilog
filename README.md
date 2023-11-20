# SystemVerilog Pygments plugin

This repository contains a SystemVerilog plugin for the [Pygments](https://pygments.org) syntax highlighter. It provides a lexer and two companion styles (light mode and dark mode) that take full advantage of the language lexing. The SystemVerilog plugin that is distributed with Pygments directly lacks support for much of the language and therefore produces sub-optimal highlighting. By leveraging a more advanced lexer (based on the lexing performed in the Sublime Text SystemVerilog package, https://github.com/TheClams/SystemVerilog), this plugin is able to produce results that look just as good as code written directly in an editor like Sublime Text or VS Code.

To be usable, plugins must be installed. If you are running the `pygmentize`
command, you probably want to use a
[virtual environment](https://docs.python.org/3/library/venv.html)
to avoid installing packages globally. For example, here is how to create
a virtual environment and install this set of plugins into it:

```
python -m venv venv/
venv/bin/pip install . # install the project in current directory into the virtual environment
venv/bin/pygmentize ... # use the pygmentize command from the virtual environment
```

Alternatively, since this plugin uses the [Hatch](https://hatch.pypa.io)
tool, you may use

```
hatch run pygmentize ...
```

If you are using Pygments from Python, possibly through a tool like Sphinx,
mkdocs, etc., then you just need to install the plugin in the same environment
as the one where you installed Pygments.

Since I mostly wrote this plugin for my own usage, I currently don't intend to distribute it on PyPi.

#### License for this template

There isn't much copyrightable content here, but if you are worried about reuse:

Copyright (C) 2023 by Dillan Mills

Permission to use, copy, modify, and/or distribute this software for any purpose
with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF
THIS SOFTWARE.
