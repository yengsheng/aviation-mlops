import os
from ml_service.util.env_variables import Env

from azureml.core.webservice import AciWebservice
from azureml.core.model import InferenceConfig
from azureml.core.model import Model
from azureml.core import Workspace

def main():
    e = Env()

    ws = Workspace.get(
        name=e.workspace_name,
        subscription_id=e.subscription_id,
        resource_group=e.resource_group
    )

    # Set path for scoring script and environment files
    script_file = os.path.join("./code/exp_folder", "score.py")
    env_file = os.path.join("./code/exp_folder", "env.yml")

    # Configure the scoring environment
    inference_config = InferenceConfig(runtime= "python",
                                    entry_script=script_file,
                                    conda_file=env_file)

    deployment_config = AciWebservice.deploy_configuration(cpu_cores = 1, memory_gb = 1)

    service_name = "aviation-service"
    model_name = "aviation_model"
    model = ws.models[model_name]
    print(model.name, 'version', model.version)

    service = Model.deploy(ws, service_name, [model], inference_config, deployment_config)

    service.wait_for_deployment(True)
    print(service.state)

    print(service.get_logs())


if __name__ == '__main__':
    main()