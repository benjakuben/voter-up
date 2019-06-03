import functools
import requests
import sys
import json

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

        # Make the request (formatted as JSON)
        url = base_url + query_string
        response = requests.get(
            url, 
            headers={'Accept': 'application/json'},
        )
    
        data = process_response(response.content)

        return render_template('election_results.html', data=data)


def build_query_string(form_data):
    q_base = '?district-divisions='
    params = 'ocd-division/'
    ocd_id_count = 0
    
    # Default: Only in the US
    country = 'us'
    params += f'country:{country}'

    # Try to process each form input field and add it to the query string
    # Example: '?district-divisions=ocd-division/country:us/state:fl/place:coral_springs'

    # For this exercise, we'll only use state and city (place)
    key_list = ['state', 'city']

    for key in key_list:
        param_name = get_query_param_name(key)
        value = form_data.get(key)

        if value is not None:
            # Separate multiple OCD_IDs with a comma
            if ocd_id_count > 0:
                params += f',{params}'

            params += f'/{param_name}:{format_for_call(value)}'
            ocd_id_count += 1

    return q_base + params


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


def process_response(json_data):
    # This first check is for how an empty response comes back
    if json_data == b'[]':
        return None
    else:
        return json.loads(json_data)