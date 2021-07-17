# Google Cloud Function Course

## Starting a project
to start a new project in Google Cloud, we can go to the [Firebase Console](https://console.firebase.google.com) or we can create it from [Google Cloud Platform Link](https://console.cloud.google.com)

## Creating a Virtual Environment
First we have to install `python3-venv` with the following command
```
pip install python3-venv
```
Then we execute the following command
```
python -m venv venv
```
We activate the virtual enviroment using the following command
```
cd venv/Scripts/activate
```

In order to add new packages to our new virtual environment, we create a file called `requirements.txt` and execute the following command
```
pip install -r requirements.txt
```
## First Cloud function
We create a new directory called `helloworld`, In that directory we make a new python file called `main.py`. The name of the file must be that. Then we write the following code:
```python
def hello_world(request): 

    # this will return a dictionary
    request_args = request.args  


    '''
If the dictionary returned is not empty, its going to look for key `name`
    '''
    if request_args and 'name' in request_args:
        name = request_args['name']
    else: 
        name = 'World'

    return f"Hello {name}"

```

In order to run the function we will type the following command, but first we have to go to the `helloworld` folder. We then type the following command in the terminal/cmd
```
functions-framework --target hello_world
```
`hello_world` is the name of the function in `main.py`

## Deploying our function
There are a few things we have to do before we can deply
- First we have to make sure that we have [GoogleSDK](https://cloud.google.com/sdk/docs/quickstart) installed 
- We then have initiate the gcloud by using the following command
```
gcloud init
```
You can see all your projects in your google cloud by the following command
```
gcloud projects list
```
We then have to set our project ID with the following command
```
gcloud config set project [YOUR_PROJECT_ID]
```
We deploy our function with this command
```
gcloud functions deploy [FUNCTION NAME] --runtime python37 --trigger-http
```