from azureml.core import Workspace, Datastore, Dataset
from ml_service.util.env_variables import Env

def main():
    e = Env()

    ws = Workspace.get(
        name=e.workspace_name,
        subscription_id=e.subscription_id,
        resource_group=e.resource_group,
    )
    print(ws.name, 'loaded.')