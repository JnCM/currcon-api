# Currency Converter API

This project contains a Python project for convert currencies. This version uses Django and Django REST Framework for API architecture and BeautifulSoup to scrap the Google Finance website in search of currencies quotes.

---

## Requirements

- Python version: 3.10+;
- Pip version: 22.0.2+;

Run the following command to install all required dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

This version doesn't need previous configuration, just go on `manage.py` root directory and type the command to start the project:

```bash
python manage.py runserver
```

The project will be running on http://127.0.0.1:8000 .

---

## Documentation

Go to [Swagger](http://127.0.0.1:8000/swagger) or [Redoc](http://127.0.0.1:8000/redoc) documentation with the project running for more infos and examples of API usage.

---

## References

- [Django docs](https://docs.djangoproject.com/en/4.1/);
- [Django REST Framework docs](https://www.django-rest-framework.org/);
- [Swagger Generator docs](https://drf-yasg.readthedocs.io/en/stable/readme.html);
- [BeautifulSoup docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).
