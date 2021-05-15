import argparse
import yaml

from objects import Deduplicator
from error_handler import ServiceNotFoundError

parser = argparse.ArgumentParser()
parser.add_argument('-c','--config', help = 'include config file')
args   = parser.parse_args()

CONFIG_FILE = args.config

def parse_config():
    path        = '/tmp/config/{}'.format(CONFIG_FILE)
    config      = yaml.load(open(path,'r'), Loader=yaml.FullLoader)
    service     = config['service']
    input_data  = config['input_data']
    output      = config['output']

    # appending /tmp/inputs to the input_data files
    input_data = ['/tmp/inputs/{}'.format(path) for path in input_data]

    return service, input_data, output

def run_service(deduplicator, service, output):
    success   = True
    error     = None
    save_path = '/tmp/outputs/{}'.format(output)

    if service == 'get_new_rows':
        df = deduplicator.get_new_rows()
    elif service == 'dedupe_single_df':
        df = deduplicator.dedupe_single_df()
    else:
        success = False
        error   = ServiceNotFoundError(service).message

    if success:
        df.to_csv(save_path, index=False)
        
    return {'success'  : success,
            'error'    : error,
            'save_path': save_path}

def process_data():
    service, input_data, output = parse_config()
    deduplicator = Deduplicator(input_data)
    print('**************************************')
    print('Running {} for {}'.format(service, input_data))
    status = run_service(deduplicator, service, output)
    if status['success']:
        print('Success! Output file located in /outputs/{}'.format(output))
    else:
        print('Error: {}'.format(status['error']))
    print('**************************************')

if __name__ == '__main__':
    process_data()