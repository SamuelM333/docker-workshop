build:
	docker build -t docker-workshop:latest .

run:
	docker run --rm -p 5000:5000 --env-file .env --name microservice -d docker-workshop:latest

logs:
	docker logs -f microservice

kill:
	docker kill microservice
