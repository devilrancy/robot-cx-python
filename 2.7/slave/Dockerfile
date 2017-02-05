FROM cloudbees/jnlp-slave-with-java-build-tools

MAINTAINER Naresh Surisetty "nareshskyrocket@gmail.com"

# User Root
RUN id
USER root

RUN apt-get update && apt-get install -y \
        python \
        python-dev \
        libffi-dev \
        libssl-dev \
        python-pip

RUN pip install fabric --upgrade \
        requests --upgrade \
        cffi --upgrade


RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip" \
        && unzip awscli-bundle.zip \
        && ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws

# Install Ubuntu packages
RUN apt-get update
RUN apt-get install alien dpkg-dev debhelper build-essential libaio1 --assume-yes

# Install oracle
# Reference: https://help.ubuntu.com/community/Oracle%20Instant%20Client
# Download RPM files from http://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html
# Get Oracle Client (this isn't the offical download location, but at least it works without logging in!)
RUN curl -O http://repo.dlt.psu.edu/RHEL5Workstation/x86_64/RPMS/oracle-instantclient12.1-basic-12.1.0.1.0-1.x86_64.rpm
RUN curl -O http://repo.dlt.psu.edu/RHEL5Workstation/x86_64/RPMS/oracle-instantclient12.1-devel-12.1.0.1.0-1.x86_64.rpm

# Alien RPM package installer
RUN alien -i *.rpm

# Cleaning up the packages downloaded
RUN rm *.rpm

ADD oracle.conf /etc/ld.so.conf.d/oracle.conf
ADD oracle.sh /etc/profile.d/oracle.sh
RUN chmod o+r /etc/ld.so.conf.d/oracle.conf
RUN chmod o+r /etc/profile.d/oracle.sh

RUN /etc/profile.d/oracle.sh
RUN ldconfig

# Install the packages from http://pypi.python.org
ADD /test/test.py /code/
ADD requirements.txt /code/
WORKDIR /code
RUN pip --no-cache-dir install -r requirements.txt

# Run th python test to make sure the ca_Oracle is properly installed
RUN python test.py

# User Jenkins
USER jenkins

ENTRYPOINT ["/opt/bin/entry_point.sh", "/usr/local/bin/jenkins-slave"]

