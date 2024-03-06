import base64
import json

ENVSPECIFIC_VARS='<Replace-with-env-variables>'
ENVSPECIFIC_VARS_JSON = json.loads(  base64.b64decode( ENVSPECIFIC_VARS ) )

with open('ENVSPECIFIC_VARS_JSON.json', 'w') as f:
    json.dump(ENVSPECIFIC_VARS_JSON, f, indent=2)
