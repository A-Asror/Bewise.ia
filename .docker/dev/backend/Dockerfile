FROM --platform=linux/amd64 python:3.11.0

# Set up Python behaviour
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV VIRTUAL_ENV=/opt/venv

# Install system dependencies
RUN apt-get update -y \
  && apt-get install -y netcat gcc postgresql vim

# Switch on virtual environment
ENV HOME=/home/app
ENV APP_HOME=/home/backend
ENV VIRTUAL_ENV=/home/backend/venv
RUN mkdir $HOME
RUN mkdir $APP_HOME
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Set the working directory
WORKDIR $APP_HOME

# Copy all files
COPY ./ ./

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r backend/requirements/dev.txt

RUN chmod +x $APP_HOME/.docker/dev/backend/entrypoint.sh

# Execute entrypoint.sh
ENTRYPOINT ["/home/backend/.docker/dev/backend/entrypoint.sh" ]

# Start up the backend server
CMD uvicorn backend.main:backend_app --reload --workers 4 --host 0.0.0.0 --port 8000
