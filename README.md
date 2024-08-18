# 🦸‍♂️ Django Pokédex

Welcome to the **Django Pokédex**! This project is a simple web application built with Django that fetches and displays Pokémon data using the PokéAPI. With this app, you can browse through the first 151 Pokémon, view detailed stats, and enjoy a sleek user interface.

## 🚀 Features

- **List of Pokémon**: Browse through the first 151 Pokémon.
- **Detailed Pokémon Information**: Click on a Pokémon to view its stats, abilities, weight, height, and more.
- **Search Functionality**: Quickly find your favorite Pokémon by name or ID.
- **Responsive Design**: A clean and responsive layout that looks great on any device.

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Gourav9165/Pokedex-django.git
cd django-pokedex
```

### 2. Set Up a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to see the application in action.


## 📝 Code Overview

### `views.py`

- **index(request)**: Fetches the first 151 Pokémon from the PokéAPI and renders them on the home page.
- **detail(request, id)**: Fetches detailed information for a specific Pokémon based on its ID and renders it on the detail page.

### `models.py`

Defines the `Pokemon` model, which includes fields like `name`, `number`, `image_url`, `weight`, `height`, `abilities`, `type_1`, and `type_2`.

### `urls.py`

- **pokedex/urls.py**: The main URL configuration that includes the Pokémon app's URLs.
- **pokemon/urls.py**: Handles routes for the index and detail views.

### `index.html`

The homepage that displays the list of Pokémon with search functionality.

### `detail.html`

The detail page that shows the stats and information for a specific Pokémon.

## 🎨 UI Highlights

- **Dynamic Search**: As you type in the search bar, the Pokémon list updates in real-time.
- **Hover Effects**: Smooth hover effects on the Pokémon cards for an engaging user experience.
- **Detailed View**: View the full details of any Pokémon, including base stats, abilities, and description.

## 🤝 Contributing

Feel free to fork this repository, create a feature branch, and submit a pull request. All contributions are welcome!

