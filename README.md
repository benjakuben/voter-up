# Running this app

Follow the instructions below to install requirements and run this app for this interview exercise.

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
**Not implemented**
```
pytest
```

# Task List
It took me about two hours to correctly call the API with data from the form, and then an additional hour to parse and display the results in a nice format.

**Required**
- [x] Stub out pages (Home/form and results)
- [x] Confirm initial API call
- [x] Wire up form to the API call <== ~ 2 hours of work (total)
- [x] Parse results
- [x] Format results nicely for display <== ~ 3 hours of work (total)

**Stretch goals**
- [ ] Validate form input
- [ ] Add input tests
- [ ] Add friendly error messages
- [ ] Display or link to results on Google Maps (maybe a link to show in Maps)

**Issues**
- [ ] Empty form hangs the page (fix with form validation)
- [ ] Update Election Results template to not display items that don't have values (ex. no website for Pinehurst)