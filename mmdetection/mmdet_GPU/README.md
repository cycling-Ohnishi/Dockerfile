# Dockerfile for mmdet_GPU 
- CUDA 12.4
- Ubuntu 22.04 (GPU)
- Python3.11  

1. ## Build Image  
    To clone the current relesse:
    ```bash:bash
    $ git clone https://github.com/atomon/Dockerfile.git
    ```
    To build mmdet_GPU enviroment:
    ```bash:bash
    $ cd ./Dockerfile/mmdetection/mmdet_GPU
    $ docker compose build
    ```

2. ## Run a Docker container based on image
    To run a docker container based on my/image:
    ```bash:bash
    $ docker compose up -d && docker compose exec mmdet /bin/bash
    ```

> [!NOTE]
> Default runtime of Docker is not nvidia, not build in cuda enviroment.
> So, after create the container, run `python -m pip uninstall mmcv && python -m pip install --no-cache-dir mmcv==2.1.0`
