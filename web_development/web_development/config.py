from dotenv import load_dotenv
from pathlib import Path
import os
import json


class CredentialLoader:
    def __init__(self, str_env='local'):
        str_working_directory = os.getcwd()
        str_config_file_path = os.path.join(str_working_directory, 'config', '.env.' + str(str_env))

        dotenv_path = Path(str_config_file_path)
        load_dotenv(dotenv_path)
        self.configData = {
            "PIPELINE_ENV": os.getenv("PIPELINE_ENV", "local"),
            "DB_HOST": os.getenv("DB_HOST", ""),
            "DB_PORT": os.getenv("DB_PORT", ""),
            "DB_USERNAME": os.getenv("DB_USERNAME", ""),
            "DB_NAME": os.getenv("DB_NAME", ""),
            "DB_PASSWORD": os.getenv("DB_PASSWORD", ""),
            "AUTO_RELOAD": True if str(os.getenv("AUTO_RELOAD", "")).lower() == 'true' else False
        }

    def set_config(self):
        os.environ["config_data"] = json.dumps(self.configData)
