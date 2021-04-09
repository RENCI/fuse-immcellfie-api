import os

from flask import Response, jsonify, request
from flask_cors import CORS, cross_origin
import requests

from api.utils.file import get_file, root_dir

IMMCELLFIE_HOST = os.getenv("IMMCELLFIE_HOST", "localhost")
IMMCELLFIE_PORT = os.getenv("IMMCELLFIE_PORT", "8080")
IMMCELLFIE_VERSION = os.getenv("IMMCELLFIE_VERSION", "v1")


def hello_world():
    return "hello world"


@cross_origin()
def serve_file():
    analysis_url = f"http://{IMMCELLFIE_HOST}:{IMMCELLFIE_PORT}/{IMMCELLFIE_VERSION}/plugin/fuse-analysis-cellfie/analysis"
    if filename := request.args.get("filename"):
        response = requests.get(f"{analysis_url}?filename={filename}")
        return Response(response.text, mimetype="text/html")
    else:
        return "Please provide the filename query param ", 400
    # if filename := request.args.get("filename"):
    #     try:
    #         content = get_file(filename)
    #         return Response(content, mimetype="text/html")
    #     except Exception:
    #         return jsonify(
    #             {
    #                 "These are the following files available": os.listdir(
    #                     "/usr/src/app/data"
    #                 )
    #             }
    #         )
    # else:
    #     return "Please provide the filename query param ", 404
