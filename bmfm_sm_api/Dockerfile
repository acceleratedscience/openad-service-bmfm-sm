FROM continuumio/miniconda3 as builder

# Set the working directory in the container
WORKDIR /app

# set up ssh
RUN mkdir /root/.ssh && chmod 0700 /root/.ssh && ssh-keyscan -t rsa github.ibm.com github.com >> /root/.ssh/known_hosts

# Create the Conda environment from the environment.yml file
RUN --mount=type=ssh git clone git@github.ibm.com:BiomedSciAI-Innersource/bmfm-sm.git && \
    conda env create --name bmfm-sm --file bmfm-sm/conda.yaml
    # conda env create -f bmfm-sm/conda.yaml

FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime AS runtime
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Los_Angeles

RUN apt-get update && apt-get install -y --no-install-recommends software-properties-common \
    build-essential curl git ssh libxrender1 libxext6\
    && rm -rf /var/lib/apt/lists/*

# Copy Conda environment from the builder stage
COPY --from=builder /opt/conda /opt/conda
COPY --from=builder /app/bmfm-sm /app

# Set the working directory in the container
WORKDIR /app

# Activate the Conda environment and ensure the PATH is set correctly
ENV PATH /opt/conda/envs/bmfm-sm/bin:$PATH
# RUN echo "conda activate bmfm-sm" >> ~/.bashrc

# fix a file for local install
RUN sed -i 's|^-f https://data.pyg.org/whl/torch-2.1.0+cu121.html|#&|' requirements.txt
RUN pip install -e .

# Copy the rest of the application code to the working directory
COPY ./requirements.txt ./api_workspace/requirements.txt

# set up ssh
RUN mkdir /root/.ssh && chmod 0700 /root/.ssh && ssh-keyscan -t rsa github.ibm.com github.com >> /root/.ssh/known_hosts
RUN --mount=type=ssh pip install --no-cache-dir -r api_workspace/requirements.txt

COPY . ./api_workspace

# Specify the command to run when the container starts
CMD ["python", "api_workspace/bmfm_sm_api/sm_implementation.py"]
