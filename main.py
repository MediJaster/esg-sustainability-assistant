from docling.document_converter import DocumentConverter


def main():
    source = "./documents/prova.pdf"  # document per local path or URL
    converter = DocumentConverter()
    result = converter.convert(source)
    with open("output.md", "w") as f:
        f.write(result.document.export_to_markdown())


if __name__ == "__main__":
    main()
