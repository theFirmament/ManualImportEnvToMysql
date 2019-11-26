# ManualImportEnvToMysql
手动输入环境变量，并存入数据库的python3程序

## 一.docker部署mysql5.7服务

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
  -e MYSQL_ROOT_PASSWORD="lqx20191125" \
  -e MYSQL_USER="cang" \
  -e MYSQL_PASSWORD="qiong" \
  -e MYSQL_DATABASES="campusEnv" \
  mysql:5.7 \
  --character-set-server=utf8mb4 \
  --collation-server=utf8mb4_unicode_ci \
  --lower-case-table-names=1
```






