"""
1. 编写一个TCP服务端程序，循环等待接受客户端的连接请求
2. 当客户端和服务端建立连接成功，创建子线程，使用子线程专门处理客户端的请求，防止主线程阻塞
3. 把创建的子线程设置成为守护线程，避免主线程结束时，子线程还在运行。
"""

# 导入socket依赖
import socket
import sys
from utils import decode_data
# 可以根据用户参数，设置服务器端口
args = sys.argv[1:]

# 创建TCP服务器socket
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定服务器ip和port
port = 8888
# print("port: ", port)
tcp_server.bind(("", port))

# 设置为被动模式，监听客户端的接入
tcp_server.listen(128)

print(f"服务器已启动，端口：{port}")
# 循环等待接受客户端的连接请求
tcp_client, tcp_client_addr = tcp_server.accept()
print(f"有新的客户端 {tcp_client_addr} 接入！")
while True:
    recv_data = tcp_client.recv(1024)
    if recv_data:
        msg = decode_data(recv_data)
        print(f"收到来自 {tcp_client_addr} 的消息：{msg}")
        tcp_client.send("消息已收到！")
    else:
        print("客户端已断开：", tcp_client_addr)
        break
        
tcp_server.close()