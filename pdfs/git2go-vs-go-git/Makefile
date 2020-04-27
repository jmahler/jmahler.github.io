
git2go-vs-go-git.pdf: main.pdf
	cp $< $@

main.pdf: main.tex main.bib
	pdflatex main.tex
	biber main
	pdflatex main.tex

clean:
	-rm -f *.out *.log *.blg *.bcf *.bbl *.aux *.xml *.toc
