# kubedeploy_demos
Demos for Kubedeploy

To get started you will need [Docker](https://www.docker.com/), [Kind](https://kind.sigs.k8s.io/), [Helm](https://helm.sh/) and [Helmfile](https://helmfile.readthedocs.io/en/latest/) installed on your machine.

## Local kind cluster prepwork


Start your local Kind cluster

```bash
cd kind/
kind create cluster --config kind-cluster.yaml
```

Command will create a 3 node cluster, one control-plane node with taints, and three worker nodes simulating three availability zones.

registry proxy for offiline demos

```bash
docker run -d --name proxy --restart=always --net=kind -e REGISTRY_PROXY_REMOTEURL=https://registry-1.docker.io registry:2
```

After that apply the ingress and cert-manager

```bash
helmfile --file helmfile.yaml apply
```

This will install and expose Haproxy ingress controller on port 80 and 443. Cert manager will be installed with local cert issuer.


