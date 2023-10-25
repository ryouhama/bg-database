from google.oauth2.service_account import Credentials
from gspread import authorize as google_authorize, Client


class GoogleAuth:
    def authorize(self) -> Client:
        credentials = Credentials.from_service_account_file(
            "YOUR_CREDENTIAL_FILEPATH",
            scopes=[
                "https://www.googleapis.com/auth/spreadsheets",
                "https://www.googleapis.com/auth/drive",
            ],
        )
        return google_authorize(credentials)
