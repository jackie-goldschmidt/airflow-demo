# airflow-demo
Use this to demo Airflow running in a container

# Prerequisites
First install docker.

On a mac
```
brew install docker
```

Create a docker account (if necessary) and log in
```
docker login
```

# Setup
Pull the image from the docker registry
```
docker pull puckel/docker-airflow
```
Navigate into the repository
```
cd airflow-demo
```

Run the image, referencing the DAG folder. You will need to reference the folder using its absolute path.

For example:
```
docker run \
-d -p 8080:8080 \
-v /Users/jgoldschmidt/IdeaProjects/airflow-demo/dags/:/usr/local/airflow/dags \
 puckel/docker-airflow webserver
```

You can view DAGs and DAG runs using the Airflow web UI
```
http://localhost:8080/admin/
```

# Developing
To create a new DAG, place the DAG definition in the airflow-demo/dags folder and restart the container

# Testing
This is just a demo of running Airflow in a container so I haven't included tests. 
If we were to start creating real DAGs, best practice would be to 
separate out the logic run by the DAGs into functions that were tested either in a /tests directory.

# Acknowledgements
* Thank you to puckel for the docker-airflow image
* Thank you to Mark Nagelberg, the author of this [helpful article](https://towardsdatascience.com/getting-started-with-airflow-using-docker-cd8b44dbff98)
* Thank you to Manasi Dalvi for the [example dag](https://github.com/vishalsatam/Data-Pipelining/tree/master/Airflow)