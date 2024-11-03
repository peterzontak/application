# Depends on global whitenoise && dj_database_url!!!
import shutil
import subprocess
import os


def run_command(_command: list):
    # Start the subprocess and capture output
    try:
        process = subprocess.run(_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

        # Print the standard output
        if process.stdout:
            print(process.stdout.strip())
            print('Done!')

        # Print any errors
        if process.stderr:
            print(process.stderr.strip())
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    input("Press Enter to continue...")


def copy_file(_source_file: str, _destination_file: str):
    try:
        os.makedirs(os.path.dirname(_destination_file), exist_ok=True)
        shutil.copy(_source_file, _destination_file)
        print(f"Copied {_source_file} to {_destination_file}")
    except FileNotFoundError as fnf_error:
        print(f"File not found: {fnf_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def copy_dir(_source_dir: str, _destination_dir: str):
    try:
        os.makedirs(_destination_dir, exist_ok=True)
        shutil.copytree(_source_dir, _destination_dir, dirs_exist_ok=True)
    except FileNotFoundError as fnf_error:
        print(f"File not found: {fnf_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


try:
    # Cache configuration
    source_file = '../config/config.json'
    destination_file = './config/config.json'
    copy_file(source_file, destination_file)
    
    source_file = '../../poznamky'
    destination_file = './config/poznamky'
    copy_dir(source_file, destination_file)
    
    
    command = ['python', 'manage.py', 'collectstatic', '--noinput']
    run_command(command)
    # subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    
except FileNotFoundError as fnf_error:
    print(f"File not found: {fnf_error}")
except subprocess.CalledProcessError as cpe:
    print(f"Error during collectstatic: {cpe.stderr}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
