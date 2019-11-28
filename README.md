# ManualImportEnvToMysql
手动输入环境变量，并存入数据库的python3程序

## 一.docker部署mysql5.7服务
注:centos7.x系统安装docker环境等，这里不再赘述     
```
docker network create campus

mkdir /data

echo 'Asia/Shanghai' > /data/etc/timezone

docker run -d \
  --name lqxMysql \
  --net campus \
  --restart always \
  -p 3307:3306 \
  -v /etc/localtime:/etc/localtime:ro \
  -v /data/etc/timezone:/etc/timezone:ro \
  -v /lqxMysql:/var/lib/mysql:Z \
  -v /data/config/mysqld.cnf:/etc/mysql/mysql.conf.d/mysqld.cnf:Z \
  -e MYSQL_ROOT_PASSWORD="lqx20191125" \
  -e MYSQL_USER="ang" \
  -e MYSQL_PASSWORD="ong" \
  -e MYSQL_DATABASE="campusenv" \
  mysql:5.7 \
  --lower-case-table-names=1
```

## 二.创建存放部署变量的表
详见文件夹sqlFile        
向数据库导入表结构       
```
docker exec -i lqxMysql mysql -uroot -plqx20191125 -DcampusEnv < envSchool.sql
docker exec -i lqxMysql mysql -uroot -plqx20191125 -DcampusEnv < envclass.sql
```

## 三.python3语言实现终端输入学校部署环境变量存入数据库
详阅envToSql.py           

## 四.增加第三方库的文件
详阅requirements.txt
如若拷贝到其它地方，只需输入如下命令，即可一键安装项目所需要的第三方库
```angular2
pip3 install -r requirements.txt
```

## 五.其它功能待后续进一步开发