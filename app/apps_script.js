// ===================================================================
// DPIA Path — Google Apps Script per raccolta report
// ===================================================================
//
// ISTRUZIONI:
// 1. Crea un Google Sheet nuovo
// 2. Vai su Estensioni > Apps Script
// 3. Incolla questo codice nel file Code.gs (sostituisci tutto)
// 4. Esegui la funzione "setup" una volta (menu Esegui > setup)
// 5. Fai il deploy: Deploy > New deployment > Web App
//    - Execute as: Me
//    - Who has access: Anyone
// 6. Copia l'URL del deploy e incollalo nella configurazione della Dashboard
//
// NOTA: La prima volta potrebbe chiederti di autorizzare l'accesso allo Sheet.
// ===================================================================

function setup() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getActiveSheet();
  sheet.setName('DPIA Reports');

  // Header row
  var headers = [
    'Timestamp', 'ID', 'Studente', 'Titolare', 'Finalita',
    'Dati', 'Interessati', 'Base Giuridica', 'Sistema AI',
    'Processo Decisionale', 'Fornitori', 'Precheck',
    'Rischio Medio', 'Rischio Aggregato', 'Misure Selezionate',
    'Esito Colore', 'Esito Label', 'Esito Messaggio', 'JSON Completo'
  ];

  sheet.getRange(1, 1, 1, headers.length).setValues([headers]);
  sheet.getRange(1, 1, 1, headers.length).setFontWeight('bold');
  sheet.setFrozenRows(1);

  // Auto-resize
  for (var i = 1; i <= headers.length; i++) {
    sheet.autoResizeColumn(i);
  }
}

function doPost(e) {
  try {
    var data = JSON.parse(e.postData.contents);
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getSheetByName('DPIA Reports') || ss.getActiveSheet();

    var row = [
      data.timestamp || new Date().toISOString(),
      data.id || '',
      data.studente || '',
      data.titolare || '',
      data.finalita || '',
      data.dati || '',
      data.interessati || '',
      data.base || '',
      data.ai || '',
      data.processo || '',
      data.fornitori || '',
      data.precheckLabel || '',
      data.riskAvg || '',
      data.riskAggregate ? data.riskAggregate.label : '',
      data.measuresCount || 0,
      data.finalColor || '',
      data.finalLabel || '',
      data.finalMessage || '',
      JSON.stringify(data)
    ];

    sheet.appendRow(row);

    return ContentService
      .createTextOutput(JSON.stringify({ status: 'ok', message: 'Salvato' }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'error', message: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet(e) {
  var action = (e && e.parameter && e.parameter.action) || 'getAll';

  if (action === 'getAll') {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getSheetByName('DPIA Reports') || ss.getActiveSheet();
    var lastRow = sheet.getLastRow();

    if (lastRow <= 1) {
      return ContentService
        .createTextOutput(JSON.stringify([]))
        .setMimeType(ContentService.MimeType.JSON);
    }

    var dataRange = sheet.getRange(2, 19, lastRow - 1, 1); // Column S = JSON Completo
    var values = dataRange.getValues();
    var results = [];

    for (var i = 0; i < values.length; i++) {
      try {
        if (values[i][0]) {
          results.push(JSON.parse(values[i][0]));
        }
      } catch (err) {
        // skip malformed rows
      }
    }

    return ContentService
      .createTextOutput(JSON.stringify(results))
      .setMimeType(ContentService.MimeType.JSON);
  }

  return ContentService
    .createTextOutput(JSON.stringify({ status: 'ok', action: action }))
    .setMimeType(ContentService.MimeType.JSON);
}
