from docxtpl import DocxTemplate

class Certificado ():
    @static_method
    def teste1(dic):
            doc = DocxTemplate("my_word_template.docx")
            context = { '' : "" }
            doc.render(context)
            doc.save("certificado_editado.docx")
