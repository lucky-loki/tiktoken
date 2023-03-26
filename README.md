## tiktoken
provide tiktok-py grpc call


### 启动

```shell
# 激活虚拟环境
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 前台启动
python main.py
python main.py --port=:50051

# 后台启动
nohup python main.py >log/server_errors.log 2>&1 & echo $! > pid

# 停止进程
kill -9 $(cat pid)
```