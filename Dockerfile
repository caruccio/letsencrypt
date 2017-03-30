FROM centos/python-35-centos7

USER root

ENV HOME=/getssl

RUN yum install -y openssl bind-utils && \
    yum clean all && \
    cd / && \
    git clone https://github.com/srvrco/getssl.git && \
    mkdir -p /getssl/www && \
    chown -R 1001:root /getssl && \
    chmod 777 /getssl

COPY run /getssl/run
COPY http-server.py /getssl/http-server.py

RUN chmod -R 777 /getssl

WORKDIR /getssl

USER 1001

CMD /getssl/run
