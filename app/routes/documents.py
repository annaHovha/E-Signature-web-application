import base64
import requests
from http import HTTPStatus

from docusign_esign import ApiException
from flasgger import swag_from
from flask import Blueprint, request, jsonify, session,redirect,current_app

from app.ds_client import DsClient
from app.schemas.documents import SomeTemplateSchema
from app.services.document import DsDocument
from app.services.envelope import Envelope


bp = Blueprint('documents', __name__, url_prefix='/documents')


@bp.route("/template", methods=["post"])
@swag_from('../apidoc/documents/template.yaml')
def sign_some_template():
    data = SomeTemplateSchema().load(request.json)

    student = {
        'email': data['email'],
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'description': data['description']
    }
    envelope_args = {
        'signer_client_id': 1000,
        'ds_return_url': data['callback_url']
    }

    try:
        envelope = DsDocument.create('some-awesome-template.html', student, envelope_args)
        envelope_id = Envelope.send(envelope)

    except ApiException as e:
        print(e)
        return {'message': f"Error: {e}"}, HTTPStatus.BAD_REQUEST

    try:
        result = Envelope.get_view(envelope_id, envelope_args, student)
    except ApiException as e:
        print(e)
        return {'message': f"Error: {e}"}, HTTPStatus.BAD_REQUEST

    return jsonify({'envelope_id': envelope_id, 'redirect_url': result.url})


@bp.route('/docusign-token', methods=['POST'])
@swag_from('../apidoc/documents/docusign-token.yaml')
def get_docusign_token():
    # Extracting integration key, secret key, and code from the request
    integration_key = '6f0dcfae-db40-44a7-92fd-ed4cb8773ab9'
    secret_key = '3a1ec801-6a24-4501-b6d1-e14716b6d64f'
    code = session.get('code')

    # Constructing the Authorization header value
    auth_header = base64.b64encode(f"{integration_key}:{secret_key}".encode()).decode()
    # Constructing the request body
    data = {
        'grant_type': 'authorization_code',
        'code': code
    }

    # Constructing the headers
    headers = {
        'Authorization': f'Basic {auth_header}',
        'Content-type': 'application/x-www-form-urlencoded',
    }

    # Making the POST request to DocuSign OAuth token endpoint
    response = requests.post('https://account-d.docusign.com/oauth/token', data=data, headers=headers)
    current_app.config["ACCESS_TOKEN"] = response.json()['access_token']
    # Returning the response
    return jsonify(response.json())


@bp.route('/code', methods=['GET'])
def get_code():
    code = request.args.get('code')
    session['code'] = code
    return 'Successfully added the code'
