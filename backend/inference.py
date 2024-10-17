from backend.model import YOLOModel


def predict_bounding_boxes(image_url):
    # Download the image from URL
    image = download_image(image_url)

    # Load YOLO model and get predictions
    model = YOLOModel()
    results = model.predict(image)

    # Format predictions for Label Studio
    predictions = []
    for box in results:
        x_min, y_min, x_max, y_max, conf = box[:5]
        predictions.append({
            "from_name": "bbox",
            "to_name": "image",
            "type": "rectanglelabels",
            "value": {
                "x": x_min,
                "y": y_min,
                "width": x_max - x_min,
                "height": y_max - y_min,
            },
            "score": conf
        })
    return predictions
