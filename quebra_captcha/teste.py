# import models
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import time
import os
import os.path
import globalconf as GC

credentials = CognitiveServicesCredentials(GC.key)
client = ComputerVisionClient(
    endpoint="https://" + GC.region + ".api.cognitive.microsoft.com/",
    credentials=credentials
)
with open(os.path.join('ajeitado', "captcha1.png"), "rb") as image_stream:
        job = client.recognize_text_in_stream(
            image=image_stream,
            mode="Printed",
            raw=True
        )
operation_id = job.headers['Operation-Location'].split('/')[-1]

image_analysis = client.get_text_operation_result(operation_id)
while image_analysis.status in ['NotStarted', 'Running']:
    time.sleep(1)
    image_analysis = client.get_text_operation_result(operation_id=operation_id)

print("Job completion is: {}\n".format(image_analysis.status))

print("Recognized:\n")
lines = image_analysis.recognition_result.lines
print(lines[0].words[0].text)  # "make"
print(lines[1].words[0].text)  # "things"
print(lines[2].words[0].text)  # "happen"
