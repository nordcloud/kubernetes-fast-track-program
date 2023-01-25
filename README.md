# Kubernetes Fast-Track program

## Overview

The Kubernetes Fast-Track program is an initiative to fast-track existing and future Nordcloud engineers onto Kubernetes. This Github project provides the necessary tools to setup a sandbox Kubernetes environment.

## Requirements

Ensure the following tools are installed.

- [Kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Docker](https://docs.docker.com/get-docker/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)

## Getting started

Spin up a new local Kubernetes cluster.

```bash
$ minikube start --driver=docker --kubernetes-version=1.23.16
😄  minikube v1.29.0 on Darwin 13.2 (arm64)
✨  Using the docker driver based on user configuration
📌  Using Docker Desktop driver with root privileges
👍  Starting control plane node minikube in cluster minikube
🚜  Pulling base image ...
💾  Downloading Kubernetes v1.23.16 preload ...
    > preloaded-images-k8s-v18-v1...:  343.85 MiB / 343.85 MiB  100.00% 3.23 Mi
🔥  Creating docker container (CPUs=2, Memory=4000MB) ...
🐳  Preparing Kubernetes v1.23.16 on Docker 20.10.23 ...
    ▪ Generating certificates and keys ...
    ▪ Booting up control plane ...
    ▪ Configuring RBAC rules ...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🔎  Verifying Kubernetes components...
🌟  Enabled addons: storage-provisioner, default-storageclass

❗  /opt/homebrew/bin/kubectl is version 1.26.1, which may have incompatibilities with Kubernetes 1.23.16.
    ▪ Want kubectl v1.23.16? Try 'minikube kubectl -- get pods -A'
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
```

Shut down the local Kubernetes cluster.

```bash
$ minikube delete
🔥  Deleting "minikube" in docker ...
🔥  Deleting container "minikube" ...
🔥  Removing /Users/fforoozan/.minikube/machines/minikube ...
💀  Removed all traces of the "minikube" cluster.
```

## Contributing

Before contributing, please read the [Contribution guidelines](./CONTRIBUTING.md)

## License

Copyright 2023 Nordcloud Oy or its affiliates. All Rights Reserved.
