sudo mkdir -p /opt/maven
cd /opt/maven
MAVEN_VERSION=3.8.4
sudo curl -O "https://dlcdn.apache.org/maven/maven-3/3.8.4/binaries/apache-maven-3.8.4-bin.tar.gz"
sudo tar -xzvf "apache-maven-$MAVEN_VERSION-bin.tar.gz"
sudo rm "apache-maven-$MAVEN_VERSION-bin.tar.gz"
MAVEN_HOME="/opt/maven/apache-maven-$MAVEN_VERSION"
##在文件最后面追加一行 使用$a
sed -i '$aMAVEN_HOME="/opt/maven/apache-maven-3.8.4"' /home/ning/.bashrc
sed -i '$aPATH=$PATH:$MAVEN_HOME/bin' /home/ning/.bashrc
source /home/ning/.bashrc

##删除文件最后一行
#sed -i '$d' ~/.bashrc