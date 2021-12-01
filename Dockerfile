FROM python


WORKDIR /code

ENTRYPOINT [ "python" ]

EXPOSE 8000

RUN pip install lxml
RUN pip install requests
RUN pip install uvicorn
RUN pip install fastapi

RUN curl -O https://raw.githubusercontent.com/LeanFly/141-docker/main/141.py

CMD [ "./141.py" ]

