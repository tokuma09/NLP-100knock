FROM ubuntu:20.04
LABEL maintainer="Tokuma Suzuki tokuma.suzuki09@gmail.com"

ENV SHELL /bin/bash
ENV DEBIAN_FRONTEND noninteractive
ENV CRF_VERSION 0.58
ENV CABOCHA_VERSION 0.69

COPY requirements.txt /tmp

RUN apt-get update && apt-get install -y \
    build-essential git wget curl tar gzip file sudo zlib1g-dev && \
    # python install
    apt-get install -y python3.8 python3.8-venv python3-pip && \
    cd /usr/local && \
    # Python Libraries
    pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt &&\
    # MeCab
    apt-get install -y mecab libmecab-dev mecab-ipadic mecab-ipadic-utf8 swig &&\
    # mecab-ipadic-neologd
    git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git /tmp/neologd &&\
    /tmp/neologd/bin/install-mecab-ipadic-neologd -n -a -y -p /usr/lib/mecab/dic/mecab-ipadic-neologd &&\
    rm -rf /tmp/neologd &&\
    # CRF ++ (for CaboCha)
    wget -O /tmp/CRF++-${CRF_VERSION}.tar.gz 'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7QVR6VXJ5dWExSTQ' &&\
    cd /tmp/ &&\
    tar xzvf CRF++-${CRF_VERSION}.tar.gz &&\
    cd CRF++-${CRF_VERSION} &&\
    ./configure &&\
    make &&\
    make install &&\
    rm /tmp/CRF++-${CRF_VERSION}.tar.gz &&\
    rm -rf /tmp/CRF++-${CRF_VERSION} &&\
    ldconfig &&\
    # Cabocha
    cd /tmp &&\
    curl -c cabocha-${CABOCHA_VERSION}.tar.bz2 -s -L "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7SDd1Q1dUQkZQaUU" \
    | grep confirm | sed -e "s/^.*confirm=\(.*\)&amp;id=.*$/\1/" \
    | xargs -I{} curl -b  cabocha-${CABOCHA_VERSION}.tar.bz2 -L -o cabocha-${CABOCHA_VERSION}.tar.bz2 \
    "https://drive.google.com/uc?confirm={}&export=download&id=0B4y35FiV1wh7SDd1Q1dUQkZQaUU" &&\
    tar jxf cabocha-${CABOCHA_VERSION}.tar.bz2 &&\
    cd cabocha-${CABOCHA_VERSION} &&\
    export CPPFLAGS=-I/usr/local/include &&\
    ./configure --with-mecab-config=`which mecab-config` --with-charset=utf8 &&\
    make &&\
    make install &&\
    rm /tmp/cabocha-${CABOCHA_VERSION}.tar.bz2 &&\
    rm -rf /tmp/cabocha-${CABOCHA_VERSION} &&\
    ldconfig　



CMD ["/bin/bash"]
