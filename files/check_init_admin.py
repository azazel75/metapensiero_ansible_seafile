#coding: UTF-8

'''This script would check if there is admin, and prompt the user to create a new one if non exist'''

import sys
import os

class RPC(object):
    def __init__(self):
        import ccnet
        ccnet_dir = os.environ['CCNET_CONF_DIR']
        self.rpc_client = ccnet.CcnetThreadedRpcClient(ccnet.ClientPool(ccnet_dir))

    def get_db_email_users(self):
        return self.rpc_client.get_emailusers('DB', 0, 1)

    def create_admin(self, email, user):
        return self.rpc_client.add_emailuser(email, user, 1, 1)

def need_create_admin():
    users = rpc.get_db_email_users()
    return len(users) == 0

def create_admin(email, passwd):
    if rpc.create_admin(email, passwd) < 0:
        raise Exception('failed to create admin')
    else:
        print 'Successfully created seafile admin'

rpc = RPC()

def main():
    if not need_create_admin():
        return
    import os
    email = os.environ['SEAFILE_ADMIN_EMAIL']
    passwd = os.environ['SEAFILE_ADMIN_PASSWORD']

    if email and passwd:
        create_admin(email, passwd)
    else:
        raise ValueError('Missing email or password')

if __name__ == '__main__':
    try:
        main()
    except Exception, e:
        print 'Error happened during creating seafile admin.'
        sys.exit(1)
