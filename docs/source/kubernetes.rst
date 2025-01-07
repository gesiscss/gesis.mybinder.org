Kubernetes
==========

We run Kubernetes on `bare-metal server <https://en.wikipedia.org/wiki/Bare-metal_server>`_ and this requires some considerations.

..  important::

    Network load balancer is not available out of the box on bare-metal server.

MetalLB
-------

We use `MetalLB <https://metallb.universe.tf/>`_ as a network load-balancer.

Ingress NGINX Controller
------------------------

We use `Ingress NGINX Controller <https://kubernetes.github.io/ingress-nginx>`_ to expose the servers running on the Kubernetes cluster.

..  figure:: ./img/ingress-nginx.drawio.svg
    :alt: Diagram of Kubernetes cluster.

The Kubernetes node running the Ingress Controller **must** be the Kubernetes node with the public IP address.
