import openai
import os
from dotenv import load_dotenv

from newspaper import Article


class ArticleSummary:
    def __init__(self, url):
        self.title = ''
        self.authors = []
        self.url = url
        self.takeaways = []
        self.openai_api()

    def parse(self):
        article = Article(self.url)
        article.download()
        article.parse()

        self.title = article.title
        self.authors = article.authors
        self.text = article.text
        self.takeaways = self.generate_text(self.text)

    def openai_api(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def text_generator(self, prompt, model):
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.choices[0].message.content

    def generate_text(self, text):
        prompt = "I need top 10 takeaways from this text: \n" + text + \
            "\n Do not write 'Sure, these are the takeaways:'. Write the takeaways with numbered bullet points."
        generated_text = list(filter(bool, self.text_generator(
            prompt, "gpt-3.5-turbo").splitlines()))
        return generated_text
