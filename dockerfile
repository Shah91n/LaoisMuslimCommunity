FROM python:3.9
ENV LATITUDE=53.0333
ENV LONGITUDE=-7.3000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "streamlit_app.py"]