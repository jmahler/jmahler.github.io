
linux-dev.pdf: linux-dev.tex main.bib
	pdflatex linux-dev.tex
	biber linux-dev
	pdflatex linux-dev.tex

clean:
	-rm -f *.out *.log *.blg *.bcf *.bbl *.aux *.xml *.toc
