from flask import render_template, request
from flask_login import login_required, current_user

def home():
	return render_template('index.html')

@login_required
def profile():
	return render_template('profile.html', name=current_user.name, id=current_user.id)
	# return render_template('profile.html', name=current_user.name)


@login_required
def community():
	return render_template('community.html')

@login_required
def recipe():
	return render_template('recipe.html')


def faq():
	return render_template('faq.html')

def recipe():
    return render_template('recipe.html')