import functools
import requests
import sys

from elections.us_states import postal_abbreviations

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('address_form', __name__, url_prefix='/')


@bp.route('/', methods=['GET'])
def display_form():
    """Take in an address."""
    return render_template('address_form.html', states=postal_abbreviations)


@bp.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        # Make a request to the TurboVote API
        base_url = 'https://api.turbovote.org/elections/upcoming'
        query_string = build_query_string(request.form)

        # Grabbed a place with known elections from here: https://github.com/democracyworks/dw-practical-upcoming-elections/wiki/Upcoming-Elections
        url = base_url + query_string

        # Configure the request for JSON
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.get(url, headers=headers)
    
        # BJJ TESTING
        print(url, file=sys.stderr)
        return response.content
        #return render_template('election_results.html')


def build_query_string(form_data):
    q = '?district-divisions=ocd-division/'
    
    # Default: Only in the US
    country = 'us'
    q += f'country:{country}'

    # Try to process each form input field and add it to the query string
    # Example: '?district-divisions=ocd-division/country:us/state:fl/place:coral_springs'
    key_list = ['state', 'city']
    for key in key_list:
        param_name = get_query_param_name(key)
        value = form_data.get(key)
        if value is not None:
            q += f'/{param_name}:{format_for_call(value)}'

    return q


# TODO: Clean this up into a helper class that uses constants and takes care of mappings
def get_query_param_name(key):
    if key == 'city':
        return 'place'
    elif key == 'state':
        return 'state'
    else:
        return ''


def format_for_call(value):
    # Trim extra whitespace
    value = value.strip()

    # Make all lowercase
    value = value.lower()

    # Convert spaces to underscores
    return value.replace(' ', '_')
