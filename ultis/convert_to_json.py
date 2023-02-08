from bson import json_util
import json

def convertToJson(data):
    return json.loads(json_util.dumps(data))