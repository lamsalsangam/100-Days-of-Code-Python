import io
import tkinter as tk
from tkinter import filedialog
import pyttsx3
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage


class PDFToSpeechConverter:
    def __init__(self, master):
        self.master = master
        master.title('PDF to Speech Converter')

        self.pdf_filename = ''
        self.text = ''

        self.select_button = tk.Button(
            master,
            text='Select PDF',
            command=self.select_pdf
        )
        self.select_button.pack()

        self.convert_button = tk.Button(
            master,
            text='Convert to Speech',
            command=self.convert_to_speech,
            state=tk.DISABLED
        )
        self.convert_button.pack()

    def select_pdf(self):
        self.pdf_filename = filedialog.askopenfilename(
            initialdir='.',
            title='Select PDF File',
            filetypes=[('PDF files', '*.pdf')]
        )

        if self.pdf_filename:
            self.convert_button.config(state=tk.NORMAL)

    def convert_to_speech(self):
        # Open the PDF file in binary mode
        with open(self.pdf_filename, 'rb') as f:
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
            self.text = fake_file_handle.getvalue()

            # Close the PDF converter and fake file handle
            converter.close()
            fake_file_handle.close()

            # Initialize the text-to-speech engine
            engine = pyttsx3.init()

            # Convert the text to speech
            engine.say(self.text)
            engine.runAndWait()


root = tk.Tk()
app = PDFToSpeechConverter(root)
root.mainloop()


