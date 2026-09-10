# Config_Self

个人精选分流规则镜像，数据主要来自 [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script)。

> 我们并不生产规则，我们只是开源规则的搬运工。

本仓库只保留自己实际在用的 Clash / Surge 规则，每周一自动从上游同步，并用 overlay 保留本地补丁（例如 HBO 额外域名）。

- 上游协议：[GPL-2.0](LICENSE)
- 镜像说明：[NOTICE](NOTICE)
- 同步清单：[source/manifest.json](source/manifest.json)

## 订阅地址

将下面的 Raw 链接填进 Clash / Surge 的规则集即可。

基础路径：

```
https://raw.githubusercontent.com/chentanwan/Config_Self/main/
```

### Clash (`rule-providers` / `payload`)

| 规则 | Raw |
| --- | --- |
| Apple | [Apple.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Apple.yaml) |
| AppleTV | [AppleTV.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/AppleTV.yaml) |
| Bahamut | [Bahamut.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Bahamut.yaml) |
| ChinaMax Classical | [ChinaMax_Classical.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/ChinaMax_Classical.yaml) |
| ChinaMedia | [ChinaMedia.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/ChinaMedia.yaml) |
| Disney | [Disneyplus.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Disneyplus.yaml) |
| Discord | [Discord.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Discord.yaml) |
| Download | [Download.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Download.yaml) |
| Emby | [Emby.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Emby.yaml) |
| Global | [Global.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Global.yaml) |
| Google | [Google.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Google.yaml) |
| GoogleVoice | [GoogleVoice.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/GoogleVoice.yaml) |
| HBO | [HBO.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/HBO.yaml) |
| Microsoft | [Microsoft.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Microsoft.yaml) |
| Netflix | [Netflix.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Netflix.yaml) |
| OneDrive | [OneDrive.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/OneDrive.yaml) |
| OpenAI | [OpenAI.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/OpenAI.yaml) |
| PayPal | [PayPal.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/PayPal.yaml) |
| Spotify | [Spotify.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Spotify.yaml) |
| SteamCN（国服，文件名 `Steam.yaml` 兼容旧订阅） | [Steam.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Steam.yaml) |
| SteamCN | [SteamCN.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/SteamCN.yaml) |
| Steam（国际） | [SteamGlobal.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/SteamGlobal.yaml) |
| Telegram | [Telegram.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Telegram.yaml) |
| Twitch | [Twitch.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Twitch.yaml) |
| Twitter / X | [Twitter.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Twitter.yaml) |
| WeChat | [WeChat.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/WeChat.yaml) |
| Whatsapp | [Whatsapp.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Whatsapp.yaml) |
| YouTube | [YouTube.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/YouTube.yaml) |

Clash 示例：

```yaml
rule-providers:
  openai:
    type: http
    behavior: classical
    url: "https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/OpenAI.yaml"
    path: ./ruleset/openai.yaml
    interval: 86400
```

> Clash 非 `_Classical` 文件沿用上游精简格式（常见是 keyword / IP / process，DOMAIN-SUFFIX 不一定全部展开）。需要完整 DOMAIN-SUFFIX 时请用 `ChinaMax_Classical.yaml` 这类 Classical 文件，或直接订阅 [blackmatrix7](https://github.com/blackmatrix7/ios_rule_script)。

### Surge (`RULE-SET`)

| 规则 | Raw |
| --- | --- |
| Apple | [Apple.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Apple.list) |
| Bahamut | [Bahamut.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Bahamut.list) |
| ChinaMax | [ChinaMax.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/ChinaMax.list) |
| Discord | [Discord.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Discord.list) |
| Disney | [Disney.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Disney.list) |
| Disney+ 登录（本地） | [DisneyPlus_dl.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/DisneyPlus_dl.list) |
| Disney+ 观看（本地） | [Disneyplus.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Disneyplus.list) |
| Download | [Download.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Download.list) |
| Emby | [Emby.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Emby.list) |
| Google | [Google.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Google.list) |
| GoogleVoice | [Googlevoice.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Googlevoice.list) |
| HBO | [HBO.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/HBO.list) |
| HBO Asia | [HBO_asia.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/HBO_asia.list) |
| HBO USA | [HBO_usa.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/HBO_usa.list) |
| Microsoft | [Microsoft.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Microsoft.list) |
| Netflix | [Netflix.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Netflix.list) |
| OneDrive | [Onedrive.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Onedrive.list) |
| OpenAI | [OpenAI.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/OpenAI.list) |
| PayPal | [PayPal.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/PayPal.list) |
| Spotify | [Spotify.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Spotify.list) |
| Telegram | [Telegram.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Telegram.list) |
| Twitter / X | [Twitter.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Twitter.list) |
| Twitch | [twitch.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/twitch.list) |
| WeChat | [WeChat.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/WeChat.list) |
| Whatsapp | [Whatsapp.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Whatsapp.list) |
| YouTube | [YouTube.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/YouTube.list) |

Surge 示例：

```ini
RULE-SET,https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/OpenAI.list,OpenAI
```

## 本地补丁

| 文件 | 说明 |
| --- | --- |
| [source/overlays/HBO.txt](source/overlays/HBO.txt) | 同步 HBO 时合并的额外域名（appsflyer / branch / Max 相关） |
| `rule/Surge/Disneyplus.list` | 本地「观看」规则，不同步覆盖 |
| `rule/Surge/DisneyPlus_dl.list` | 本地「登录」规则，不同步覆盖 |

历史 HBO 文件里有一条非法规则 `DOMAIN,SUFFIX,appsflyersdk.com`，已改为 `DOMAIN-SUFFIX`。

## 维护

```bash
# 从 blackmatrix7 拉取并合并 overlay
python3 scripts/sync.py

# 只同步某个名字
python3 scripts/sync.py --only OpenAI

# 语法 / 空文件 / 重复项 / DOMAIN,SUFFIX 校验
python3 scripts/validate.py
```

GitHub Actions：

- [CI](.github/workflows/ci.yml)：push / PR 跑 `validate.py`
- [Sync](.github/workflows/sync.yml)：每周一 03:17 UTC 自动同步并提交；也可在 Actions 里手动 `workflow_dispatch`

新增规则：在 `source/manifest.json` 的 `rules` 里加一条 `local` + `remote`，然后跑 `sync.py`。需要额外域名时在 `source/overlays/` 放一份 Surge 格式列表，并在 manifest 里写 `"overlay": "source/overlays/Foo.txt"`。

## 声明

规则数据来自互联网开源项目（主要为 blackmatrix7），仅供学习研究。使用后果由使用者自行承担。完整规则集、Loon / Quantumult X / Shadowrocket / 复写规则请直接使用上游仓库。
