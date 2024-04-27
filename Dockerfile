# This sets up the container with Python 3.10 installed.
FROM python:latest

# copies everything in current directory to the container /app .
COPY . /app

# sets the /app directory as the working directory
WORKDIR /app

# install for all the packages inside requirements.txt file.
RUN pip3 install -r requirements.txt

# Expose the port to run Streamlit
EXPOSE 8501

# run streamlit app.py script when the container starts.
CMD ["streamlit","run","app.py"]

