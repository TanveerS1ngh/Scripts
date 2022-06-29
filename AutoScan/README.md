# Docker + kali usage

```bash
# Build simple kali image with mounted /kali dir
docker-compose build

# Run default script within container (Autoscan.sh)
docker-compose run kali

# Run a raw bash within kali container
docker-compose run kali bash
```
