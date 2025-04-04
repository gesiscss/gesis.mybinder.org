.. Methods Hub Kubernetes documentation master file, created by
   sphinx-quickstart on Mon Jan  6 18:48:14 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Methods Hub's Interactive Environment's Kubernetes Cluster
==========================================================

Methods Hub's `Interactive Environment`_ is based on `mybinder.org <https://mybinder.org>`_ that requires `Kubernetes <https://kubernetes.io/>`_. This project covers the configuration of the Kubernetes Cluster used by the Methods Hub team for the `Interactive Environment`_. The configuration of the `Interactive Environment`_ itself is done in conjunction with the `mybinder.org operators <https://mybinder-sre.readthedocs.io/en/latest/index.html#what-is-the-mybinder-org-operations-team>`_ using `mybinder.org-deploy <https://github.com/jupyterhub/mybinder.org-deploy/>`_ at GitHub.

.. mermaid::
   :align: center
   :alt: Diagram of deploy of Methods Hub's Interactive Environment.
   :caption: Diagram of deploy of Methods Hub's Interactive Environment.

   sequenceDiagram
      actor user as User
      participant gitlab as GESIS GitLab<br/>interactive-environment
      participant glcd as GESIS GitLab<br/>Continuous Integration
      participant github as GitHub<br/>mybinder.org-deploy
      participant ghcd as GitHub<br/>Actions
      participant hetzner as Hetzner<br/>78.46.233.119

      user->>gitlab: git push
      gitlab->>glcd: trigger
      glcd->>hetzner: ansible

      user->>github: git push
      github->>ghcd: trigger
      ghcd->>hetzner: helm

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   infrastructure-as-code
   environments
   kubernetes
   ansible
   gitlab

.. _Interactive Environment: https://git.gesis.org/methods-hub/interactive-environment/
