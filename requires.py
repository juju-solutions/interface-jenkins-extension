#!/usr/bin/python
from charmhelpers.core.hookenv import log
from charms.reactive import hook
from charms.reactive import RelationBase
from charms.reactive import scopes


class JenkinsExtension(RelationBase):
    scope = scopes.GLOBAL

    @hook("{requires:jenkins-extension}-relation-{joined,changed}")
    def joined(self):
        """Indicate the relation is connected and transmit our credentials."""
        log("Updating extension interface with up-to-date data.")

        self.set_state("{relation_name}.connected")
        conv = self.conversation()
        if conv.get_remote('jenkins_url'):
            conv.set_state('{relation_name}.available')

    def get_connection_info(self):
        '''
        To be called when jenkins has become available
        Returns: Dictionary with connection information.

        '''
        conv = self.conversation()
        connection = {
            "admin_username": conv.get_remote('admin_username'),
            "admin_password": conv.get_remote('admin_password'),
            "jenkins_url": conv.get_remote('jenkins_url'),
            "jenkins-admin-user": conv.get_remote('jenkins-admin-user'),
            "jenkins-token": conv.get_remote('jenkins-token'),
        }

        return connection
