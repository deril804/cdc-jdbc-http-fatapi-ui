FROM python:3.9-slim

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
# Copy the entire project directory into the container at /app
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ../../app_fastapi /code/app



# Command to run the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]