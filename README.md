# Redmine hook

## Introduction

It is used for converting the hook from [GitHub - suer/redmine\_webhook](https://github.com/suer/redmine_webhook) to [QQ Channel Bot](https://bot.q.qq.com/wiki/develop/api/openapi/message/post_messages.html)



## Usage



### Requirements

```
pip install -r requirements
```



### Run

export the environment and run

```shell
export CHANNEL_ID = 'xxx'
export BOT_TOKEN = 'xxx'
```



```shell
python hook.py
```



### Redmine Config

* Install [GitHub - suer/redmine\_webhook](https://github.com/suer/redmine_webhook) on your Redmine
* Configure the hook address in the project.



## Docker Run

build docker

```
docker build -t hook .
```



create a env.txt with the following content

```
CHANNEL_ID = 'xxx'
BOT_TOKEN = 'xxx'
```

start docker

```
docker run -d -p 3080:3080 --env-file=env.txt hook
```



