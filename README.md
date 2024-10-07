# E-Health-Care
The web app aims to reduce reliance on doctors by providing accessible medical checkups for underprivileged individuals and helping people avoid unnecessary expenses. This project is built using Django, along with machine learning algorithms and deep learning techniques, including ANN and CNN.
## Overview
IToday, there is a significant shortage of doctors worldwide, particularly in Nepal. Many individuals suffer due to a lack of access to proper medical checkups, and numerous cases lead to death because timely medical attention is not available. This app is designed to address these issues and provide substantial benefits in overcoming these challenges.
## Demo
![Image of project demo](https://github.com/Pradip-p/E-Health-Care/blob/master/media/images/Screenshot%20from%202021-02-07%2009-31-31.png)
## Application
* Eliminate reliance on doctors for basic medical needs.
* Provide free medical checkups to those in need.
* Help individuals avoid unnecessary medical expenses.
* Enhance the role of technology in healthcare.

<hr>
<h3> Down below are the names of the various model files used:</h3>
<ul>
<li><p><b>Heart model = pickle_model_heart.pkl</b></p></li>
<li><p><b>Diabetes model = pickle_model_diabetes.pkl</b></p></li>
<li><p><b> pneumonia model = pickle_model_pneumonia.pkl</b></p></li>
<li><p><b>Disease model = pickle_model_disease.pkl</b></p></li>
</ul>
<hr>

<h3> Kernals used for training deep learning model </h3>
<ul>
<li><p><b>Kernal for Malaria model :</b>https://www.kaggle.com/shobhit18th/malaria-cell</p></li>

<li><p><b>Kernal for Pneumonia model :</b>https://www.kaggle.com/shobhit18th/keras-nn-x-ray-predict-pneumonia-86-54</p></li>
<hr>
</ul>

<h3> Details of various datasets used for model development : </h3>
<ul>
<li><p><b>Heart</b> : heart.csv [In the repository]</p></li>
<li><p><b>Diabetes</b> : diabetes.csv [In the repository]</p></li>
<li><p><b>Disease</b> : disease.csv [In the repository]</p></li>
<li><p><b>Pneumonia: </b> https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia </p></li>
</ul>

<hr>

<h3> Tools used for project development: </h3>
<ul>
<li><b>Python ( 3.7 version) - Django - Javascript -Pandas - Numpy -HTML - CSS</b></li>
</ul>

## Installation
The code is written in Python 3.7.0. If Python isn't installed, you can download it here. If you're using an older version, upgrade using pip to ensure you have the latest version. After cloning the repository, navigate to the project directory and run the following command to install the necessary packages:

Use pip to install the dependencies listed in the requirements file.


```bash
* pip install -r requirements.txt

* python manage.py makemigrations

* python manage.py migrate

* python manage.py createsuperuser

* python manage.py runserver

```