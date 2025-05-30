FROM continuumio/miniconda3 as builder

# Set the working directory in the container
WORKDIR /app

# set up ssh
RUN mkdir /root/.ssh && chmod 0700 /root/.ssh && ssh-keyscan -t rsa github.ibm.com github.com >> /root/.ssh/known_hosts

# Create the Conda environment from the environment.yml file
#RUN --mount=type=ssh git clone https://github.com/acceleratedscience/biomed-multi-view.git && \
RUN export ROOT_DIR=/opt/conda && \
mkdir -p $ROOT_DIR && conda create -y python=3.11  --name bmfm-sm
    # conda env create -f bmfm-sm/conda.yaml

FROM pytorch/pytorch:2.1.0-cuda12.1-cudnn8-runtime AS runtime
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Los_Angeles

RUN apt-get update && apt-get install -y --no-install-recommends software-properties-common \
    build-essential curl git ssh libxrender1 libxext6\
    && rm -rf /var/lib/apt/lists/*

# Copy Conda environment from the builder stage
COPY --from=builder /opt/conda /opt/conda
#COPY --from=builder /app/biomed-multi-view /app

# Set the working directory in the container
WORKDIR /app
#
# Activate the Conda environment and ensure the PATH is set correctly
ENV PATH /opt/conda/envs/bmfm-sm/bin:$PATH
RUN echo "conda activate bmfm-sm" >> ~/.bashrc

# fix a file for local install
#RUN sed -i 's|^-f https://data.pyg.org/whl/torch-2.1.0+cu121.html|#&|' requirements.txt
#R#UN pip install # pip install -e .

# Copy the rest of the application code to the working directory
COPY ./requirements.txt ./api_workspace/requirements.txt
COPY ./requirements_extra.txt ./api_workspace/requirements_extra.txt
RUN python --version
# set up ssh
RUN mkdir /root/.ssh && chmod 0700 /root/.ssh && ssh-keyscan -t rsa github.ibm.com github.com >> /root/.ssh/known_hosts
RUN --mount=type=ssh pip install --no-cache-dir -r api_workspace/requirements.txt 
RUN --mount=type=ssh pip install --no-cache-dir -r api_workspace/requirements_extra.txt 
#RUN pip install .


ENV HF_HOME="/tmp/.cache/huggingface" \
MPLCONFIGDIR="/tmp/.config/matplotlib" \
LOGGING_CONFIG_PATH="/tmp/app.log" \
gt4sd_local_cache_path="/tmp/.openad_models" 
COPY . ./api_workspace
# Specify the command to run when the container starts
CMD ["python", "api_workspace/bmfm_sm_api/sm_implementation.py"]
