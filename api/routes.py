import os

from flask import Response, jsonify, request
from flask_cors import CORS, cross_origin

from api.utils.file import get_file, root_dir


def hello_world():
    return "hello world"


@cross_origin()
def serve_file():
    if filename := request.args.get("filename"):
        try:
            content = get_file(filename)
            return Response(content, mimetype="text/html")
        except Exception:
            return jsonify(
                {
                    "These are the following files available": os.listdir(
                        "/usr/src/app/data"
                    )
                }
            )
    else:
        return "Please provide the filename query param ", 404
