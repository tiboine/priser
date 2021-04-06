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
RANGE_NAME = 'PrislisteLandskap!A1:050'
MAIN_PRICE = 'Hoved!D3:J50'
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

mydict = {}


productVarTemp = []
myValues = []
mySizes = []
myValues2 = []
mySizes2 = []
productVar = []
productSize = []
productPrice = []
awesomelist = []
countLog = []


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
                                      range=MAIN_PRICE).execute()
    all_values = price_result.get('values', [])

    for row in range(len(all_values)):
        if all_values[row][0] != '':
            # lagrer produktnavn i liste
            productVarTemp.append(all_values[row])
        else:
            # lagrer verdiene til størrelse og pris
            mySizes.append(all_values[row][1])
            myValues.append(all_values[row][6])
            countLog.append(len(productVarTemp))

    for i in range(len(productVarTemp)):  # sjekker antall produkter
        myv = []
        myl = []
        i += 1  # +1 for at neste count skal starte fra 1, og ikke 0
        # lager lister av pris/lengde for antallet produkter
        for j in range(countLog.count(i)):
            myl.append(mySizes.pop(0))
            myv.append(myValues.pop(0))

        myValues2.append(myv)
        mySizes2.append(myl)
    for i in range(len(productVarTemp)):
        productVar.append(productVarTemp[i][0])
        productSize.append(mySizes2[i])
        productPrice.append(myValues2[i])

    if not values:
        print('No data found.')
    else:
        for row in values:
            sheets.append(row)


if __name__ == '__main__':
    gsheets()
