# PCL 1930 文档构建器

有问题请联系 @youzi-2333 或者凌云（

## 运行

Python 环境：Python 3.12+

```
usage: main.py [-h] [-o OUTPUT] [-d] [-e ENCODING] [-t TIMEOUT] [-p PROXY] [--ssl-no-revoke] [input]

PCL 1930 文档构建器。

positional arguments:
  input                 输入 Markdown 文件的位置或 URL。默认为 GitHub PCL2-1930 仓库中的 form/README.md 文件。

options:
  -h, --help            输出此帮助，然后退出。
  -o OUTPUT, --output OUTPUT
                        输出 Json 文件的位置。默认为 output.json。
  -d, --debug           启用调试模式。
  -e ENCODING, --encoding ENCODING
                        输入文件的编码。默认为 UTF-8。
  -t TIMEOUT, --timeout TIMEOUT
                        网络请求的超时时间（秒）。默认为 10 秒。
  -p PROXY, --proxy PROXY
                        请求 GitHub 时的代理服务器及端口。
  --ssl-no-revoke       请求服务器时，不校验 SSL 证书。
```

## 输出格式

```json
{
    "Minecraft": [
        {
            "catg": "Minecraft",
            "title": "无法下载 Minecraft",
            "q": "<strong>无法下载 Minecraft</strong>",
            "a": "<strong>为 MCBBS 关停所致，同时由于 BMCLAPI 源压力过大，可能导致大部分时间段无法通过镜像源下载 Minecraft。届时请尝试以下四种解决方案：<br>1. 更换不同的网络；<br>2. 每间隔一段时间后再次尝试下载；<br>3. 若您的网络条件允许，尝试使用加速器或 VPN；<br>4. 如个人技术能力允许，尝试部署 <a href=\"https://github.com/bangbang93/openbmclapi\">OpenBMCLAPI</a>。</strong> <br><br><em>部分日志可见：基础连接已经关闭: 未能为 SSL/TLS 安全通道建立信任关系。</em>",
            "ref": {
                "issue": [],
                "disc": [],
                "pull": [],
                "link": [
                    {
                        "text": "Bilibili&nbsp;动态",
                        "link": "https://t.bilibili.com/899749241434406921"
                    }
                ]
            }
        },
        {
            "catg": "Minecraft",
            "title": "1.16.4 及 1.16.5 离线模式无法进入多人游戏界面",
            "q": "<strong>1.16.4 及 1.16.5 离线模式无法进入多人游戏界面</strong>",
            "a": "<strong>PCL 不会解决该问题，这超出了启动器功能范畴。</strong> <br> <em>如仍需要使用多人游戏 [^1]，请自行断网启动游戏或安装 <a href=\"https://github.com/MCTeamPotato/MultiOfflineFix\" title=\"Fabric &amp; Forge\">MultiOfflineFix</a> 或 <a href=\"https://github.com/ChickenPige0n/offline-multiplayer-fabric\" title=\"仅 Fabric\">Offline Multiplayer</a> 模组。同时您可以参考<a href=\"https://github.com/Hex-Dragon/PCL2/discussions/1930#discussioncomment-6797858\">此处的解决方案</a>以彻底解决此问题。</em>",
            "ref": {
                "issue": [
                    "#2004"
                ],
                "disc": [
                    "#2003",
                    "#2017",
                    {
                        "text": "#1930",
                        "link": "https://github.com/Hex-Dragon/PCL2/discussions/1930#discussioncomment-6805733"
                    }
                ],
                "pull": [],
                "link": []
            }
        },
        {
            "catg": "Minecraft",
            "title": "游戏崩溃",
            "q": "游戏崩溃",
            "a": "请依照本文下方附文步骤进行解决。",
            "ref": {
                "issue": [],
                "disc": [],
                "pull": [],
                "link": []
            }
        }
    ],
    "PCL": [
        {
            "catg": "PCL",
            "title": "支持通过启动器联机游玩 Minecraft",
            "q": "<strong>支持通过启动器联机游玩 Minecraft</strong>",
            "a": "<strong><em>“至于联机，因为网易还在继续代理中国版，我和 HMCL 的维护者都觉得还得谨慎一点……况且现在也有 Mod 支持联机了……咳咳。”</em></strong> <br> <strong><em>“目前联机并不是遇到了技术问题。等到网易不代理国服了联机就有了”</em></strong> <br> <div align=\"right\"> <strong><em>——龙腾猫跃</em></strong> </div> <br> <em>BakaXL 现已于 2023 年 10 月 8 日将其部分服务与 Octo 章鱼网络进行对接，并对其可用性进行初步评估，待评估完成后，Octo 网络会全面对其他启动器开放。</em>[^4]",
            "ref": {
                "issue": [],
                "disc": [
                    "#4166",
                    {
                        "text": "#4158",
                        "link": "https://github.com/Hex-Dragon/PCL2/discussions/4158#discussioncomment-9968069"
                    }
                ],
                "pull": [],
                "link": [
                    {
                        "text": "2.6.11&nbsp;更新日志",
                        "link": "https://www.bilibili.com/read/cv28121157/"
                    }
                ]
            }
        },
        {
            "catg": "PCL",
            "title": "爱发电无法收到加群信息或更新密钥",
            "q": "爱发电无法收到加群信息或更新密钥",
            "a": "加群请 <strong>在爱发电</strong> 回复 “加群”，更新密钥 <strong>在爱发电</strong> 获取请回复 “‘更新’ +识别码”。如无法收到回复，很可能是您已经触发了人工回复，在等待人工回复的过程中无法使用命令。您如果只是想使用命令，可以发送 “取消人工处理”。如仍旧没有回复，可以等待一会后再进行尝试。",
            "ref": {
                "issue": [],
                "disc": [
                    "#1867"
                ],
                "pull": [],
                "link": [
                    {
                        "text": "石墨文档",
                        "link": "https://shimo.im/docs/qKPttVvXKqPD8YDC"
                    }
                ]
            }
        },
        {
            "catg": "PCL",
            "title": "支持识别、安装 Cleanroom",
            "q": "支持识别、安装 Cleanroom",
            "a": "正在 Discussions 中投票。",
            "ref": {
                "issue": [
                    "#3003"
                ],
                "disc": [
                    "#3004"
                ],
                "pull": [],
                "link": []
            }
        }
    ],
    "Hard": [
        {
            "catg": "Hard",
            "title": "因第三方组件引起的问题",
            "q": "因第三方组件引起的问题",
            "a": "PCL 不会处理第三方造成的问题。",
            "ref": {
                "issue": [],
                "disc": [],
                "pull": [],
                "link": [
                    {
                        "text": "Label:&nbsp;第三方",
                        "link": "https://github.com/Hex-Dragon/PCL2/issues?q=label%3A%E7%AC%AC%E4%B8%89%E6%96%B9+is%3Aclosed"
                    }
                ]
            }
        },
        {
            "catg": "Hard",
            "title": "因使用可编译开源版本导致的问题",
            "q": "因使用可编译开源版本导致的问题",
            "a": "因可编译版本可能经过了二次修改，因此此类版本造成的问题可能与 PCL 原版无关。",
            "ref": {
                "issue": [],
                "disc": [],
                "pull": [],
                "link": []
            }
        },
        {
            "catg": "Hard",
            "title": "因使用 32 位系统引起的问题",
            "q": "因使用 32 位系统引起的问题",
            "a": "新版 Minecraft 已不支持 32 位系统，因此不会再额外为 32 位进行修复和调整。",
            "ref": {
                "issue": [
                    {
                        "text": "#3649",
                        "link": "https://github.com/Hex-Dragon/PCL2/issues/3649#issuecomment-2047054821"
                    }
                ],
                "disc": [],
                "pull": [],
                "link": []
            }
        }
    ]
}
```