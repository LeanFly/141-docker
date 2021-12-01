FROM python


WORKDIR /code

ENTRYPOINT [ "python" ]

EXPOSE 8000

RUN pip install lxml
RUN pip install requests
RUN pip install uvicorn
RUN pip install fastapi

CMD [ "./141.py" ]

