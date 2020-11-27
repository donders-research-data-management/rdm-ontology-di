# How to edit the help document

The online help is written with the [reStructuredText (ReST)](https://en.wikipedia.org/wiki/ReStructuredText). It is a light-weight markup language with separation between documentation content and presentation. With this separation, editor can focus on content writing; while the presentation is taken care by a build process.

The content of the help document could/should be edited with a plain-text editor (such as the Notepad application on Windows, Vim on the command-line of Linux/MacOSX). Following to the editing, one builds the content with a presentation template (e.g. a theme or HTML CSS) and previews the document in a web browser.

Hereafter are possible utilities/workflows that will make this process a bit easier.

## Method 1: edit on GitHub and preview with Readthedocs

One can edit the ReST documents directly on the [GitHub repository](https://github.com/Radboud-University/rdr-configurable-content/tree/master/doc/help).  A corresponding [ReadTheDocs](https://readthedocs.org/) project has been linked to this repository.  As soon as changes are made in the GitHub repository, a process is triggered to rebuild the documentation at this [preview on ReadTheDocs](https://rdm-configurable-content-donders.readthedocs.io/en/latest/).

## Method 2: edit with desktop tools

- [GitHub desktop](https://desktop.github.com/) for syncrhonizing updates between desktop and the GitHub repository.
- [Visual Studio Code](https://code.visualstudio.com/) for editing and previewing the reStructuredText documentations. It requires an [extension](https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext) which makes use of [Sphinx](http://www.sphinx-doc.org/en/master/usage/installation.html) to build ReST.
