# Article Takeaway API

This is a RESTful API built with Flask that uses OpenAI and newspaper library to parse online articles and extract the top 10 takeaways. The API can be used to extract key insights and information from online articles quickly and easily.

## Endpoints

The following endpoints are available:

### `GET /article?url=<url>`
Returns the top 10 takeaways for the given article URL.

Parameters

url: The URL of the article to extract takeaways from.
### Example
#### Request:
```GET /article?url=https://www.ycombinator.com/library/89-how-to-succeed-with-a-startup-sus-2018```
#### Response:
```
{
  "title": "Example Article",
  "authors": ["John Doe"],
  "url": "https://www.example.com/article",
  "takeaways": ["Takeaway 1", "Takeaway 2", ..., "Takeaway 10"]
}
```
## Getting started

To get started with the application, clone the repository and install the dependencies:

```
$ git clone https://github.com/bekbull/nFactoiralAICup-backend.git
$ cd nFactoiralAICup-backend
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

You'll also need to set up an OpenAI API key. Once you have your API key, create a `.env` file in the project root and add the following line:

```
OPENAI_API_KEY=your-api-key
```

To run the application, use the following command:

```
$ python3 app.py
```

The application will run on `http://localhost:5000` by default.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please create a pull request or open an issue.
