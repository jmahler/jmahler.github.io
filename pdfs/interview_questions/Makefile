
name=interview

$(name).pdf: $(name).tex main.bib
	pdflatex $(name).tex
	biber $(name)
	pdflatex $(name).tex

clean:
	-rm -f *.out *.log *.blg *.bcf *.bbl *.aux *.xml *.toc
