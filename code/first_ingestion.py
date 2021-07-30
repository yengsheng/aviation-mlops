from azureml.copre import Workspace, Datastore, Dataset

def main():
    ws = Workspace.from_config()
    print(ws.name, 'loaded.')
    default_ds = ws.get_default_datastore()
    directory = './data/'
    default_ds.upload_file(file='./data/aviation_main.csv',
                        target_path = 'aviation-data/',
                        overwrite = True,
                        show_progress = True)

if __name__ == '__main__':
    main()
    
# def get_ws():
#     ws = Workspace.from_config()
#     print(ws.name, 'loaded.')
#     return ws

# def get_datastore():
#     default_ds = ws.get_default_datastore()
#     directory = './data/'

# default_ds.upload_file(file='./data/aviation_main.csv',
#                         target_path = 'aviation-data/',
#                         overwrite = True,
#                         show_progress = True)

