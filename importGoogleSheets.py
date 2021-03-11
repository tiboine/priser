from __future__ import print_function
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle
import os.path
from googlekey import key

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = key
RANGE_NAME = 'Prisliste!A1:N50'
SHEET_PRICE_RANGE = 'Main!B1:I43'
sheets = []
sheetsPrice = {}
prices = {}
priceStorformat = {}
priceStorformatPano = {}
priceStorformatPano_3_1 = {}
priceChroma = {}
priceLerret = {}
priceLerret_2_3 = {}
priceLerretPano = {}
priceLerretPano_3_1 = {}


def gsheets():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()  # dunno what's wrong here
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])

    price_result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                      range=SHEET_PRICE_RANGE).execute()
    price_values = price_result.get('values', [])

    for i in range(1, 6):
        priceStorformat[price_values[i][1]] = price_values[i][7]
    prices['storformat'] = priceStorformat
    # print(priceStorformat)
    # print(prices)
    print(price_values[i][1])
    for i in range(7, 12):
        priceStorformatPano[price_values[i][1]] = price_values[i][7]
    prices['storformatPano'] = priceStorformatPano
    for i in range(13, 18):
        priceChroma[price_values[i][1]] = price_values[i][7]
    prices['Chromaluxe'] = priceChroma
    for i in range(19, 24):
        priceLerret[price_values[i][1]] = price_values[i][7]
    prices['Lerret'] = priceLerret
    for i in range(25, 30):
        priceLerretPano[price_values[i][1]] = price_values[i][7]
    prices['LerretPano'] = priceLerretPano
    for i in range(31, 34):
        priceLerretPano_3_1[price_values[i][1]] = price_values[i][7]
    prices['LerretPano_3_1'] = priceLerretPano_3_1
    for i in range(35, 38):
        priceStorformatPano_3_1[price_values[i][1]] = price_values[i][7]
    prices['storformatPano_3_1'] = priceStorformatPano_3_1
    # print(prices)
    if not values:
        print('No data found.')
    else:
        for row in values:
            sheets.append(row)


if __name__ == '__main__':
    gsheets()
