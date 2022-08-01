# Courier Statistics

This Django app is designed to help couriers in the UK working with Deliveroo and Stuart to see better statistics about their work.

This simple app lets you add Restaurants, then you will be able to add orders for those restaurants.

I've taken into account the information provided by Deliveroo and Stuart so that the forms for Deliveroo and Stuart are slightly different; same for the statistics.

For example: statistics for Deliveroo include the time you took to finish each delivery order, and a promedy for each restaurant, so that you can judge better on which restaurants are faster. You are also provided with average £ made with each restaurant, and average of £ in that restaurant.

Only downside is that all information must be provided by the end user manually, since there's no public API for the Deliveroo and Stuart courier apps.

Uber Eats can be implemented, but since I don't have an account with them, I don't know what information they provide within the app to set up the models in the DB.

## Installation:

1- Clone this repository and *cd* into it:

```
git clone https://github.com/JeanFerreira91/Courier-Statistics-Django.git
cd Courier-Statistics-Django
```

2- Create a virtual environment:

```
python3 -m venv venv
```

3- Activate the virtual environment:

```
source venv/bin/activate
```

4- Install what's in *requirements.txt*

```
pip install -r requirements.txt
```

5- Run the code:

```
python manage.py runserver
```

Feel free to edit the code and adjust it to your needs.