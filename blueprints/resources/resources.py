from . import resource_bp
from quart import request, render_template, redirect, session, url_for, jsonify
from quart_auth import login_required


@resource_bp.route('/resources', methods=['POST', 'GET'])
@login_required
async def get_resources():
    if request.method == 'GET':
        return await render_template('resources/resources.html', title='资源列表')
    json = await request.get_json()
    page = json['page']
    if int(page) > 2:
        return jsonify({'code': 200, 'msg': 'false', 'data': '无更多数据'})
    data = [{
        "id": "10001",
        "author": "cck",
        "time": "2024-3-5 20:52",
        "title": "[原创] 关于函数调用链路trace的效果展示【仅供学习参考】",
        "classification": "iOS安全"
        },
        {
            "id": "10002",
            "author": "cck",
            "time": "2024-3-5 20:52",
            "title": "[原创]绕过爱奇艺新版libmsaoaidsec.so Frida检测",
            "classification": "Android安全"
        },
        {
            "id": "10003",
            "author": "cck",
            "time": "2024-3-5 20:52",
            "title": "[原创]DFA还原白盒AES密钥",
            "classification": "Android安全"
        },
        {
            "id": "10004",
            "author": "cck",
            "time": "2024-3-5 20:52",
            "title": "DEFCON-2023-Quals Blackbox 好玩的黑盒虚拟机代码执行",
            "classification": "CTF对抗"
        },
        {
            "id": "10005",
            "author": "cck",
            "time": "2024-3-5 20:52",
            "title": "[原创]Dobby框架源码学习",
            "classification": "Android安全"
        },
        {
            "id": "10006",
            "author": "cck",
            "time": "2024-3-5 20:52",
            "title": "[礼物]岁月沉淀二十四载，2024元宵大礼包，《看雪论坛精华24期》发布！",
            "classification": "茶余饭后"
        },
        {
            "id": "10007",
            "author": "cck",
            "time": "2024-3-5 20:52",
            "title": "[原创]初次漏洞分析--winrar(CVE-2023-38831)漏洞原理",
            "classification": "二进制漏洞"
        },
        {
            "id": "10008",
            "author": "cck",
            "time": "2024-3-5 20:52",
            "title": "CVE-2021-32760漏洞分析与复现",
            "classification": "二进制漏洞"
        },
        {
            "id": "10009",
            "author": "cck",
            "time": "2024-3-5 20:52",
            "title": "2023年工业控制网络安全态势白皮书",
            "classification": "茶余饭后"
        },
        {
            "id": "10010",
            "author": "cck",
            "time": "2024-3-5 20:52",
            "title": "[原创]记一次某汽车app白盒aes还原过程",
            "classification": "Android安全"
        },
        {
            "id": "10011",
            "author": "cck",
            "time": "2024-3-5 20:52",
            "title": "[原创]CS 4.4 二开笔记：beacon 指令分析篇",
            "classification": "软件逆向"
        },
        {
            "id": "10012",
            "author": "cck",
            "time": "2024-3-5 20:52",
            "title": "[原创]Directory Opus 13.2 逆向分析",
            "classification": "软件逆向"
        },
        {
            "id": "10013",
            "author": "cck",
            "time": "2024-3-5 20:52",
            "title": "[翻译]使用 Malcat 编写 Qakbot 5.0 配置提取器",
            "classification": "软件逆向"
        },
        {
            "id": "10014",
            "author": "cck",
            "time": "2024-3-5 20:52",
            "title": "[原创]对某旅行APP的检测以及参数计算分析【新手向-Simplesign篇】（二）",
            "classification": "Android安全"
        },
        {
            "id": "10015",
            "author": "cck",
            "time": "2024-3-5 20:52",
            "title": "[原创]安卓真机无root环境下的单机游戏修改-IL2CPP",
            "classification": "Android安全"
        },
        {
            "id": "10016",
            "author": "cck",
            "time": "2024-3-5 20:52",
            "title": "SVK1.3x脱壳笔记",
            "classification": "加壳脱壳"
        },
        {
            "id": "10017",
            "author": "cck",
            "time": "2024-3-5 20:52",
            "title": "bugku CTF 安卓逆向题目First_Mobile(xman)",
            "classification": "CTF对抗"
        }
    ]
    return jsonify({'code': 200, 'msg': 'success', 'data': data})
