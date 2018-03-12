FROM registry.access.redhat.com/rhscl/python-36-rhel7

ADD . /workspace
WORKDIR /workspace

EXPOSE 5000

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
