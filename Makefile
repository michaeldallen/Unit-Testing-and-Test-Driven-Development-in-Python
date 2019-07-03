IAM  := tdd
VENV := venv.${IAM}/bin/activate
ACT  := . ${VENV} &&

venv.${IAM} : ${VENV} requirements.txt
	touch $@

${VENV} :
	python3 -m venv venv.${IAM}
	${ACT} pip install --upgrade pip
	${ACT} pip install --requirement requirements.txt

test : ${VENV}
	${ACT} pytest

clean : 
	rm -rfv venv.${IAM}
	find * -name '*~' | sort | xargs -L 1 rm -v

