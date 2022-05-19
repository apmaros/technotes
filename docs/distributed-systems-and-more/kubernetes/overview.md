# Overview

Kubernetes is a platform for managing containerized workflows and services. It facilitates declarative configuration and automation.

## Main Features

Kubernetes provides following:

- Service discovery and load balancing - container is exposed via DNS or IP
- storage orchestration
- automated rollout and rollback
- self-healing
- secret and configuration management

## Kubernetes Components

Nodes - a set of worker machines running containerized applications. Every cluster has at least one worker node
Pod - a component of the application workflow (more on pods lates in text)
Control plane - manages the worker nodes and the Pods in the cluster. Usually runs over multiple machines [2]

![kubernetes components](https://raw.githubusercontent.com/apmaros/technotes/main/docs/_assets/kubernetes/kubernetes-components.png)

### Control Plane Components

Control plane consists of a set of components which are making global decision about the cluster.

- **Kube-apiserver** - It is the frontend of the control plane
- **etcd** - Consistent, highly available key-value storage storing all cluster data
- **kube-scheduler** - watches for newly created Pods with no assigned node and selects a node for them to run on
- **kube-controller-manager** - runs a controller process. A multiple logical controller processes are packaged in a single binary and running as a single physical process. Some controller types are:
  - Node controller - noticing and responding to loosing a node
  - Job controller
  - Enpoint controller - populates endpoints object
- **cloud-controller-manages** - A Kubernetes control plane component that embeds cloud-specific control logic

### Node Components

Node components run on every node maintaining running pods and providing the kubernetes runtime environment.

- **kubelet** - makes sure that containers are running in a Pod. An agent running on every node in the cluster.
- **kube-proxy** - maintains network rules on nodes, what allows the network communication to Pods from inside and outside of its cluster
- **container runtime** - a runtime that is responsible for running the container, e.g. containerd

## References

1. Kubernetes Documentation/Concepts/Overview <https://kubernetes.io/docs/concepts/overview/>
2. Kubernetes Documentation/Concepts/Overview/Kubernetes Components <https://kubernetes.io/docs/concepts/overview/components/>
