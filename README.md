# Overview

This interface layer handles the communication between a Jenkins master
and a Jenkins extensions via the `jenkins-extension` interface.

# Usage

## Provides

The interface on the provider side sets the `{relation_name}.connected` state
to signal that an extension has connected.

The interface will install all plugins specified in the `required_plugins`
field of the established relation.

## Requires

This is the side of the interface that an extension charm will use to be informed
of the availability of Jenkins.

The interface layer sets the following states for the extension to react to:

conv.set_state('{relation_name}.available')
            conv.set_state('{relation_name}.has.changed')

  * `{relation_name}.available`: The extension has been related to Jenkins
  and is ready.

  * `{relation_name}.changed`: The information passed to the extensions
  has changed.

  The client can retrieve information from Jenkins via:

  * `get_connection_info`: Returns all required info and credentials needed
  to access jenkins. Changes to the connection information must be acknowlegded
  with a call to `change_acked`.


# Resources

- [Juju mailing list](https://lists.ubuntu.com/mailman/listinfo/juju)
- [Juju community](https://jujucharms.com/community)
