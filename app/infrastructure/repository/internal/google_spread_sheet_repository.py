from gspread import Client
from app.infrastructure.auth.google import GoogleAuth


class GoogleSpreadSheetRepository:
    client: Client

    def __init__(self) -> None:
        self.client = GoogleAuth().authorize()

    def fetch_by_url(self, url: str):
        sheet = self.client.open_by_url(url).sheet1
        return sheet.get_all_values()
