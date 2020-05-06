## Azure-Function-IoT_to_Cosmos

As there is no way to directly use Stream Analytic and Functions triggers to output data to Cosmos DB with Mongo API, a mongodb driver is needed to this situation.

This python scripts uses a simple way to monitor data arrival from IoT Hub build-in Event Hub endpoint (Azure Functions Event Hub / IoT Hub Trigger) and use mongodb driver to write data to cosmos DB.

## Tips:
- The data from event hub is list data format, therefore, covert to dict is a must before write to Cosmos DB
- The Cosmos DB mongo connection string should add "&retrywrites=false" in the end

## How to use:
- Follow this page to set your local testing environment: [Link](https://docs.microsoft.com/en-us/azure/developer/python/tutorial-vs-code-serverless-python-01)
- In your folder root, will be a file named "local.setting.json", add "EventHub_ConnectionString":{Eventhub_ConnectionString} in "Values"
- Replace your "MongoDB Uri" in "__init__.py"
- Replace your "eventHubName" in functions.json

