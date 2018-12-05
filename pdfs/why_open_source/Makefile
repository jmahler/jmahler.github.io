
NAME=why-open-source

${NAME}.pdf: ${NAME}.tex main.bib
	pdflatex $<
	biber ${NAME}
	pdflatex $<

clean:
	-rm -f *.out *.log *.blg *.bcf *.bbl *.aux *.xml *.toc
