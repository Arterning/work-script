LATEST=$(wget -q -O - http://chromedriver.storage.googleapis.com/LATEST_RELEASE)
mkdir tmp
cd tmp
wget http://chromedriver.storage.googleapis.com/$LATEST/chromedriver_linux64.zip

unzip chromedriver_linux64.zip
chmod +x chromedriver
sudo mv chromedriver /usr/bin/