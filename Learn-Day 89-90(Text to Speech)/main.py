import io
import pyttsx3
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage


def pdf_to_speech(pdf_file):
    # Open the PDF file in binary mode
    with open(pdf_file, 'rb') as f:
        # Create a PDF resource manager object that stores shared resources
        resource_manager = PDFResourceManager()

        # Create a string object that stores the final text
        fake_file_handle = io.StringIO()

        # Set parameters for PDF resource manager
        laparams = LAParams()

        # Create a PDF converter object
        converter = TextConverter(
            resource_manager,
            fake_file_handle,
            laparams=laparams
        )

        # Create a PDF page interpreter object
        page_interpreter = PDFPageInterpreter(
            resource_manager,
            converter
        )

        # Iterate through all the pages in the PDF file
        for page in PDFPage.get_pages(f, check_extractable=False):
            # Process the page
            page_interpreter.process_page(page)

        # Get the extracted text
        text = fake_file_handle.getvalue()

        # Close the PDF converter and fake file handle
        converter.close()
        fake_file_handle.close()

        # Initialize the text-to-speech engine
        engine = pyttsx3.init()

        # Convert the text to speech
        engine.say(text)
        engine.runAndWait()


pdf_to_speech('example.pdf')
