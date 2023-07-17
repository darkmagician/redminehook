#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify
import logging
import jinja2
import requests
import logging.handlers
import os
import sys
from collections import defaultdict


def getENV(key, defaultVal=None):
    if defaultVal:
        return os.getenv(key, default=defaultVal)
    val = os.getenv(key)
    if val:
        return val
    raise Exception(f'env {key} is not configured')


# Environments
HTTP_PORT = getENV('HTTP_PORT', 3080)
CHANNEL_ID = getENV('CHANNEL_ID')
BOT_TOKEN = getENV('BOT_TOKEN')
TEMPLATE_ID = getENV('TEMPLATE_ID', "issue.txt")

fileLoader = jinja2.FileSystemLoader(searchpath="./templates")
environment = jinja2.Environment(loader=fileLoader)

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hook():
    try:
        templateName = TEMPLATE_ID
        template = environment.get_template(templateName)
    except jinja2.exceptions.TemplateNotFound:
        logging.info(f"{templateName} is not found.")
        return {}

    body = json.loads(request.data)
    forwardrequest = template.render(body)
    url = f"https://sandbox.api.sgroup.qq.com/channels/{CHANNEL_ID}/messages"
    print(f"{url}-> {forwardrequest}")
    r = requests.post(url, headers={"Authorization", BOT_TOKEN} json={"content": forwardrequest})

    return {}


if __name__ == '__main__':
    app.run(port=HTTP_PORT, host="0.0.0.0")
