import datetime
import pyttsx3
from PyPDF2 import PdfReader

print("File and the script should be in the same folder.")

file_name = input("Insert correct filename: ")
starting_page = input("Insert starting page number: ")
pages_to_avoid_at_the_end = input("Number of pages to remove at the end of the book: ")

file_name_with_extension = file_name + ".pdf"
reader = PdfReader(open(file_name_with_extension, 'rb'))
total_number_of_pages = len(reader.pages)

# remove 7 pages at the end of the book - for clean coder
without_indexes = total_number_of_pages - int(pages_to_avoid_at_the_end)

# for clean coder it is page number 23 is the starting page
clean_text = ""
for page_num in range(int(starting_page), without_indexes):
    page = reader.pages[page_num]
    text = page.extract_text()
    clean_text += text.strip().replace('\n', ' ')

print(f"Started creating audio")

speaker = pyttsx3.init()
audio_file_name = file_name + ".mp3"
speaker.save_to_file(clean_text, audio_file_name)
speaker.runAndWait()
speaker.stop()

print(f"Finished creating audio")