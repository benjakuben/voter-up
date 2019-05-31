import functools

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
        return render_template('election_results.html')