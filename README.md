# Keep Trade Cut to Google Sheet

This Python Script scrapes Keep Trade Cut Superflex Dynasty Fantasy Football rankings and inserts them into Google Sheets.

## Instillation

This program uses the following libraries:

<ul>
    <li>Pandas</li>
    <li>Beautiful Soup</li>
    <li>Pygsheets</li>
</ul>

This program also requires credentials for the google sheets api via a json file. The json file will have to be placed in the project directory and the PATH inserted in the global variable CREDS_PATH. Once configured, you will need to create a google sheet and insert the sheet id in the global variable SPREADSHEET_ID + share the sheet with the app created in google developer tab (with editors privileges).

## Usage

Simply call the scrape.cmd file. 
