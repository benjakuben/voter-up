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

        ### BJJ TESTING WITH HARDCODE VALUE
        ### Grabbed a place with known elections from here: https://github.com/democracyworks/dw-practical-upcoming-elections/wiki/Upcoming-Elections
        url = 'https://api.turbovote.org/elections/upcoming?district-divisions=ocd-division/country:us/state:fl/place:coral_springs'

        # Configure the request for JSON
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.get(url, headers=headers)
    
        print(f'TESTING::status code={response.status_code}', file=sys.stderr)
        print('\n\nTESTING::response.content\n\n', file=sys.stderr)
        print(response.content, file=sys.stderr)

        return render_template('election_results.html')