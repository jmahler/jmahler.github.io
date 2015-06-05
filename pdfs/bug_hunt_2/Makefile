
main.pdf: main.tex main.bib
	pdflatex $<
	biber $(basename $<)
	pdflatex $<

clean:
	-rm -f *.out *.log *.blg *.bcf *.bbl *.aux *.xml *.toc
