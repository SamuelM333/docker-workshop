https://docs.docker.com/compose/

```bash
make build
make run
docker ps
make logs
curl localhost:5000
curl -X POST -H "Content-Type: application/json" -d '{"username":"abc","email":"abc"}' localhost:5000/user
curl localhost:5000/user
```
