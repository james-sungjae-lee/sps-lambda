FROM amazon/aws-lambda-python:3.9

# optional : ensure that pip is up to data
RUN /var/lang/bin/python3.9 -m pip install --upgrade pip

# install git, curl, unzip
RUN yum install git -y
RUN yum install curl -y
RUN yum install unzip -y

# uninstall awscli1 and install awscli2
RUN pip3 uninstall awscli -y
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN sudo ./aws/install

RUN pip3 uninstall boto3 -y
RUN pip3 install boto3==1.19.10

# git clone
RUN git clone https://github.com/odobenuskr/sps-lambda.git

# move lambdafunc.py
RUN cp spc-lambda/lambda_function.py /var/task/

CMD ["lambda_function.handler"]
