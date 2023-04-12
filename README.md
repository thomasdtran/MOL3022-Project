# Predicting Secondary Structures of Proteins Using a Feed-Forward Neural Network Model
Welcome to the repository for my project in MOL3022 - Bioinformatics - Method Oriented Project Predicting. It contains the source code for the implementation of a Feed-Forward Neural Network trained to predict the secondary structure of proteins, as well as the web application to test out the model and its predictions.

## Authors
Thomas Tran - ttdtran@stud.ntnu.no

## Getting started

The repository consists of two main folders, ```frontend``` which contains the source code for the web applcation, and ```backend``` which contains the necessary scripts to train and load the network, as well as the REST API for the web application. 

### Frontend

To spin up the site locally, you have to run the following commands from the `frontend` directory:

```
npm install
npm run dev
```

The site will be running on [http://localhost:8080].

### Backend

The backend consists of two parts: The Feed-Forward Neural Network and the REST API.

#### Feed-Forward Neural Network

##### Setup
Run the following command in the `backend` folder to install the necessary dependencies to train the model:

```pip install -r requirements.txt```

##### Training

(**NOTE:** There is already trained model saved in the folder `saved_model`, if you dont want to retrain the model.)

In order to train the model, run the following command:

```python train.py```

There is a `.env` file with variables for `WINDOW_SIZE`, `ACCURACY_THRESHOLD`, `PATH_TRAIN_DATA`, `PATH_TEST_DATA`. Change these as needed. If there is a need to change and experiment with the parameters for the actual network, you can go to the `FNN.py` file and change them there.

#### REST API

To spin up the API locally, run the following command from the `backend` folder:

`flask --app endpoints run`

The API will be running on [http://127.0.0.1:5000].




