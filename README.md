# poms-django

This is the repository for the poms project at [Kings Digital Lab](https://kdl.kcl.ac.uk)

This project uses the technologies outlined in our [Technology Stack](https://stackshare.io/kings-digital-lab/django) and is configured to ~~use [Vagrant](https://www.vagrantup.com/) for local development and [Fabric](http://www.fabfile.org/)~~ to now use Docker for deployment ( see below).

## Containers:

- [nginx-proxy](https://hub.docker.com/r/nginxproxy/nginx-proxy): This is the primary entry point for the stack, running on 80.  It automatically builds a proxy to other containers.
- [django 3.2](https://hub.docker.com/layers/library/python/3.6-slim-buster/images/sha256-5dd134d6d97c67dd02e4642ab24ecbb9d23059ea018a8b5185784d29dce2f37a?context=explore): The main container for the project (see more detailed description below.) 
- [nginx](https://hub.docker.com/_/nginx): This is the static data container, serving Django's static content.
- db: The database container for Django above, running a legacy version of MySQL (5.7).
- elasticsearch [7.10](https://hub.docker.com/_/elasticsearch): The indexing container, used by Haystack 3.2.1. (Pre-migration, Haystack 2 was using Solr 6.)
- geoserver: The original VM deployment shared a geoserver with other projects.  It has now been dockerized and moved here as a standalone resource.
- postgis: The backing database container for the geoserver above.
- rdf: This container is an encapsulation of a Tomcat server running John Bradley's modified [RDF4J](https://rdf4j.org/) to provide the dataset as linked open data.  For more information, see the  at [documentation](https://poms.ac.uk/rdf/doc/index.html)


## Getting started
1. Enter the project directory: `cd poms-django`
2. Build and run the docker containers `docker compose -f compose/docker-compose.yml up -d --build`
3. Copy mysql data into the db container and ingest it via the command line if necessary.
4. **Haystack indexes are not buit during the build process**.  To build the Haystack search indexes, first log into the django container `docker compose -f compose/docker-compose.yml exec django bash`.  Then run the update_index management command: `python manage.py update_index`

You can access the site locally at [http://localhost](http://localhost)

