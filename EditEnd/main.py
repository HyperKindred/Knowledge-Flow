from flask import Flask, request, jsonify
from flask_cors import CORS
from mindmap import *
import pymysql
import erniebot
import cv2
import os
import numpy as np
import re
import base64
import pathlib
import requests
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resource={r'/*': {'origins': '*'}})

with open("defaultStyle.json", "r", encoding="utf-8") as f:
    defaultStyle = f.read()
erniebot.api_type = 'aistudio'
erniebot.access_token = "85f4055523d16301b7b9eac2816814cee81d1238"

# 用户登录与注册
@app.route('/api/signIn', methods=["GET", "POST"])
def signIn():
    conn = pymysql.connect(
        host='127.0.0.1', 
        port=3306, 
        user='root', 
        password='Mysql123#', 
        charset='utf8', 
        autocommit=True
    )
    username = request.form.get("username")
    password = request.form.get("password")
    cursor = conn.cursor()
    cursor.execute("use KnowledgeFlow")
    sql = f"select password from userInfo where username = '{username}';"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result == None:
        data = {"ret": 1, "msg": "用户名不存在！"}
    elif password != result[0]:
        data = {"ret": 1, "msg": "密码错误！"}
    else:
        data = {"ret": 0}
    cursor.close()
    conn.close()
    return jsonify(data)

@app.route('/api/signUp', methods=["GET", "POST"])
def signUp():
    conn = pymysql.connect(
        host='127.0.0.1', 
        port=3306, 
        user='root', 
        password='Mysql123#', 
        charset='utf8', 
        autocommit=True
    )
    username = request.form.get("username")
    password = request.form.get("password")
    cursor = conn.cursor()
    cursor.execute("use KnowledgeFlow")
    sql = f"select username from userInfo where username = '{username}';"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result != None or username == "userInfo":
        data = {"ret": 1, "msg": "用户名已存在！"}
    else:
        sql = f"insert into userInfo(username, password) values('{username}', '{password}');"
        cursor.execute(sql)
        data = {"ret": 0}
    cursor.close()
    conn.close()
    return jsonify(data)

# 用户笔记数据库增删改查
@app.route('/api/pullNoteList', methods=["GET", "POST"])
def pullNoteList():
    conn = pymysql.connect(
        host='127.0.0.1', 
        port=3306, 
        user='root', 
        password='Mysql123#', 
        charset='utf8', 
        autocommit=True
    )
    cursor = conn.cursor()
    username = request.form.get("username")
    if username == None:
        conn.close()
        return jsonify({"ret": 1, "msg": "用户名不存在！"})
    cursor.execute("use KnowledgeFlow")
    cursor.execute("show tables;")
    result = cursor.fetchall()
    tables = [row[0] for row in result]
    if username not in tables:
        sql = f"create table `{username}`(id int unsigned auto_increment, noteName text, content longtext, styleId int unsigned, primary key ( `id` ));"
        cursor.execute(sql)
    cursor.execute(f"select * from `{username}`;")
    result = cursor.fetchall()
    if result == ():
        data = {"ret": 1, "msg": "笔记为空！"}
    else:
        data = {"ret": 0, "noteList": result}
    cursor.close()
    conn.close()
    return jsonify(data)

@app.route('/api/createNote', methods=["GET", "POST"])
def createNote():
    conn = pymysql.connect(
        host='127.0.0.1', 
        port=3306, 
        user='root', 
        password='Mysql123#', 
        charset='utf8', 
        autocommit=True
    )
    username = request.form.get("username")
    if username == None:
        conn.close()
        return jsonify({"ret": 1, "msg": "用户名不存在！"})
    cursor = conn.cursor()
    cursor.execute("use KnowledgeFlow")
    try:
        sql = f"insert into `{username}`(noteName, content, styleId) values('未命名页面', '开启知识之旅~', 1);"
        cursor.execute(sql)
    except:
        data = {"ret": 1, "msg":"创建新页面失败！"}
        conn.close()
        return jsonify(data)
    sql = f"select MAX(id) from `{username}`"
    cursor.execute(sql)
    id = cursor.fetchone()[0]
    data = {"ret": 0, "id":id}
    cursor.close()
    conn.close()
    return jsonify(data)

@app.route('/api/renameNote', methods=["GET", "POST"])
def renameNote():
    conn = pymysql.connect(
        host='127.0.0.1', 
        port=3306, 
        user='root', 
        password='Mysql123#', 
        charset='utf8', 
        autocommit=True
    )
    username = request.form.get("username")
    if username == None:
        conn.close()
        return jsonify({"ret": 1, "msg": "用户名不存在！"})
    cursor = conn.cursor()
    cursor.execute("use KnowledgeFlow")
    id = request.form.get("id")
    noteName = request.form.get("noteName")
    sql = f"select noteName from `{username}` where id = {int(id)};"    
    cursor.execute(sql)
    result = cursor.fetchone()
    if result == None:
        data = {"ret": 1, "msg":"目标笔记不存在！"}
    else:
        sql = f"update `{username}` set noteName = '{noteName}' where id = {int(id)};"
        cursor.execute(sql)
        data = {"ret": 0}
    cursor.close()
    conn.close()
    return jsonify(data)

@app.route('/api/delNote', methods=["GET", "POST"])
def delNote():
    conn = pymysql.connect(
        host='127.0.0.1', 
        port=3306, 
        user='root', 
        password='Mysql123#', 
        charset='utf8', 
        autocommit=True
    )
    username = request.form.get("username")
    if username == None:
        conn.close()
        return jsonify({"ret": 1, "msg": "用户名不存在！"})
    cursor = conn.cursor()
    cursor.execute("use KnowledgeFlow")
    id = request.form.get("id")
    sql = f"select noteName from `{username}` where id = {int(id)};"    
    cursor.execute(sql)
    result = cursor.fetchone()
    if result == None:
        data = {"ret": 1, "msg":"目标笔记不存在！"}
    else:
        sql = f"delete from `{username}` where id = {int(id)};"
        cursor.execute(sql)
        data = {"ret": 0}
    cursor.close()
    conn.close()
    return jsonify(data)

@app.route('/api/saveNote', methods=["GET", "POST"])
def saveNote():
    conn = pymysql.connect(
        host='127.0.0.1', 
        port=3306, 
        user='root', 
        password='Mysql123#', 
        charset='utf8', 
        autocommit=True
    )
    username = request.form.get("username")
    id = request.form.get("id")
    note = request.form.get("note")
    styleId = request.form.get("styleId")
    if username == None:
        conn.close()
        return jsonify({"ret": 1, "msg": "用户名不存在！"})
    cursor = conn.cursor()
    cursor.execute("use KnowledgeFlow")
    sql = f"select noteName from `{username}` where id = {int(id)};"    
    cursor.execute(sql)
    result = cursor.fetchone()
    if result == None:
        data = {"ret": 1, "msg":"目标笔记不存在！"}
    else:
        sql = f"update `{username}` set content = '{note}' where id = {int(id)};"
        cursor.execute(sql)
        sql = f"update `{username}` set styleId = '{int(styleId)}' where id = {int(id)};"
        cursor.execute(sql)
        data = {"ret": 0}
    cursor.close()
    conn.close()
    return jsonify(data)

# 用户样式数据库增删改查
@app.route('/api/pullStyleList', methods=["GET", "POST"])
def pullStyleList():
    conn = pymysql.connect(
        host='127.0.0.1', 
        port=3306, 
        user='root', 
        password='Mysql123#', 
        charset='utf8', 
        autocommit=True
    )
    cursor = conn.cursor()
    username = request.form.get("username")
    if username == None:
        conn.close()
        return jsonify({"ret": 1, "msg": "用户名不存在！"})
    cursor.execute("use KLFStyle")
    cursor.execute("show tables;")
    result = cursor.fetchall()
    tables = [row[0] for row in result]    
    if username not in tables:
        sql = f"create table `{username}`(id int unsigned auto_increment, styleName text, style longtext, primary key ( `id` ));"
        cursor.execute(sql)
        sql = f"insert into `{username}`(styleName, style) values('默认样式', '{defaultStyle}');"
        cursor.execute(sql)
    cursor.execute(f"select * from `{username}`;")
    result = cursor.fetchall()
    if result == ():
        data = {"ret": 1, "msg": "样式为空！"}
    else:
        data = {"ret": 0, "styleList": result}
    cursor.close()
    conn.close()
    return jsonify(data)

@app.route('/api/createStyle', methods=["GET", "POST"])
def createStyle():
    conn = pymysql.connect(
        host='127.0.0.1', 
        port=3306, 
        user='root', 
        password='Mysql123#', 
        charset='utf8', 
        autocommit=True
    )
    username = request.form.get("username")
    if username == None:
        conn.close()
        return jsonify({"ret": 1, "msg": "用户名不存在！"})
    cursor = conn.cursor()
    cursor.execute("use KLFStyle")
    try:
        sql = f"insert into `{username}`(styleName, style) values('默认样式', '{defaultStyle}');"
        cursor.execute(sql)
    except:
        data = {"ret": 1, "msg":"创建新样式失败！"}
        conn.close()
        return jsonify(data)
    sql = f"select MAX(id) from `{username}`"
    cursor.execute(sql)
    id = cursor.fetchone()[0]
    data = {"ret": 0, "id":id}
    cursor.close()
    conn.close()
    return jsonify(data)

@app.route('/api/renameStyle', methods=["GET", "POST"])
def renameStyle():
    conn = pymysql.connect(
        host='127.0.0.1', 
        port=3306, 
        user='root', 
        password='Mysql123#', 
        charset='utf8', 
        autocommit=True
    )
    username = request.form.get("username")
    if username == None:
        conn.close()
        return jsonify({"ret": 1, "msg": "用户名不存在！"})
    cursor = conn.cursor()
    cursor.execute("use KLFStyle")
    id = request.form.get("id")
    styleName = request.form.get("styleName")
    sql = f"select styleName from `{username}` where id = {int(id)};"    
    cursor.execute(sql)
    result = cursor.fetchone()
    if result == None:
        data = {"ret": 1, "msg":"目标样式不存在！"}
    else:
        sql = f"update `{username}` set styleName = '{styleName}' where id = {int(id)};"
        cursor.execute(sql)
        data = {"ret": 0}
    cursor.close()
    conn.close()
    return jsonify(data)

@app.route('/api/delStyle', methods=["GET", "POST"])
def delStyle():
    conn = pymysql.connect(
        host='127.0.0.1', 
        port=3306, 
        user='root', 
        password='Mysql123#', 
        charset='utf8', 
        autocommit=True
    )
    username = request.form.get("username")
    if username == None:
        conn.close()
        return jsonify({"ret": 1, "msg": "用户名不存在！"})
    cursor = conn.cursor()
    cursor.execute("use KLFStyle")
    id = request.form.get("id")
    sql = f"select styleName from `{username}` where id = {int(id)};"    
    cursor.execute(sql)
    result = cursor.fetchone()
    if result == None:
        data = {"ret": 1, "msg":"目标样式不存在！"}
    else:
        sql = f"delete from `{username}` where id = {int(id)};"
        cursor.execute(sql)
        data = {"ret": 0}
    cursor.close()
    conn.close()
    return jsonify(data)

@app.route('/api/saveStyle', methods=["GET", "POST"])
def saveStyle():
    conn = pymysql.connect(
        host='127.0.0.1', 
        port=3306, 
        user='root', 
        password='Mysql123#', 
        charset='utf8', 
        autocommit=True
    )
    username = request.form.get("username")
    id = request.form.get("id")
    style = request.form.get("style")
    if username == None:
        conn.close()
        return jsonify({"ret": 1, "msg": "用户名不存在！"})
    cursor = conn.cursor()
    cursor.execute("use KLFStyle")
    sql = f"select styleName from `{username}` where id = {int(id)};"    
    cursor.execute(sql)
    result = cursor.fetchone()
    if result == None:
        data = {"ret": 1, "msg":"目标样式不存在！"}
    else:
        sql = f"update `{username}` set style = '{style}' where id = {int(id)};"
        cursor.execute(sql)
        data = {"ret": 0}
    cursor.close()
    conn.close()
    return jsonify(data)

# 大模型功能，摘要、润色、翻译、病句改写
@app.route('/api/summarize', methods=["GET", "POST"])
def summarize():
    text = request.form.get("text")
    askcont="请帮我提取这段话的摘要："+text
    try:
        response = erniebot.ChatCompletion.create(
            model='ernie-bot',
            messages=[{'role': 'user', 'content':askcont}],
        )
        res = response['result']
        index = res.find("：")
        if index == -1:
            data = {"ret": 1, "msg":"模型返回结果异常！"}
        else:
            res = res[index+1:].strip()
            data = {"ret": 0, "res":res}
    except:
        data = {"ret": 1, "msg":"模型调用失败！"}
    return jsonify(data)

@app.route('/api/polish', methods=["GET", "POST"])
def polish():
    text = request.form.get("text")
    askcont="帮我润色下面这段话，直接输出结果:"+text
    try:
        response = erniebot.ChatCompletion.create(
            model='ernie-bot',
            messages=[{'role': 'user', 'content':askcont}],
        )
        res = response['result']
        data = {"ret": 0, "res":res}
    except:
        data = {"ret": 1, "msg":"模型调用失败！"}
    return jsonify(data)

@app.route('/api/translate', methods=["GET", "POST"])
def translate():
    text = request.form.get("text")
    mode = request.form.get("mode")
    mode = int(mode)
    if mode == 0:
        askcont="中译英（格式要求结果前添加“输出：”）："+text
    elif mode == 1:
        askcont="英译中（格式要求结果前添加“输出：”）："+text
    else:
        data = {"ret": 1, "msg":"翻译模式错误！"}
        return jsonify(data)
    try:
        response = erniebot.ChatCompletion.create(
            model='ernie-bot',
            messages=[{'role': 'user', 'content':askcont}],
        )
        res = response['result']
        index = res.find("：")
        if index == -1:
            data = {"ret": 1, "msg":"模型返回结果异常！"}
        else:
            res = res[index+1:].strip()
            data = {"ret": 0, "res":res}
    except:
        data = {"ret": 1, "msg":"模型调用失败！"}
    return jsonify(data)

@app.route('/api/correct', methods=["GET", "POST"])
def correct():
    text = request.form.get("text")
    askcont="请帮我纠正这段话可能存在的错误（不需要解释，如果原句正确直接输出原句，格式：输出：）："+text
    try:
        response = erniebot.ChatCompletion.create(
            model='ernie-bot',
            messages=[{'role': 'user', 'content':askcont}],
        )
        res = response['result']
        index = res.find("：")
        if index == -1:
            data = {"ret": 1, "msg":"模型返回结果异常！"}
        else:
            res = res[index+1:].strip()
            data = {"ret": 0, "res":res}
    except:
        data = {"ret": 1, "msg":"模型调用失败！"}
    return jsonify(data)

@app.route('/api/img2word', methods=["GET", "POST"])
def img2word():
    API_URL = "https://n0p3ybs0m36ce8w7.aistudio-hub.baidu.com/ocr"
    TOKEN = "85f4055523d16301b7b9eac2816814cee81d1238"

    # 设置鉴权信息
    headers = {
        "Authorization": f"token {TOKEN}",
        "Content-Type": "application/json"
    }

    res = []
    username = request.form.get("username")
    img = request.files['img']
    picname=img.filename
    file = img.read()

    file = cv2.imdecode(np.frombuffer(file, np.uint8), cv2.IMREAD_COLOR)  # 解码为ndarray
    imgfilePath = "./static/images/" + username + "/"

    if not os.path.exists(imgfilePath):
        os.makedirs(imgfilePath)
    imgPath = os.path.join(imgfilePath, picname)
    cv2.imwrite(filename=imgPath, img=file)

    imgPath=imgfilePath+picname

    # 对本地图片进行Base64编码
    image_path = imgPath
    image_bytes = pathlib.Path(image_path).read_bytes()
    image_base64 = base64.b64encode(image_bytes).decode('ascii')

    # 设置请求体
    payload = {
        "image": image_base64  # Base64编码的文件内容或者文件链接
    }

    # 调用
    resp = requests.post(url=API_URL, json=payload, headers=headers)

    # 处理接口返回数据
    if resp.status_code != 200:
        return jsonify({"ret":0, "img":"模型调用失败！"})
    result = resp.json()["result"]
    result = result["texts"]
    for line in result:
        res.append(line["text"])
    data = {"ret":0, "res":res}
    return jsonify(data)

# 一键生成格式
@app.route('/api/autoFormat', methods=["GET", "POST"])
def autoFormat():
    text = request.form.get("text")
    askcont="请帮我将下面的html添加格式，直接输出html代码，不需要解释（尽量保持原有html层级结构不变，对于正文部分，有选择性地根据内容自动提取摘要并且设置符合原有层级的小标题，可以使用加粗、斜体、代码、引用、有序列表、无序列表等）："+text
    try:
        response = erniebot.ChatCompletion.create(
            model='ernie-bot',
            messages=[{'role': 'user', 'content':askcont}],
        )
        res = response['result']
        pattern = r"```html\n(.*?)```"
        try:
            results = re.findall(pattern, res, re.DOTALL)
            res = results[0].replace("\n", " ")
            data = {"ret": 0, "res":res}
        except: 
            return jsonify({"ret": 1, "msg":"模型输出结果异常！"})
    except:
        data = {"ret": 1, "msg":"模型调用失败！"}
    return jsonify(data)

# 文本导出思维导图
@app.route('/api/autoMindmap', methods=["GET", "POST"])
def autoMindmap():
    noteName = request.form.get("noteName")
    text = request.form.get("text")
    try:
        mindmap_json = parse_html_to_mindmap(text, noteName)
    except:
        return jsonify({"ret": 1, "msg": "生成思维导图失败！"})
    data = {"ret": 0, "res": mindmap_json}
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
