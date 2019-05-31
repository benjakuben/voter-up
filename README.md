# Running this app

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
- [ ] Stub out pages (Home/form and results)
- [ ] Confirm initial API call
- [ ] Parse results
- [ ] Format results nicely for display

**Stretch goals**
- [ ] Validate form input
- [ ] Add input tests
- [ ] Add friendly error messages
- [ ] Display or link to results on Google Maps (maybe a link to show in Maps)