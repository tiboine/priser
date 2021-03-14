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
MAIN_PRICE = 'Kopi av Main!D3:J43'
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


templist = []
myValues = []
myLengths = []
myValues2 = []
myLengths2 = []

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
    price_values = price_result.get('values', [])

    count = 0
    for x in range(len(price_values)):
        if price_values[x][0] != '':  # skriver navn på produktene
            count += 1
            templist.append(price_values[x])
        if price_values[x][0] == '':  # legger til prisene

            myLengths.append(price_values[x][1])
            myValues.append(price_values[x][6])
            countLog.append(count)

    for i in range(count):  # 7 ganger
        myv = []
        myl = []

        # deler opp prisene i egne lister for å sette sammen etterpå
        for j in range(countLog.count(i+1)):
            myl.append(myLengths.pop(0))
            myv.append(myValues.pop(0))
        myValues2.append(myv)
        myLengths2.append(myl)

        mydict[templist[i][0]] = dict(
            zip(myLengths2[i], myValues2[i]))
    # print(mydict)
    for i in range(1, 6):
        priceStorformat[price_values[i][1]] = price_values[i][6]
    prices['storformat'] = priceStorformat
    for i in range(6, 11):
        priceStorformatPano[price_values[i][1]] = price_values[i][6]
    prices['storformatPano'] = priceStorformatPano

    for i in range(11, 16):
        priceChroma[price_values[i][1]] = price_values[i][6]
    prices['Chromaluxe'] = priceChroma
    for i in range(16, 21):
        priceLerret[price_values[i][1]] = price_values[i][6]
    prices['Lerret'] = priceLerret
    for i in range(21, 26):
        priceLerretPano[price_values[i][1]] = price_values[i][6]
    prices['LerretPano'] = priceLerretPano
    for i in range(26, 29):
        priceLerretPano_3_1[price_values[i][1]] = price_values[i][6]
    prices['LerretPano_3_1'] = priceLerretPano_3_1
    for i in range(29, 31):
        priceStorformatPano_3_1[price_values[i][1]] = price_values[i][6]
    prices['storformatPano_3_1'] = priceStorformatPano_3_1
    # print(prices)
    if not values:
        print('No data found.')
    else:
        for row in values:
            sheets.append(row)


if __name__ == '__main__':
    gsheets()
