import io
import zipfile
import requests
import time
import os
import json
import pprint
from dotenv import load_dotenv

def read_config_file(config_file):
  """
  Reads configuration file and returns the configuration as a dictionary.
  """

  with open(config_file, "r") as f:
    config = json.load(f)

  return config

def main():
  """
  Reads configuration and starts the process of creating a new layer in GeoServer.
  """

  # Load environment variables
  load_dotenv()
  config_file = os.getenv("CONFIG_FILE")
  # Read configuration
  config = read_config_file(config_file)
  GEOSERVER_USER = os.getenv("GEOSERVER_USER")
  GEOSERVER_PW = os.getenv("GEOSERVER_PW")
  GS_URL = config["geo_server"]["url"]


if __name__ == "__main__":
  start_time = time.time()

  main()
  pprint.pp(f"Completed in {(time.time() - start_time):.2f} seconds")
