FROM joyzoursky/python-chromedriver:3.7

ARG user_name
ARG user_password

COPY * /

WORKDIR /

RUN pip install -r requirements.txt

CMD [ "python", "./test.py" ]