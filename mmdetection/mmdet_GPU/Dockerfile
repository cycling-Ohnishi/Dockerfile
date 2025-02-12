ARG base_image=nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04

FROM ${base_image}


ENV DEBIAN_FRONTEND=noninteractive
ENV LIBRARY_PATH=/usr/local/cuda/lib64/stubs
SHELL ["/bin/bash", "-c"]


RUN <<EOT
apt update
apt install -y vim wget curl git libgl1-mesa-glx libglib2.0-0
apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libreadline-dev libffi-dev libsqlite3-dev libbz2-dev libssl-dev ninja-build
wget https://www.python.org/ftp/python/3.11.11/Python-3.11.11.tgz
tar xf Python-3.11.11.tgz && cd Python-3.11.11
./configure --enable-optimizations
JOBS=$(($(grep cpu.cores /proc/cpuinfo | sort -u | sed 's/[^0-9]//g') + 1))
make -j${JOBS}
make install
update-alternatives --install /usr/bin/python python /usr/local/bin/python3.11 1
EOT

# Install mmdetection
RUN <<EOT
cd /home
python -m venv mmdet-env && source mmdet-env/bin/activate
echo "source /home/mmdet-env/bin/activate" >> /root/.bashrc
git clone https://github.com/open-mmlab/mmdetection.git
python -m pip install wheel setuptools
python -m pip install torch torchvision
python -m pip install -r mmdetection/requirements/build.txt 
python -m pip install -r mmdetection/requirements/runtime.txt 
python -m pip install -r mmdetection/requirements/mminstall.txt
python -m pip install --no-build-isolation -e mmdetection
EOT

WORKDIR /home
COPY ./sample.py /home
