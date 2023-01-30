# Currency Converter API

This project contains a Python project for convert currencies. This initial version uses Flask Framework and Fixer API to get the currencies rates data.

---

## Requirements

- Python version: 3.10+;
- Pip version: 22.0.2+;

Run the following command to install all the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

- Create a `.env` file on the repository main folder;

- Put the following variables in `.env` file:

```env
API_KEY=<your_api_key>
BASE_URL=https://api.apilayer.com/fixer/
```
You can get the free API key on this [site](https://fixer.io/).

Run the API with the command:

```bash
flask --app app run
```

The API will be running on http://127.0.0.1:5000.

---

## Example

Try the following URL on an API Platform like Postman or directly on browser:

```url
http://127.0.0.1:5000?from=BTC&to=USD&amount=1
```

You should get a result like this:

```json
{
    "msg": "success",
    "result": 22684.60
}
```