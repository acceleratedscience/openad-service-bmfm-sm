# BMFM Small Molecules Inference for Smiles

## About:
the below Repository is based on the FOundation Model Biomed0multi0view and provides checkpoints for the following properties [ BACE, BBBP, CLINTOX, ESOL, FREESOLV, HIV, LIPOPHILICITY, MUV, QM7, SIDER, TOX21, TOXCAST ].

Pore information can be found at:
https://github.com/BiomedSciAI/biomed-multi-view


## Deployment Options


### Deplyoing with Sky Pilot
1 Support for skypilot on AWS is available. you must have a valid aws account setup with appropriate accound settings to allow sky pilot

 In openad running the following
Step 1:
`catalog model service from 'git@github.com:acceleratedscience/bmfm-sm.git' as sm`
Step 2: 
`model service up sm`

to stop the service run `model service down` in openad.

you will now have to wait until the service is available use `sky status` to see if the service is up and provisioned


### Deploying on podman / docker 
run on the command line `mkdir -p ~/.openad_models`

then using Podman or Docker run the following in the same directory as the compose.yaml file:
step 1:
`compose create`
step 2:
`compose start`

the service will start on poert `8080` change this in the compose file if you wish it to run on another port.

In openad run the following command
`catalog model service from remote 'http://127.0.0.1:8080/' as sm`

### Deploying in venv
you will need a python level of 3.11 & to follow the following installation directions:
https://github.com/BiomedSciAI/biomed-multi-view

Then run `python ./bmfm_sm_api/sm_implementation.py`


In openad run the following command once the container is up and running
`catalog model service from remote 'http://127.0.0.1:8080/' as sm`
