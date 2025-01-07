Environments
============

The Methods Hub team uses the `development, testing, acceptance and production <https://en.wikipedia.org/wiki/Development,_testing,_acceptance_and_production>`_ cycle (DTAP street) but for the Kubernetes Cluster we only use acceptance and production.

Acceptance
----------

..  important::

    This servers are physical located in Cologne.

Ansible inventory: https://git.gesis.org/methods-hub/binder.methodshub.gesis.org/-/blob/main/ansible/inventories/gesis-acceptance?ref_type=heads

+-----------------------------------+------------------------------------------------------------+
| Service                           | URL                                                        |
+===================================+============================================================+
| GESIS Notebooks                   | https://notebooks-test.gesis.org/                          |
+-----------------------------------+------------------------------------------------------------+
| BinderHub                         | https://binder.methodshub.gesis.org/                       |
+-----------------------------------+------------------------------------------------------------+

Production
----------

..  important::

    This servers are physical located in Cologne.

Ansible inventory: https://git.gesis.org/methods-hub/binder.methodshub.gesis.org/-/blob/main/ansible/inventories/gesis-production?ref_type=heads

+-----------------------------------+------------------------------------------------------------+
| Service                           | URL                                                        |
+===================================+============================================================+
| GESIS Notebooks                   | https://notebooks.gesis.org/                               |
+-----------------------------------+------------------------------------------------------------+
| BinderHub                         | https://binder.methodshub.gesis.org/                       |
+-----------------------------------+------------------------------------------------------------+
