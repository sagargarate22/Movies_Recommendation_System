# 🎬 Context-Based Movie Recommendation System

This is a **context-based movie recommendation system** that recommends movies to users based on various factors such as cast, author, storyline, genre, and more.

## 🛠️ Tech Stack

**Frontend:**
- HTML
- CSS
- JavaScript

**Backend:**
- Python
- Django

## 🤖 Machine Learning Model

This project uses a machine learning model based on **cosine similarity** and **CountVectorizer** to provide content-based movie recommendations.

### Model Details:
- **Algorithm:** Cosine Similarity on CountVectorizer features
- **Features Used:** Movie cast, director, storyline, genre
- **Model Storage:** Saved as `model.pkl`
- **Data Source:** Kaggle movie dataset
- **Libraries Used:** scikit-learn, pandas

### How it Works:
1. When a user searches for a movie, the backend retrieves the movie’s feature vector.
2. The saved model (`model.pkl`) calculates similarity scores with other movies.
3. Top similar movies are returned as recommendations.

## 🔐 Features

- User Authentication (Sign Up & Login)
- Search movies by name
- Get smart movie recommendations based on:
  - Cast
  - Director/Author
  - Storyline
  - Genre

## 🚀 How to Run This Project Locally

Follow these steps to set up and run the project on your local machine.

### 1. Clone the Repository
```bash
git clone https://github.com/sagargarate22/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2. Create a Virtual Environment
Make sure you have Python installed.
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment
Windows
```bash
venv\Scripts\activate
```
Linux/MacOS
```bash
source venv/bin/activate
```
### 4. Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 5. Install ML Model from drive
Windows
```bash
bash download_model.sh
```
MacOs/Linux
```bash
chmod +x download_model.sh
```
```bash
./download_model.sh
```

### 6. Apply Migrations
Go to the directory where `manage.py` file present and run the command
```bash
python manage.py migrate
```
### 7. Run the Development Server
```bash
python manage.py runserver
```
Then open your browser and go to:
`http://127.0.0.1:8000/`



## 📝 Notes
 - Make sure you are connected to the internet if any external APIs are used.

 - You can create a superuser for admin access:

```bash
python manage.py createsuperuser
```

---
# 🙋‍♂️ Author
**Sagar Garate**

**LinkedIn :** [LinkedIn](https://www.linkedin.com/in/sagar-garate-3573ab233)

**GitHub :** [GitHub](https://github.com/sagargarate22)
