from module.eaeo import logging as lgg
import pdfkit
from django.template.loader import get_template

def render_pdf(pdffilename, data):
    try:
        template = get_template('main/export_influencer.html')
        html = template.render(data)
        options = {
            'page-width': '750px',
            'page-height': '834px',
            'margin-top': '0px',
            'margin-right': '0px',
            'margin-bottom': '0px',
            'margin-left': '0px',
            'enable-local-file-access': None
        }
        pdfkit.from_string(input=html, output_path=pdffilename, options=options)
        return 0
    except Exception as e:
        lgg._logging()
        return -1
