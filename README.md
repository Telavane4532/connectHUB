# 🔗 ConnectHub — Social Media Web Application

A full-stack social media web application built with Python and Django,
featuring user authentication, post interactions, follow system,
real-time notifications, and direct messaging.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Django](https://img.shields.io/badge/Django-6.0-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

##  Live Demo [connecthub.up.railway.app](https://connecthub.up.railway.app)

---



##  Features

-  **User Authentication** — Register, Login, Logout with
  Django's built-in auth system
-  **User Profiles** — Custom bio, profile picture,
  followers & following count
-   Posts — Create, view and delete posts in a live feed
-   Likes — Like and unlike posts with instant toggle
-   Comments — Comment on posts and delete your own comments
-   Follow System — Follow and unfollow other users
-   Notifications — Get notified on likes, comments and follows
-   Direct Messages — Private conversations between users
-   Search — Search for users by username
-   Responsive UI — Clean modern design using Bootstrap 5

---

##  Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.13 |
| Framework | Django 6.0 |
| Database | SQLite |
| Frontend | Bootstrap 5, HTML, CSS |
| Icons | Bootstrap Icons |
| Fonts | Google Fonts (Inter) |
| Deployment | Railway |
| Server | Gunicorn + WhiteNoise |

---

##  Project Structure
<img width="901" height="483" alt="image" src="https://github.com/user-attachments/assets/5b28c45a-cfde-4a9c-960f-0b3cc47d67ce" />


---

##  Local Setup

Follow these steps to run the project locally:

### 1. Clone the repository
```bash
git clone https://github.com/YOURUSERNAME/connecthub.git
cd connecthub
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Create superuser
```bash
python manage.py createsuperuser
```

### 6. Run the server
```bash
python manage.py runserver
```

### 7. Visit the app
http://127.0.0.1:8000

## 📚 What I Learned

- Django MVT architecture and project structure
- Django ORM — ForeignKey, ManyToMany relationships
- User authentication and session management
- File uploads with Pillow
- Building notification systems across multiple apps
- Responsive UI design with Bootstrap 5
- Cloud deployment with Railway

---

##  Future Improvements

- [ ] Real-time chat using Django Channels & WebSockets
- [ ] Image posts support
- [ ] Stories feature like Instagram
- [ ] Switch to PostgreSQL for production
- [ ] REST API using Django REST Framework
- [ ] Mobile app using React Native

---

##  Author

**Your Name**
- GitHub: [@telavane4532](https://github.com/telavane4532)
---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
