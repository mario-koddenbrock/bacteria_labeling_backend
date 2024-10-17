from label_studio_ml import LabelStudioMLBase
from backend.model import YOLOModel

class BacteriaDetection(YOLOModel):
    pass

if __name__ == "__main__":
    BacteriaDetection().run(host='0.0.0.0', port=9090)
