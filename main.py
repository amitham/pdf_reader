import pyttsx3
from PyPDF2 import PdfReader


def print_message(message):
    print(message)


def get_input_value(message):
    input_value = input(message)
    return input_value


def get_clean_text(pdf_reader, pdf_starting_page, pdf_without_indexes):
    all_clean_text = ""
    for page_num in range(int(pdf_starting_page), pdf_without_indexes):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        all_clean_text += text.strip().replace('\n', ' ')
    return all_clean_text


def get_total_number_of_pages(total_pages, pages_to_avoid):
    return total_pages - int(pages_to_avoid)


def create_audio_file(file_name_without_extension, clean_text):
    speaker = pyttsx3.init()
    audio_file_name = file_name_without_extension + ".mp3"
    speaker.save_to_file(clean_text, audio_file_name)
    speaker.runAndWait()
    speaker.stop()


def read_pdf_file(file_name_without_extension):
    file_name_with_extension = file_name_without_extension + ".pdf"
    return PdfReader(open(file_name_with_extension, 'rb'))


def generate_audio_from_pdf():
    print_message("File and the script should be in the same folder.")

    file_name = get_input_value("Insert correct filename: ")
    starting_page = get_input_value("Insert starting page number: ")
    pages_to_avoid_at_the_end = get_input_value("Number of pages to remove at the end of the book: ")

    reader = read_pdf_file(file_name)
    total_number_of_pages = len(reader.pages)

    # remove 7 pages at the end of the book - for clean coder
    without_indexes = get_total_number_of_pages(total_number_of_pages, int(pages_to_avoid_at_the_end))

    # for clean coder it is page number 23 is the starting page
    clean_text = get_clean_text(reader, starting_page, without_indexes)

    print_message("Started creating audio")
    create_audio_file(file_name, clean_text)
    print_message("Finished creating audio")


generate_audio_from_pdf()