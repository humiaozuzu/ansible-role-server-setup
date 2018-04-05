
import os
import glob

HAVE_PARAMIKO = False
try:
    import paramiko
    HAVE_PARAMIKO = True
except ImportError:
    pass

from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()


class LookupModule(LookupBase):

    def load_ssh_config(self):
        client = paramiko.SSHClient()
        ssh_config = paramiko.SSHConfig()
        user_config_file = os.path.expanduser("~/.ssh/config")
        if os.path.exists(user_config_file):
            with open(user_config_file) as f:
                ssh_config.parse(f)
        # temp workaround
        user_config_path = os.path.expanduser("~/.ssh/config.d/")
        for filename in glob.iglob(user_config_path + '*'):
            with open(filename) as f:
                ssh_config.parse(f)
        return ssh_config

    def run(self, terms, variables=None, **kwargs):

        if HAVE_PARAMIKO is False:
            raise AnsibleError("Module paramiko is not installed")

        ssh_config = self.load_ssh_config()
        ret = []
        for term in terms:
            display.v("Lookup term: %s" % term)
            host = ssh_config.lookup(term)['hostname']
            if host == term:
                raise AnsibleError("hostname %s not found" % term)
            ret.append(host)
        return ret
