# Openshift setup

> update any necessary resources in the values.yaml

### Install helm chart
```shell
helm install sm ./helm-chart
```

### Run the build config to create the docker image
```shell
oc start-build sm-build
```