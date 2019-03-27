FROM oraclelinux:7-slim

ARG GRAAL_VERSION=1.0.0-rc14
ENV LANG=en_US.UTF-8

ENV GRAALVM_PKG=https://github.com/oracle/graal/releases/download/vm-$GRAAL_VERSION/graalvm-ce-$GRAAL_VERSION-linux-amd64.tar.gz \
    JAVA_HOME=/opt/graalvm-ce-$GRAAL_VERSION/ \
    PATH=$PATH:/opt/rh/llvm-toolset-7/root/usr/bin \
    LD_LIBRARY_PATH=/opt/rh/llvm-toolset-7/root/usr/lib64 \
    MANPATH=/opt/rh/llvm-toolset-7/root/usr/share/man \
    PKG_CONFIG_PATH=/opt/rh/llvm-toolset-7/root/usr/lib64/pkgconfig \
    PYTHONPATH=/opt/rh/llvm-toolset-7/root/usr/lib/python2.7/site-packages \
    X_SCLS=llvm-toolset-7

RUN curl -o /etc/yum.repos.d/public-yum-ol7.repo http://yum.oracle.com/public-yum-ol7.repo \
    && yum-config-manager --enable ol7_developer \
    && yum-config-manager --enable ol7_developer_EPEL \
    && yum-config-manager --enable ol7_optional_latest \
    && yum-config-manager --enable ol7_software_collections \
    && yum install -y bzip2-devel ed gcc gcc-c++ gcc-gfortran gzip file fontconfig less libcurl-devel make openssl-devel readline-devel tar vi which xz-devel zlib-devel \
    && yum install -y glibc-static libcxx libcxx-devel llvm-toolset-7 zlib-static \
    && rm -rf /var/cache/yum

RUN fc-cache -f -v

RUN set -eux \
    && curl --fail --silent --location --retry 3 ${GRAALVM_PKG} \
    | gunzip | tar x -C /opt/ \
    && mkdir -p "/usr/java" \
    && ln -sfT "$JAVA_HOME" /usr/java/default \
    && ln -sfT "$JAVA_HOME" /usr/java/latest \
    && for bin in "$JAVA_HOME/bin/"*; do \
        base="$(basename "$bin")"; \
        [ ! -e "/usr/bin/$base" ]; \
        alternatives --install "/usr/bin/$base" "$base" "$bin" 20000; \
    done \
    && chmod +x /usr/local/bin/gu

CMD java -version

RUN gu install r && gu install python && gu install ruby

RUN wget https://raw.githubusercontent.com/kallooa/usefulScripts/master/rpkginstall && chmod +x rpkginstall
RUN cat Rpackages.txt | while read line; do echo "./rpkginstall $line"; done;
