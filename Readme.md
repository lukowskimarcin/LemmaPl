docker run -v C:/Users/themo/Desktop/LemmaPl:/root/test -it ipipan/langtools-all /bin/bash
cd /root/lemmapl
python lemmapl.py ../test/test.txt > /root/test/out.xml

