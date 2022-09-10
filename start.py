# Note
'''
    This script is written with codes & commands,
    according Ubuntu 20.04 so it may not be suitable for Windows or Mac.
'''


# Imports
import os
import yaml
import subprocess
import errno


# Funcs
def db_directory():

    '''
    Delete the 'example' directory if it exists, to avoid problems while building the image.
        
    The 'example' is the local db directory defined in 'docker-compose.yml => services => db => volumes'
    And if its name is something else, it will be checked and necessary action will be taken automatically.

    Note that this python script should be next to the docker-compose file
    '''
    
    # Check if docker-compose.yml exists
    if not os.path.isfile('docker-compose.yml'):
        return print("Can't find docker-compose.yml here.")

    # Read docker-compose.yml file
    with open("docker-compose.yml", 'r') as stream:
        data_loaded = yaml.safe_load(stream)
        db_dir_path = data_loaded['services']['db']['volumes'][0].split(':')[0]

    # Check if the given dir in docker-compose exists to delete it
    if os.path.isdir(db_dir_path):
        command = f"sudo -S rm -r {db_dir_path}"
        os.system(command)
        print(f'{db_dir_path} folder has been successfully deleted')
        return True
    else:
        print(f'Checking completed and there ain\'t {db_dir_path} to delete')
        return True


def check_docker_installation() -> bool:

    '''
    Check the correctness of Docker and Docker-compose installation
    '''

    def is_tool(name):
        try:
            # Try to call the command
            devnull = open(os.devnull)
            subprocess.Popen([name], stdout=devnull, stderr=devnull).communicate()
        except OSError as e:
            if e.errno == errno.ENOENT:
                return False
        return True

    if is_tool('docker') and is_tool('docker-compose'):
        return True
    return False


def main() -> None:
    if check_docker_installation():
        if db_directory() == True:
            
            # downing any container
            os.system('docker-compose down')

            # build our image
            os.system('docker-compose build')

            # remove all dangling images
            os.system('echo y|docker image prune')

            # start the container
            os.system('docker-compose up -d')

            # run migrate for django migrations
            os.system('docker-compose exec web python manage.py migrate')

            # load initial data for the project
            # os.system('docker-compose exec web python manage.py loaddata initial_data.json')
            

            print('','See => http://127.0.0.1:8000/')
            print('To stop docker-compose run "docker-compose down"')
    else:
        print('Seems that you\'ve not installed Docker on your system')


if __name__ == '__main__':
    main()
    