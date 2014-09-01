metapensiero_ansible_seafile
============================

Ansible role to install Seafile on a Debian Wheezy host.

To be used with a config like::

    config:
      version: 3.1.3
      orgname: myorgname
      base: /srv
      data: /var/lib/seafile
      database:
        type: postgresql
        user: seafile
        host: localhost
        port: 5432
        names:
          ccnet: ccnet_db
          seafile: seafile_db
          seahub: seahub_db
      ccnet:
        server_name: seafile
        port: 8001
        name: file.example.com
        host: file.example.com
        protocol: https
      seafile:
        port: 12001
        fileserver_port: 8082
      seahub:
        enable_public_group: yes
        smtp:
          host: localhost
          port: 25
          from_email: seafile@example.com
      frontend: nginx

The credentials (for db user, and seahub's SECRET_KEY) are by default
stored in ``$PWD/credentials/{{inventory_hostname}}`` directory and
can be specified by defining the following variables::

  seafile_db_password: "{{lookup('password', credentials_dir + '/db_' + recipe.seafile.database.user)}}"
  seafile_secret_key: "{{lookup('password', credentials_dir + '/seahub_secret_key length=50')}}"
  seafile_admin_password: "{{lookup('password', credentials_dir + '/seafile_admin')}}"
This role is is designed to install with a PostgreSQL database. It
creates the user and the tables, but packages are considered to be
installed externally (i have a proper role to do that). The packages
that are (currently) considered installed are:

- python2.7
- python2.7-dev
- python-psycopg2
- python-simplejson
- python-imaging
- python-setuptools
- postgresql-9.1
- postgresql-contrib-9.1
- python-flup
- nginx
