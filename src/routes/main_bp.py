from flask import Blueprint
from controllers.MainController import home, profile, faq, community, recipe

main_bp = Blueprint('main_bp', __name__)

main_bp.route('/', methods=['GET','POST'])(home)
main_bp.route('/home', methods=['GET','POST'])(home)
main_bp.route('/profile', methods=['GET','POST'])(profile)
main_bp.route('/community', methods=['GET','POST'])(community)
main_bp.route('/recipe', methods=['GET','POST'])(recipe)
main_bp.route('/faq', methods=['GET'])(faq)