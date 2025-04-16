# BMFM-SM &nbsp;/&nbsp; Inference for SMILES

<!--
The description & support tags are consumed by the generate_docs() script
in the openad-website repo, to generate the 'Available Services' page:
https://openad.accelerate.science/docs/model-service/available-services
-->

<!-- support:apple_silicon:true -->

[![License MIT](https://img.shields.io/github/license/acceleratedscience/openad_service_utils)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Docs](https://img.shields.io/badge/website-live-brightgreen)](https://acceleratedscience.github.io/openad-docs/)  
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

<br>

## About

<!-- description -->
This OpenAD service provides access to the **Biomedmultiview** foundation model with checkpoints for the following properties:

| BACE | BBBP | CLINTOX | ESOL | FREESOLV | HIV |
| ---- | ---- | ------- | ---- | -------- | --- |

| LIPOPHILICITY | MUV | QM7 | SIDER | TOX21 | TOXCAST |
| ------------- | --- | --- | ----- | ----- | ------- |

More information:  
[github.com/BiomedSciAI/biomed-multi-view](https://github.com/BiomedSciAI/biomed-multi-view)  
[arxiv.org/abs/2410.19704](https://arxiv.org/abs/2410.19704)
<!-- description -->

For instructions on how to deploy and use this service in OpenAD, please refer to the [OpenAD docs](https://openad.accelerate.science/docs/model-service/prepackaged-models).

<br>

## Overview

![image](images/overview.png)

<br>

## Deployment Options

- ✅ [Deployment via container + compose.yaml](https://openad.accelerate.science/docs/model-service/deploying-models#deployment-via-container-composeyaml-recommended)
- ✅ [Deployment via container](https://openad.accelerate.science/docs/model-service/deploying-models#deployment-via-container)
- ✅ [Local deployment using a Python virtual environment](https://openad.accelerate.science/docs/model-service/deploying-models#local-deployment-using-a-python-virtual-environment)
- ✅ [Cloud deployment to Red Hat OpenShift](https://openad.accelerate.science/docs/model-service/deploying-models#cloud-deployment-to-red-hat-openshift)
- ✅ [Cloud deployment to SkyPilot on AWS](https://openad.accelerate.science/docs/model-service/deploying-models/#cloud-deployment-to-skypilot-on-aws)
