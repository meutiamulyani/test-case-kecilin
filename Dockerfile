# This sets up the container with Python 3.10 installed.
FROM python:latest

# This copies everything in your current directory to the /app directory in the container.
COPY . /app

# This sets the /app directory as the working directory for any RUN, CMD, ENTRYPOINT, or COPY instructions that follow.
WORKDIR /app

# This runs pip install for all the packages listed in your requirements.txt file.
RUN pip3 install -r requirements.txt

# This command tells Streamlit to run your app.py script when the container starts.
CMD ["streamlit","run","app.py"]