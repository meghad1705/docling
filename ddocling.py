from docling.document_converter import DocumentConverter

converter = DocumentConverter()

source = "tgwcs.pdf"  # local file path
doc = converter.convert(source).document

print(doc.export_to_markdown())
