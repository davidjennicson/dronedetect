from ultralytics import YOLO
from enum import Enum

class ModelType(Enum):
    YOLOv8n = 'yolov8n.pt'
    YOLOv8s = 'yolov8s.pt'
    YOLOv8x = 'yolov8x.pt'
    BEST='best.pt'

class Camera(Enum):
    LAPTOP = '0'


def liveObjDetection(modelType:ModelType):
    model = YOLO(modelType.value)
    model.predict(source=Camera.LAPTOP.value,show=True)

if __name__ == '__main__':
    # liveObjDetection(ModelType.YOLOv8x)
    liveObjDetection(ModelType.BEST)

# from ultralytics import YOLO
# model=YOLO('best.pt')
# results = model('bird.jpg')