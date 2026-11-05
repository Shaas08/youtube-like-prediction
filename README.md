# YouTube Like Prediction

A Flask web app that predicts how many likes a YouTube video will get, based on
a linear regression model trained on the Kaggle "US YouTube Trending Videos"
dataset.

## How it works

- `model.py` loads `USvideos.csv`, drops text columns (title, description,
  tags, etc.), log-transforms `views`, `likes`, `dislikes` and
  `comment_count`, one-hot encodes `category_id`, and fits a
  `LinearRegression` model on views, dislikes, comment count, the
  comments/ratings-disabled and video-error flags, and category. The fitted
  model is pickled to `model.pkl`.
- `app.py` serves a form (`templates/index.html`) where a user enters a
  video's stats and category, and returns the predicted like count from
  `model.pkl`.
- `US_category_id.json` maps YouTube category IDs to names for the form.

## Project structure

```
app.py                 Flask app (routes: / and /predict)
model.py               Trains the linear regression model, writes model.pkl
model.pkl              Pickled trained model
US_category_id.json    YouTube category id -> name mapping
templates/index.html   Form + prediction result page
static/css/style.css   Page styling
static/Images/         Page assets
dataset/               Place USvideos.csv here to retrain
```

## Setup

```bash
pip install -r requirements.txt
```

Train the model (needs `USvideos.csv` from the
[Kaggle Trending YouTube Video Statistics](https://www.kaggle.com/datasets/datasnaek/youtube-new)
dataset, placed next to `model.py`):

```bash
python model.py
```

Run the app:

```bash
python app.py
```

Then open `http://127.0.0.1:5000`.
