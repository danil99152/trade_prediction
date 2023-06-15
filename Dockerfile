FROM python:3.11.4

ADD ./trade_prediction ./trade_prediction

RUN pip3.11 install -r ./trade_prediction/requirements.txt

ADD ./contracts.csv ./contracts.csv

CMD python ./trade_prediction/main.py
