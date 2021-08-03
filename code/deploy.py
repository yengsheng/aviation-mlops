import os
from ml_service.util.env_variables import Env

from azureml.core.model import InferenceConfig
from azureml.core import Workspace
from azureml.core.model import Model

from azureml.core.webservice import AciWebservice
from azureml.core.authentication import MsiAuthentication


def main():
    e = Env()
    model_name = 'aviation_model'
    msi_auth = MsiAuthentication()

    ws = Workspace.get(
        name=e.workspace_name,
        subscription_id=e.subscription_id,
        resource_group=e.resource_group,
        auth = msi_auth
    )
    print(ws.name, 'loaded.')

    model = Model(ws, model_name)
    inference_config = InferenceConfig(
        environment = e,
        conda_file="../AviationMLOps/conda_dependencies.yml",
        entry_script="../AviationMLOps/scoring/score.py",
    )  

    deployment_config = AciWebservice.deploy_configuration(
        cpu_cores=0.5, memory_gb=1, auth_enabled=True
    )

    service = Model.deploy(
        ws,
        "myservice",
        [model],
        inference_config,
        deployment_config,
        overwrite=True,
    )
    service.wait_for_deployment(show_output=True)

if __name__ == '__main__':
    main()