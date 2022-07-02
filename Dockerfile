FROM continuumio/miniconda3

WORKDIR /app

# Create the environment:
COPY environment.yml .
RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

RUN echo "Make sure flask is installed:"
RUN python -c "import flask"


# The code to run when container is started:
COPY . .
EXPOSE 5000
# ENV FLASK_APP=server.py
# ENV FLASK_RUN_HOST=0.0.0.0
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "myenv", "python", "server.py"]
# ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "myenv", "python", "run.py"]