Paranoik
========

Paranoik is a Python Framework, intended to easify automation of backups on servers and developers' machines. Most of the currently available backup solutions are too hard to configure, have a big learning curve, and are not written in Python. :) Since now I have tried a bunch of backup tools, but no one fully satisfied my needs.

Overview
--------

Paranoik provides a mechanism to backup different things on a server, like:

* Directories
* MySQL Databases
* PostgreSQL Databases
* etc.

Separate components that define backup logic are called "backup providers". It is pretty easy to create new backup providers. It is nothing more than a class that inherits from `Backupable` (something that can be backuped).

Backup Providers
----------------

* Directory - allows to copy directories to another backup location.

```python
    directory = Directory("Some Directory Backup Resource")
    directory.path = "/path/to/directory"
    directory.destination = "/backup/location"
    directory.backup()
```

* MySQL - executes `mysqldump` and writes the output to a file.

```python
    database = MySQL("Some Database")
    database.database = "database_name"
    database.username = "user"
    database.password = "Passw0rd!"
    database.destination = "/path/to/dump.sql"
    database.backup()
```

Syncers
-------

Syncers primary task is to synchronize content that is locally available with remote services.
