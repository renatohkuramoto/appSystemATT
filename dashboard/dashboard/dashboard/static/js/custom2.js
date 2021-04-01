let URL_TO_FETCH = 'http://54.39.228.181:8000/api/clientes/documentos/download-all-documents/'
let filedata = JSON.parse(document.getElementById('contents').innerHTML);

async function getpdf () {
    response = await fetch(URL_TO_FETCH + filedata, {
        method: 'GET',
        headers: {
            'Authorization': 'Bearer ' + access_token
        },});
    response.blob().then(function(content) {
        let pdf = URL.createObjectURL(content)
        PDFObject.embed(pdf, "#pdfwindow");
    })
}

getpdf()