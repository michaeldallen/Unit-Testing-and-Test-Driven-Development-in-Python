IAM  := tdd
ACT  := venv.${IAM}/bin/activate
VENV := . ${ACT} &&

venv.${IAM} : venv.${IAM}/bin/activate requirements.txt
	${VENV} pip install --requirement requirements.txt
	touch $@

${ACT} :
	python3 -m venv venv.${IAM}
	${VENV} pip install --upgrade pip

clean : 
	rm -rfv venv.${IAM}

