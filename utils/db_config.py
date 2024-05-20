import base64, json

class DatabaseConfig():
    def encoder(self, data):
        """ Encode JSON to base64
        data: JSON Data
        return base64 encoded string
        """
        base64.b64encode(json.dumps(data).encode())
        return base64.b64encode(json.dumps(data).encode())

    def decoder(self, data):
        """ Encode base64 to JSON
        data: base64 encode string
        :return json_obj for base64
        """
        return json.loads(base64.b64decode(data))
    def __init__(self):
        self.db_name = None
        self.db_user = None
        self.db_password = None
        self.db_host = None
        self.db_port = None

        self.base_variables = {
            "ENVIRONMENT": "staging",
            "DYNAMODB_PROCESS_TABLE": "CsApp-DL-Process-Staging-1",
            "SAGEMAKER_MODEL": "dl-app-Staging-v2-model-v1-dt-20210926-072436",
            "GCP_ENDPOINT_ID": "5279634934254796800",
            "DATABASE_ENGINE": "postgres",
            "ETL_DATABASE_USER": "bandwidth-crm_ro-tmpusr-1675076495-B9ijoML9",
            "ETL_DATABASE_PASSWORD": "BG9xbK9nVWA5h5OXE3M-",
            "ETL_DATABASE_ENGINE": "postgres",
            "ETL_DATABASE_HOST": "localhost",
            "ETL_DATABASE_PORT": 5432,
            "ETL_DATABASE_NAME": "bandwidth",
            "SSLMODE": "verify-full",
            "DYNAMODB_LOG_TABLE": "CSApp-Staging-logs",
            "NOTIFICATIONS_TO_EMAIL": "reports@emtropylabs.com",
            "STITCH_API_KEY": "at_decd30dc7e103b011c7e677af795ee8b",
            "SLACK_WEBHOOK_URL": "https://hooks.slack.com/services/TGANTDR7F/B01we23Z51/w98wewefVFG1eti664FWpO",
            "HOST_NAME": "https://csapi-qa.supportlogic.io/",
            "PROCESS_DYNAMODB_TABLE": "CsApp-DL-Process-Staging-v22",
            "ARCHIVE_DYNAMODB_TABLE": "Staging_Data_Archive",
            "LOAD_TOPIC_NAME": "dlprocess-load-staging",
            "OUTPUT_TOPIC_SUB_NAME": "dlprocess-output-staging-sub",
            "SNOWFLAKE_USER": "EP_TRANSFORMER_USER",
            "SNOWFLAKE_DATABASE": "temp_db",
            "SNOWFLAKE_PRIVATE_KEY": "d2Vmd2Vmd2Vm",
            "SNOWFLAKE_ACCOUNT": "temp_key",
            "SNOWFLAKE_WAREHOUSE": "temp_key",
            "REDIS_URL": "redis://redis:6379/7",
            "CELERY_REDIS_URL": "redis://redis:6379/6",
            "AUTH_REDIS_URL": "redis://redis:6379/0",
            "CELERY_RESULT_BACKEND": "redis://redis:6379/7"
        }
    def generate_env_variables(self):
        self.db_name = self.get_valid_input("Input database name (min 3 characters): ", 3)
        self.db_user = self.get_valid_input("Input database user (min 3 characters): ", 3)
        self.db_password = self.get_valid_input("Input database password (min 6 characters): ", 4)
        self.db_host = self.get_valid_input("Input database host (min 3 characters): ", 3)
        self.db_port = self.get_valid_port("Input database port (1-65535): ")
        self.base_variables["DATABASE_USER"] = self.db_user
        self.base_variables["DATABASE_PASSWORD"] = self.db_password
        self.base_variables["DATABASE_HOST"] = self.db_host
        self.base_variables["DATABASE_PORT"] = self.db_port
        self.base_variables["DATABASE_NAME"] = self.db_name
        print (self.encoder(self.base_variables))

    def get_valid_input(self, prompt, min_length):
        """ Generic function to check if proper input is passed with minimum length"""
        while True:
            value = input(prompt).strip()
            if len(value) >= min_length:
                return value
            else:
                print(f"Error: Input must be at least {min_length} characters long. Please try again.")

    def get_valid_port(self, prompt):
        while True:
            value = input(prompt).strip()
            if value.isdigit():
                port = int(value)
                if 1 <= port <= 65535:
                    return port
                else:
                    print("Error: Port must be between 1 and 65535. Please try again.")
            else:
                print("Error: Port must be a number. Please try again.")


# Create an instance of DatabaseConfig to execute the input and validation
db_config = DatabaseConfig().generate_env_variables()

