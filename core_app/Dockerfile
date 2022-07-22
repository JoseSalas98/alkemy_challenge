FROM python:3.10
WORKDIR /core_app
RUN mkdir /core_app/sql_script
RUN mkdir /dataset
RUN mkdir /dataset/out_dataset
RUN mkdir /dataset/log
ADD requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip
RUN pip install --default-timeout=100 future -r requirements.txt
ADD .env .env
ADD confi.py confi.py
ADD constans.py constans.py
ADD db_connect_script.py db_connect_script.py
ADD lets_connet.py lets_connet.py
ADD lets_scrap.py lets_scrap.py
ADD main.py main.py
ADD sql_script/ /core_app/sql_script
CMD ["python3", "main.py"]