import json
from flask import Flask, request

import os
from dotenv import load_dotenv

from ArticleSummary import ArticleSummary


load_dotenv()
app = Flask(__name__)


@app.route('/article', methods=['GET'])
def index():
    args = request.args
    res = ArticleSummary(
        url=args.get('url')
    )
    res.parse()

    return json.dumps({
        'title': res.title,
        'authors': res.authors,
        'url': res.url,
        'takeaways': res.takeaways
    })


if __name__ == '__main__':
    app.run(port=5000, debug=True)
