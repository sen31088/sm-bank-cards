from flask import render_template, Blueprint, session
from models.model_cards import Carddetails
from utils.encrypt import encrypt


cards_ctrl = Blueprint("cards", __name__, static_folder='static', template_folder='templates')

@cards_ctrl.route("/cards",methods=["POST", "GET"])
def cards(): 
    user_session = session.get('name')
    user_session_otp = session.get('otp_valid')
    if not user_session or not user_session_otp:
        return render_template('index.html')
    else:
        act_page = 'cards'
        user_session = session.get('name')
        card_details_found = Carddetails.get_data({'userid': user_session})
        card_number = card_details_found["Cardnum"]
        card_start_date = card_details_found["CardStartdate"]
        card_end_date = card_details_found["CardEnddate"]
        card_holder_name = card_details_found["CardName"]
        card_cvv_num = card_details_found["Cardcvv"]
        decoded_card_number = encrypt.decode(card_number)
        decode_cvv_number = encrypt.decode(card_cvv_num)
        return render_template('cards.html', active_page = act_page, card_num = decoded_card_number, card_start = card_start_date, card_end = card_end_date, card_name = card_holder_name,card_cvv = decode_cvv_number, logedin_user = user_session)