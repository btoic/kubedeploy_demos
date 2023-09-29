# kubedeploy_demos
Demos for Kubedeploy

To get started you will need [Docker](https://www.docker.com/), [Kind](https://kind.sigs.k8s.io/), [Helm](https://helm.sh/) and [Helmfile](https://helmfile.readthedocs.io/en/latest/) installed on your machine.

## Local kind cluster prepwork


Start your local Kind cluster

```bash
cd kind/
kind create cluster --config kind-cluster.yaml
```
Command will create a 3 node cluster, one control-plane node with taints, and two worker nodes simulating two availability zones.

After that apply the ingress and cert-manager

```bash
helmfile --file helmfile.yaml apply
```

This will install and expose Haproxy ingress controller on port 80 and 443. Cert manager will be installed with local cert issuer.


