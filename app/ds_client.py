import os
import uuid

from docusign_esign import ApiClient, AccountsApi



class DsClient:
    """
    Docusign Client class
    """

    @staticmethod
    def get_instance():
        """
        Getting a client instance with DS_HOST_NAME set
        """
        client = ApiClient()
        host_name = 'https://account-d.docusign.com'.split('://')[1]
        client.set_oauth_host_name(oauth_host_name=host_name)
        return client

    @classmethod
    def get_configured_instance(cls, access_token, host=None):
        if host is None:
            host = 'https://demo.docusign.net' + '/restapi'
        client = cls.get_instance()
        client.host = host
        client.set_default_header(
            header_name="Authorization",
            header_value=f"Bearer {access_token}"
        )

        return client

    @classmethod
    def get_redirect_uri(cls):
        """
        Receiving a redirect so that the user logs into his DS account and gives consent
        """
        client = cls.get_instance()

        # this values should not be hardcoded we need to pass them from the config file
        uri = client.get_authorization_uri(
            client_id='5b6857cb-b3c3-4192-aa00-2295e3ec2f4d',
            scopes='signature',
            redirect_uri='http://localhost/',
            response_type="code",
            state=uuid.uuid4().hex.upper()
        )
        return uri





