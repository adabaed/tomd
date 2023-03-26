import os
import subprocess
import click
import re
import docx

@click.command()
@click.option('--input', '-i', required=True, help='Input PDF, plain text, or Word document file.')
@click.option('--output', '-o', required=True, help='Output Markdown file.')
def tomd(input, output):
    file_extension = os.path.splitext(input)[1].lower()

    if file_extension == '.pdf':
        text = extract_text_from_pdf(input)
    elif file_extension == '.txt':
        with open(input, 'r') as f:
            text = f.read()
    elif file_extension in ['.doc', '.docx']:
        text = extract_text_from_doc(input)
    else:
        click.echo("Error: Unsupported file type. Please provide a PDF, plain text, or Word document file.")
        return

    markdown_text = process_text_to_markdown(text)

    with open(output, 'w') as f:
        f.write(markdown_text)

    click.echo(f'Converted {input} to {output}')


def extract_text_from_pdf(pdf_path):
    output_path = 'temp_output.txt'

    with open(output_path, 'wb') as output_file:
        subprocess.run(['pdf2txt.py', pdf_path], stdout=output_file)

    with open(output_path, 'r') as input_file:
        text = input_file.read()

    os.remove(output_path)
    return text


def extract_text_from_doc(doc_path):
    doc = docx.Document(doc_path)
    text = []

    for paragraph in doc.paragraphs:
        text.append(paragraph.text)

    return '\n'.join(text)


def process_text_to_markdown(text):
    text = text.replace('\x0C', '')

    text = remove_page_numbers(text)

    return text


def remove_page_numbers(text):
    lines = text.split('\n')
    filtered_lines = []

    for line in lines:
        line = line.strip()

        if not re.match(r'^\d+$', line):
            filtered_lines.append(line)

    return '\n'.join(filtered_lines)


if __name__ == '__main__':
    tomd()
