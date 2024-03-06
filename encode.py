import base64
import json
data = json.load(open('ENVSPECIFIC_VARS_JSON.json', 'r'))
result = base64.b64encode(json.dumps(data).encode())
open('ENVSPECIFIC_VARS_JSON.txt', "w").write(str(result))
