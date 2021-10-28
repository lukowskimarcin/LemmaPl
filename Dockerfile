FROM ipipan/langtools-all

WORKDIR /root/lemmapl

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "./app.py"]