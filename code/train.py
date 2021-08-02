from azureml.core import Workspace, Datastore, Dataset
from ml_service.util.env_variables import Env
from azureml.core import Experiment
from azureml.core import Model
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from azureml.core.model import Model

def main():
    e = Env()
    model_name = 'aviation_model'

    ws = Workspace.get(
        name=e.workspace_name,
        subscription_id=e.subscription_id,
        resource_group=e.resource_group,
    )
    print(ws.name, 'loaded.')

    experiment = Experiment(workspace=ws, name="aviation-experiment")
    run = experiment.start_logging()
    print("Starting experiment:", experiment.name)

    #Retrieving current model
    model = ws.models['classification_model']
    print(model)

    model = ws.models[model_name]
    print(model)

    # # Load dataset
    # dataset = Dataset.get_by_name(ws, name='main').to_pandas_dataframe()
    # # Dataset loaded

    # # Separate features and labels
    # X, y = dataset[['Investigation.Type','Country','Injury.Severity','Amateur.Built','Number.of.Engines','Total.Fatal.Injuries','Total.Serious.Injuries','Total.Minor.Injuries', 'Total.Uninjured']].values, dataset['Aircraft.damage'].values

    # # Split data into training set and test set
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

    # # Train a decision tree model
    # print('Training a decision tree model')
    # model = DecisionTreeClassifier().fit(X_train, y_train)

    # # calculate accuracy
    # y_hat = model.predict(X_test)
    # acc = np.average(y_hat == y_test)
    # print('Accuracy:', acc)
    # run.log('Accuracy', np.float(acc))

    # # calculate AUC
    # y_scores = model.predict_proba(X_test)
    # auc = roc_auc_score(y_test,y_scores[:,1])
    # print('AUC: ' + str(auc))
    # run.log('AUC', np.float(auc))

    # # Save the trained model
    # model_file = 'aviation_model.pkl'
    # joblib.dump(value=model, filename=model_file)
    # run.upload_file(name = 'outputs/' + model_file, path_or_stream = './' + model_file)

    # # Complete the run
    # run.complete()

    # # Register the model
    # run.register_model(model_path='outputs/aviation_model.pkl', model_name='aviation_model',
    #                 tags={'Training context':'Inline Training'},
    #                 properties={'AUC': run.get_metrics()['AUC'], 'Accuracy': run.get_metrics()['Accuracy']})
    # print('Model trained and registered')

if __name__ == '__main__':
    main()