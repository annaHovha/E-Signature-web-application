import os

from docusign_esign import EnvelopesApi, RecipientViewRequest
from flask import send_from_directory, current_app

from app.ds_client import DsClient


class Envelope:
    @staticmethod
    def send(envelope):
        """Send an envelope
        Parameters:
            envelope (object): EnvelopeDefinition object
        Returns:
            envelope_id (str): envelope ID
        """
        # Call Envelope API create method
        # Exceptions will be caught by the calling function
        access_token = current_app.config["ACCESS_TOKEN"]
        account_id = 'b85e5bc6-a609-4152-bc29-42312d938570'

        ds_client = DsClient.get_configured_instance(access_token)

        envelope_api = EnvelopesApi(ds_client)
        results = envelope_api.create_envelope(
            account_id,
            envelope_definition=envelope
        )
        return results.envelope_id

    @staticmethod
    def get_view(envelope_id, envelope_args, student, authentication_method='None'):
        """Get the recipient view
        Parameters:
            envelope_id (str): envelope ID
            envelope_args (dict): parameters of the document
            student (dict): student information
            authentication_method (str): authentication method
        Returns:
            URL to the recipient view UI
        """
        # we will hardcode the account_id and access_token for now
        access_token = current_app.config["ACCESS_TOKEN"]
        account_id = 'b85e5bc6-a609-4152-bc29-42312d938570'

        # Create the RecipientViewRequest object
        recipient_view_request = RecipientViewRequest(
            authentication_method=authentication_method,
            client_user_id=envelope_args['signer_client_id'],
            recipient_id='1',
            return_url=envelope_args['ds_return_url'],
            user_name=f"{student['first_name']} {student['last_name']}",
            email=student['email']
        )
        # Obtain the recipient view URL for the signing ceremony
        # Exceptions will be caught by the calling function
        ds_client = DsClient.get_configured_instance(access_token)

        envelope_api = EnvelopesApi(ds_client)
        results = envelope_api.create_recipient_view(
            account_id,
            envelope_id,
            recipient_view_request=recipient_view_request
        )
        return results



# https://account-d.docusign.com/oauth/auth?response_type=code&scope=signature&client_id=5b6857cb-b3c3-4192-aa00-2295e3ec2f4d&redirect_uri=http://localhost/
