import time
from flask import Flask, request, jsonify
from yolov8_inference.model import YOLOv8
from yolov8_inference.utils import readb64
from werkzeug.exceptions import BadRequest, InternalServerError
import io
import base64
import uuid
import os
from constant import LabelMap
from loguru import logger
import json

TEMPLATE_JSON = {
    "job": {
        "id": "",
        "result": {
            "status": "success",
            "analytic_type": "Vehicle Detection",
            "result": []
        }
    },
    "message": "Vehicle Detection Success",
    "ok": True
}
MODEL_PATH = os.getenv("MODEL_PATH")

supported_mimetypes = ["image/jpeg", "image/png"]
app = Flask(__name__)
model = YOLOv8(path=MODEL_PATH, labels_dict=LabelMap.VEHICLE_MAPS)

@app.errorhandler(BadRequest)
def bad_request_handler(error):
    return {
        "error": error.description
    }, 400

@app.errorhandler(InternalServerError)
def internal_server_error_handler(error):
    return {
        "error": error.description
    }, 500

def unpack_base64_string_img(img):
    data = img.split(":")
    mimetype = None
    if len(data) == 1:
        return mimetype, io.BytesIO(base64.b64decode(data[0]))
    else:
        mimetype, image = data[1].split(";")
        image = image.split(',')
        return mimetype, io.BytesIO(base64.b64decode(image[1]))

@app.route("/predict", methods=['POST'])
def predict():
    data = dict(request.json)
    id1 = uuid.uuid1().hex
    id2 = uuid.uuid1().hex
    job_id = id1 + id2
    template_json = TEMPLATE_JSON
    template_json["job"]["id"] = job_id
    logger.info(f"Processing detection with job id : {job_id}")
    start_time = time.time()
    img = readb64(data["images"][0])
    final_results = model(img)
    template_json["job"]["result"]["result"] = final_results
    end_time = time.time()
    inference_time = '{:3f}'.format(end_time - start_time)
    logger.info(f"Job {job_id} finished. Inference time {inference_time}")
    logger.info(f"Results {template_json}")
    return json.dumps(template_json)
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8888")
