# CrewGo

This repositery is an answer to this exercice : https://github.com/crewdotwork/backend-challenge

Testing the script is easy :

## Option 1 : using Dockefile

We can start by running the following command (same folder as the Dockefile): 

    docker build . -t crewpython

    docker run -p 1111:1005 -d crewpython

## Option 2 : using Docker Compose File

We can run the following command (same folder as the Dockefile): 

    docker-compose up -d