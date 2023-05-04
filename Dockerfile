FROM pypy:latest
WORKDIR /SemanticsNLP

COPY ./requirements.txt ./
COPY . .
RUN pip3 install -r requirements.txt

CMD python semantics.py