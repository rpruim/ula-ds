

all: \
projection-line-1.svg projection-line-8.svg projection-line-10.svg projection-line-12.svg \
projection-line-1.pdf projection-line-8.pdf projection-line-10.pdf projection-line-12.pdf \
3d-orthog-proj-3.svg \
3d-orthog-proj-3.pdf

all: $(SVGFILES) $(PDFFILES)

projection-line-1.eps: projection-line.py
	python projection-line.py

projection-line-8.eps: projection-line.py
	python projection-line.py

projection-line-10.eps: projection-line.py
	python projection-line.py

projection-line-12.eps: projection-line.py
	python projection-line.py

%.eps: %.py
	python $<

%.pdf: %.eps
	ps2pdf -dEPSCrop $<

%.svg: %.pdf
	pdf2svg $< $@

.PHONY: move

move:
	-mv *.svg *.pdf ../images

.PHONY: clean

clean: 
	-rm tmp*.aux tmp*.tex tmp*.log PiScript-tmp*