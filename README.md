# Toxic Comment Classification

## Contributors and Credits

William Jessop

- Setup Google Colab Experiments
- Wrote notebooks to pickle the best models

Mario Bravo

- Did website development and deployment

The majority of the experiments in the notebooks were peer programmed.

## Quick Links

| Name                                 | Value                                                                                 |
| :----------------------------------- | :------------------------------------------------------------------------------------ |
| **Project Website**                  | https://cmu-toxic-comment-classifier.herokuapp.com/                                   |
| **Project Data**                     | https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge     |
| **SGD Google Colab**                 | https://colab.research.google.com/drive/1e-3QOrIehEA4yn5pfEOmeIAGLarX1krw?usp=sharing |
| **Logistic Regression Google Colab** | https://colab.research.google.com/drive/1gMchPcKvI1DTsCUj7EJTrj4UD1I8tPAY?usp=sharing |

## Project Abstract

Machine learning can be applied to natural language processing (NLP) and classification problems. A topical application of NLP is classifying hate speech on the internet forums. For our project, we propose to build and test various machine learning models to classify online comments as toxic or non-toxic. To train this model we will use a public dataset of labeled forum comments from Kaggle. We will take the best model we have trained and deploy it as a web application where users can enter a piece of text and the application will determine if the text entered is hate speech (toxic) or not.

## Project Overview

In this project Python and SciKit Learn are used to test various machine learning algorithms performance in classifying pieces of text as "toxic" or "non-toxic".
The data for this project was found on the Kaggle platform here: https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge

After the data was collected, it was cleaned, vectorized, and used to train different models. After the best model was found, it was deployed into a Flask website hosted on Heroku here: https://cmu-toxic-comment-classifier.herokuapp.com/

## Acronyms

The table below breaks down all of the acronyms that may be used throughout this repository.
| Acronym | Expansion | Type |
| :------------------ | :--------------------------------------------- | :------------------ |
| **NB** | Naive Bayes | ML Model |
| **LR** | Logistic Regression | ML Model |
| **SGD** | Stochastic Gradient Decent | ML Model |
| **tfidf** | Term Frequency Inverse Document Frequency | Vectorizer |

## Repo Structure

### Repo root
This folder of the repository contains the code for the Python website that was deployed as well as a few other files for Python deployment. This folder also contains the slides for the presentation that was given in a pdf format.
### Notebooks
This folder contains all of the data cleaning, and model testing, and model pickling that was done in Python. The experiments were done in Jupyter notebook and with seeded randomness. Notebooks in the "training" folder are named with the following convention: "notebookType_MLModel.ipynb"

The notebook types are as follows:
**"count"**: This notebook contains experiments with the Count vectorizer
**"tfidf"**: This notebook contains experiments with the tfidf vectorizer
**"tune"**:  This notebook contains hyper parameter tuning

### Pickles
This folder contains the pickled versions of the Python objects that were used in the website deployment of the project.

### Templates
This folder contains some static assets and html for the hosted Flask website.

## Hyper Parameter Tuning Experiments

To hyper parameter tune the models that were chosen, the Google Colab platform was utilized. The results of the hyper parameter tuning can be viewed in Google Colab links below.
The experiments that are linked below use a balanced subsample technique tom re-balance the training data.

**Tuning SGD:** https://colab.research.google.com/drive/1e-3QOrIehEA4yn5pfEOmeIAGLarX1krw?usp=sharing
**Tuning Logistic Regression:** https://colab.research.google.com/drive/1gMchPcKvI1DTsCUj7EJTrj4UD1I8tPAY?usp=sharing
