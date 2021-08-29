from io import BytesIO
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import uuid
from django.conf import settings


def save_pdf(params: dict):
    template = get_template("pdf.html")
    print("template: ", template)
    html = template.render(params)
    print("html: ", html)
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
    print("html: ", html)
    file_name = uuid.uuid4()

    try:
        print("Inside TRy FILE: ", file_name)
        with open(str(settings.BASE_DIR) + f"/media/{file_name}.pdf", "wb+") as output:
            pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), output)
            print("Inside TRy pdf: ", pdf)

    except Exception as e:
        print(e)

    if pdf.err:
        return "", False

    return file_name, True
