# Running this app

Follow the instructions below to install requirements and run the app for this interview exercise.

## Installation
If Flask and pytest are needed: 
```
pip install -r requirements.txt
```

## Running the app

Set up your local Flask environment:
```
export FLASK_APP=elections
export FLASK_ENV=development
flask run
```

## Testing the app
```
pytest
```

# Task List

**Required**
- [x] Stub out pages (Home/form and results)
- [x] Confirm initial API call
- [x] Wire up form to the API call <== ~ 2 hours of work
- [x] Parse results
- [x] Format results nicely for display <== ~ 3 hours of work

**Stretch goals**
- [ ] Validate form input
- [ ] Add input tests
- [ ] Add friendly error messages
- [ ] Display or link to results on Google Maps (maybe a link to show in Maps)