# start from an official image
FROM python:3.6

# arbitrary location choice: you can change the directory
RUN mkdir -p /project
WORKDIR /project

# copy our project code
COPY . /project


# install our dependencies from requirements.txt
RUN pip install -r requirements.txt

RUN cd Compendium && python manage.py collectstatic --no-input

# expose the port 8000
EXPOSE 8000


# define the default command to run when starting the container

CMD ["gunicorn", "--chdir", "Compendium", "--bind", ":8000", "Compendium.wsgi:application"]


