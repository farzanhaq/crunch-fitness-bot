FROM python:3.8

# Adding trusting keys to apt for repositories
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Adding Google Chrome to the repositories
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Updating apt to see and install Google Chrome
RUN apt-get -y update

# Magic happens
RUN apt-get install -y google-chrome-stable

# Installing Unzip
RUN apt-get install -yqq unzip

# Installing Cron
RUN apt-get install -yqq cron

# Download the Chrome Driver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip

# Unzip the Chrome Driver into /usr/local/bin directory
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

RUN chmod 755 /usr/local/bin/chromedriver

# Set display port as an environment variable
ENV DISPLAY=:99

ENV TZ=America/Toronto

COPY crunch-cron /etc/cron.d/crunch-cron

RUN chmod 644 /etc/cron.d/crunch-cron

RUN crontab /etc/cron.d/crunch-cron

RUN touch /var/log/cron.log

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD cron && tail -f /var/log/cron.log

#CMD ["python", "./main.py"]