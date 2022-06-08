FROM python:3.9

COPY . .
RUN apt-get update \
 && apt-get install -y sudo

RUN pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run"]
#CMD [ "streamlit", "run", "frontmain.py" ]
CMD ["frontmain.py"]

EXPOSE 8501