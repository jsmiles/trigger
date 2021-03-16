# trigger
This project is an example of how to run a Data Pipeline using Airflow and Docker


## Scenario
You are a diligent data scientist who has a customer that enjoys data summaries and Chuck Norris jokes. Your job is to provide a daily profit report. Puns help them digest the sometimes difficult news. There is a daily sales count file you can use (raw_data.csv) but in order to calculate total daily profit for the report you require another file (ref.csv)


# Files
- __docker-compose.yml__ this is the docker configuration file used to create my containers. I used the [puckel docker/airflow](https://github.com/puckel/docker-airflow/blob/master/docker-compose-LocalExecutor.yml) configuration file heavily as its now almost standard. I added an extra volume to take account of the complicated file structure I need for my pipeline (i.e. dir/ and the subdirectories) 
- __airflow.cfg__ the airflow confirguration file to allow airflow to work within my container. This again is taken from [puckel](https://github.com/puckel/docker-airflow/blob/master/config/airflow.cfg)
- __dag.py__ the Directed Acyclic Graph I have used to bring together my thress process
- __pr1.py__ this python job: reads the raw and reference data, merges and munges then calculates the quantity of interest and writes it to an output file constituting the first part of your report 
- __pr2.py__ this job reads a [Chuck Norris API](https://api.chucknorris.io/jokes/) and then writes that joke to the report
- __pr3.py__ this job cleans up the raw files directory, renames and moves them to a processed file directory
- __ref.csv__ this file contains reference data needed to make the calculations required
- __raw_data.csv__ the raw sales file has a count value per product ID sold
- __holder.txt__ a holder file



# Replication
If you would like to run this project for yourself make sure you have the following dependencies, follow the steps and be aware of the warning below. 

## Dependencies
1. Ensure you have [Docker](https://www.docker.com/get-started) downloaded 
2. You also need [Docker Compose](https://docs.docker.com/compose/install/)


## Steps
1. CD into a new directory and run `git clone https://github.com/jsmiles/trigger.git`
2. Now start your containers by running `docker-compose up -d`
3. After this check to make sure both containers are up by running `docker ps` you should see two containers, one for the webserver (puckel/docker) and one for the database (postgres)
4. You should now be able to open http://localhost:8080/admin/ and the airflow portal should be open with a single job, *Python_DAG*
5. Toggle the button to on and job should run
6. When finished dont forget to close your containers with `docker-compose down`

When the job is complete you should have a new output file in *output_dir* and the raw data file should now be located in the *processed_dir*


**Note:** if you run this workflow, it will only run once because there is only a single *raw_data* file
