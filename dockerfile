FROM python:3.9
WORKDIR /app
COPY . .
# Additional setup steps if needed
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
