# Para que dado un documento, extraiga sus páginas

import pymupdf

def extract_pdf(path):
	document = pymupdf.open(path)

	pages = []

	# Almacenar el texto de las paginas con su numero de pagina
	for page_number, page in enumerate(document):
		text = page.get_text()

		pages.append({
			"page": page_number + 1,
			"text": text
		})

	document.close()

	return pages


