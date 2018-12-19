### Description
参考: [The Flask Mega-Tutorial]
要看 Chapter 9
要整理 Chapter 4 Database 的脚本
### Migration Script
``` zsh
# 每次修改完 app/models.py 后, 都要运行 migrate 和 upgrade
flask db migrate -m "new fields in user model"  # -m 是添加说明
flask db upgrade
```
### Run
``` zsh
export FLASK_APP=microblog.py && flask run  # 开始运行
```
