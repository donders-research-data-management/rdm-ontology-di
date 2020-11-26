.. _mount-network-drive:

Mount network drive
===================

On Windows and OS X you can mount the webdav connection directly as a network drive.

Mounting webdav on OS X
-----------------------

Open Finder, click "Go -> Connect to server..." or press the shortcut ``Command-K``.

Enter your username and the server address as ${repositoryWebdavUrl}. You can click the "+" symbol on the right to add it to your list of favorite servers.

Press enter and you will be prompted for your username and password. Enter the username and the one time password from the :ref:`datra access account <data-access-account>`. It is convenient to store your password in your Keychain for browsing, but note that it will only be valid for 72 hour after which you have to enter the new password.

Mounting webdav on Windows
--------------------------

.. note::
    :mode: warning

    Although it's technically possible, mounting WebDAV as network drive on Windows is known to be unstable and sometimes problematic. It is suggested to use other WebDAV client (such as :ref:`cyberduck <cyberduck>`) to transfer data on Windows.

Open File explorer, right-click on "Network", and click "map network drive". Then click "connect to a web site that you can use to store your documents and pictures" -> next -> choose custom network location -> next -> add network address ${repositoryWebdavUrl}.

Windows will prompt you for your username and password, which you can get from the :ref:`data access account <data-access-account>`.

.. include:: readmore.rst
