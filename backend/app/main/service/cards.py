import pathlib
import json
from quopri import quote

from flask import jsonify
import os

from ..model.users import User
from ..model.cards import Quote
from backend.tasks import generate_picture
from backend.utils import get_quote


class CardsManager:

    @classmethod
    def get_all_images(cls) -> list:
        path = pathlib.Path(f"{os.getcwd()}\\static/")
        result = [str(im).split('/')[-1] for im in path.glob('*.jpg')]
        return result

    @staticmethod
    def make_wish(username: str):
        if f"{username}.jpg" in CardsManager.get_all_images():
            return None

        user = User.objects(username=username).first()
        if not user:
            return None

        quote = get_quote()

        quote_db = Quote(
            text=quote.text,
            author=quote.author
        )

        user.quote = quote_db

        user.save()

        generate_picture.delay(username)

        return True

    @staticmethod
    def get_card(username: str):

        if f"{username}.jpg" not in CardsManager.get_all_images():
            return None

        quote_db = User.objects(username=username).only('quote').first()
        if not quote_db:
            return None

        text = json.loads(quote_db.to_json()).get('quote').get('text')
        author = json.loads(quote_db.to_json()).get('quote').get('author')

        return {"image": f"{username}.jpg", "text": text, "author": author}
