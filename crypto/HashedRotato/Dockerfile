FROM ubuntu:20.04


RUN apt-get update && \
        apt-get -y upgrade && \
        apt-get install -y \
            xinetd \
            iproute2 \
            python3

RUN groupadd -r user && useradd -r -g user user

COPY --chown=root:user ./build/start.sh /home/user/start.sh
COPY --chown=root:root ./build/ctf.conf /etc/xinetd.d/ctf
COPY --chown=root:user ./src/flag.txt /home/user/flag.txt
COPY --chown=root:user ./dist/main.py /home/user/main.py

WORKDIR /home/user

RUN chmod 444 ./flag.txt && \
    chmod 444 ./main.py && \
    chmod 555 ./start.sh && \
    chmod 444 /etc/xinetd.d/ctf

USER user
EXPOSE 30005

CMD ["xinetd","-dontfork","-f","/etc/xinetd.d/ctf"]
