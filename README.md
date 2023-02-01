# Currency Converter API

This project contains a Python project for convert currencies. This version uses Django and Django REST Framework for API architecture and BeautifulSoup to scraping the Google Finance website in search of currencies quotes.

---

## Versions used

- Linux Ubuntu 22.04.1 LTS;
- Docker 20.10.23+;
- Python 3.10.6+;
- Pip 22.0.2+;

---

## Usage

This version doesn't need previous configuration, you just need build the docker image and run a container. To build the docker image, type the following command on the same folder as `Dockerfile`:

```bash
docker build -t currapi-docker .
```

After this, to start the image inside a container, type the command:

```bash
docker run -p 8000:8000 --name api-server currapi-docker
```

The project will be running on http://127.0.0.1:8000 .

`Obs.:` Depending of your docker installation and configuration, all commands will need the `sudo` flag.

---

## Documentation

Go to [Swagger](http://127.0.0.1:8000/swagger) or [Redoc](http://127.0.0.1:8000/redoc) documentation while the project running for more infos and examples of API usage.

---

## References

- [BeautifulSoup docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/);
- [Django docs](https://docs.djangoproject.com/en/4.1/);
- [Django REST Framework docs](https://www.django-rest-framework.org/);
- [Docker docs](https://docs.docker.com/);
- [Swagger Generator docs](https://drf-yasg.readthedocs.io/en/stable/readme.html).
