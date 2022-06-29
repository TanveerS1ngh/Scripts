FROM kalilinux/kali-rolling

ENV BASE_DIR /kali

RUN apt-get update && apt-get install -y nmap nikto gobuster wpscan && apt-get clean

RUN mkdir -p $BASE_DIR

WORKDIR $BASE_DIR

COPY . .

CMD [ "/kali/Autoscan.sh" ]
