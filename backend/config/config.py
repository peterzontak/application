import os
import json

def load_config():
    current_script_directory = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_script_directory, 'config.json')
    
    try:
        with open(config_path, 'r', encoding='utf-8') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        print(f"Configuration file not found at: {config_path}")
    except json.JSONDecodeError:
        print("Error decoding JSON from the configuration file.")

    return None


# if __name__ == "__main__":
#     config_data = load_config()
#     if config_data is not None:
#         print(config_data)
