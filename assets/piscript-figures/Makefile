
all: projection-line-1.pdf projection-line-8.pdf projection-line-10.pdf projection-line-12.pdf projection-line-1.svg projection-line-8.svg projection-line-10.svg projection-line-12.svg

projection-line-%.eps: projection-line.py
	python projection-line.py

%.eps: %.py
	python $<

%.pdf: %.eps
	ps2pdf -dEPSCrop $<

%.svg: %.pdf
	pdf2svg $< $@

.PHONY: move

move:
	mv *.svg *.pdf ../images
