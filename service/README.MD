# Vehicle Detection Service
## Model Information
- [Experiment Logs](https://wandb.ai/hklard/vehicle_yolo_v8/runs/p5bh9hu2?workspace=user-hklard)
- [Artifact URL](https://wandb.ai/hklard/vehicle_yolo_v8/artifacts/model/vehicle-yolov8-model/dd010a7d1d589e1144fa/files)

## How to Use?

### Install and Run Docker container
You can simply up this service using this command
```bash
docker compose up -d

or 
docker-compose up -d
```

### Request Format
Example Request Format
```json
{
    "images": ["base64image"]
}
```

### Response
```json
{
  "job": {
    "id": "4d62c5c6194711ee9db30242ac1200024d62d7aa194711ee9db30242ac120002",
    "result": {
      "status": "success",
      "analytic_type": "Vehicle Detection",
      "result": [
        {
          "bbox": [
            385,
            337,
            508,
            482
          ],
          "score": 0.9311,
          "label": "Van"
        },
        {
          "bbox": [
            615,
            202,
            689,
            260
          ],
          "score": 0.9208,
          "label": "MPV/SUV"
        },
        {
          "bbox": [
            0,
            182,
            54,
            238
          ],
          "score": 0.913,
          "label": "MPV/SUV"
        },
        {
          "bbox": [
            176,
            417,
            301,
            497
          ],
          "score": 0.9113,
          "label": "MPV/SUV"
        },
        {
          "bbox": [
            216,
            166,
            279,
            226
          ],
          "score": 0.8874,
          "label": "MPV/SUV"
        },
        {
          "bbox": [
            564,
            134,
            622,
            197
          ],
          "score": 0.7906,
          "label": "Van"
        },
        {
          "bbox": [
            212,
            228,
            298,
            314
          ],
          "score": 0.7225,
          "label": "MPV/SUV"
        },
        {
          "bbox": [
            454,
            90,
            498,
            129
          ],
          "score": 0.7207,
          "label": "MPV/SUV"
        }
      ]
    }
  },
  "message": "Vehicle Detection Success",
  "ok": true
}
```