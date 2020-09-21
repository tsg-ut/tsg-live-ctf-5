FROM rust:1.46

RUN apt-get update && \
        apt-get -y upgrade && \
        apt-get install -y \
            xinetd \
            iproute2 \
            python3.7

RUN groupadd -r user && useradd -r -g user user -d /home/user

COPY --chown=root:user ./build/env /home/user/env
COPY --chown=root:root ./build/ctf.conf /etc/xinetd.d/ctf
COPY --chown=root:user ./build/flag /home/user/env/flag
COPY --chown=root:user ./build/start.sh /home/user/start.sh

WORKDIR /home/user

RUN chmod 444 /etc/xinetd.d/ctf && \
    chmod 444 env/flag && \
    chmod 555 ./start.sh

RUN mkdir -p /prog
RUN chown user:user /prog

USER user
EXPOSE 30001

CMD ["xinetd", "-dontfork"]

