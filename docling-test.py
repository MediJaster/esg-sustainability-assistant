import ssl
import urllib3
from docling.document_converter import DocumentConverter

# Disable SSL verification warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Create an unverified SSL context
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE


def main():
    source = "./documents/prova.pdf"

    # Set environment variables to disable SSL verification
    import os

    os.environ["CURL_CA_BUNDLE"] = ""
    os.environ["REQUESTS_CA_BUNDLE"] = ""
    os.environ["SSL_VERIFY"] = "false"
    os.environ["PYTHONHTTPSVERIFY"] = "0"

    converter = DocumentConverter()
    result = converter.convert(source)

    with open("output.md", "w", encoding="utf-8") as f:
        f.write(result.document.export_to_markdown())


if __name__ == "__main__":
    main()
