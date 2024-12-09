from celery import shared_task
import time
import requests
import io
from PIL import Image
from backend.config import Config
from backend.utils import get_prompt
import pathlib


@shared_task(ignore_result=False)
def generate_picture(username: str):
    headers = {"Authorization": f"Bearer {Config.API_TOKEN}"}

    def query(payload):
        response = requests.post(
            Config.API_URL,
            headers=headers,
            json=payload
        )

        return response.content

    prompt = get_prompt()

    image_bytes = query({
        "inputs": prompt,
    })

    image = Image.open(io.BytesIO(image_bytes))

    image.save(f"/home/michael/PycharmProjects/DayCard/static/{username}.jpg")

    return {"status": "ok"}


@shared_task()
def delete_pictures():

    path = pathlib.Path(f"/home/michael/PycharmProjects/DayCard/static/")
    result = [pathlib.Path.unlink(im) for im in path.glob('*.jpg')]

    return {"status": "okay"}
