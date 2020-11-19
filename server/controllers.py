from flask import Response

from app import session_maker
from model import LeadPac
from utils import get_or_create


def create_or_update_pac(request):
    # create a configured "Session" class
    json_data = request.json
    session = session_maker()
    lead = get_or_create(session, LeadPac, id=json_data['id'])
    for key, value in json_data.items():
        setattr(lead, key, value)
    session.commit()
    return Response("ok")