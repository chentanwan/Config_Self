# Config_Self

个人精选分流规则镜像，数据主要来自 [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script)。

> 我们并不生产规则，我们只是开源规则的搬运工。

本仓库只保留自用 Clash / Surge 规则，每周一自动从上游同步，并用 overlay 补上游没有的域名。

- 上游协议：[GPL-2.0](LICENSE)
- 镜像说明：[NOTICE](NOTICE)
- 同步清单：[source/manifest.json](source/manifest.json)

Raw 基础路径：

```
https://raw.githubusercontent.com/chentanwan/Config_Self/main/
```

Clash `behavior: classical`，Surge 用 `RULE-SET`。

```yaml
rule-providers:
  ai:
    type: http
    behavior: classical
    url: "https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/AI.yaml"
    path: ./ruleset/ai.yaml
    interval: 86400
```

```ini
RULE-SET,https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/AI.list,AI
```

> Clash 非 `_Classical` 文件沿用上游精简格式（常见是 keyword / IP / process）。需要完整 DOMAIN-SUFFIX 时用 `ChinaMax_Classical.yaml`，或直接订阅 [blackmatrix7](https://github.com/blackmatrix7/ios_rule_script)。

下面链接均为 Raw。每个集合同时提供 Clash YAML 和 Surge list。

## 加密交易所 / Crypto

上游 `Crypto` + `Cryptocurrency` 已覆盖 Binance / OKX / Bybit / Coinbase / Kraken / Gate / MEXC 等；Bitget 及部分 Gate/Bybit CDN 由 overlay 补齐。单所规则可单独订阅。

| 集合 | 说明 | Clash | Surge |
| --- | --- | --- | --- |
| **Crypto** | 交易所+DEX 聚合（推荐） | [Crypto.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Crypto.yaml) | [Crypto.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Crypto.list) |
| Cryptocurrency | 上游精简交易所表 | [Cryptocurrency.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Cryptocurrency.yaml) | [Cryptocurrency.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Cryptocurrency.list) |
| Binance | 币安 | [Binance.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Binance.yaml) | [Binance.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Binance.list) |
| OKX | OKX / OKEx | [OKX.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/OKX.yaml) | [OKX.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/OKX.list) |

## Web3 钱包 / DEX

上游没有独立的 Bitget Wallet / Rainbow / GMGN / Tangem / Base 规则，本仓库用本地 overlay 做成 `Web3`。

| 集合 | 说明 | Clash | Surge |
| --- | --- | --- | --- |
| **Web3** | Binance/OKX/Bitget Wallet、Rainbow、Phantom、MetaMask、Uniswap、Base、GMGN、Tangem、WalletConnect | [Web3.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Web3.yaml) | [Web3.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Web3.list) |

## AI

| 集合 | 说明 | Clash | Surge |
| --- | --- | --- | --- |
| **AI** | OpenAI/ChatGPT + Claude + Gemini + Copilot 聚合，叠加 Cursor / Grok / xAI | [AI.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/AI.yaml) | [AI.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/AI.list) |
| OpenAI | ChatGPT / OpenAI | [OpenAI.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/OpenAI.yaml) | [OpenAI.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/OpenAI.list) |
| Claude | claude.ai | [Claude.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Claude.yaml) | [Claude.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Claude.list) |
| Anthropic | Anthropic 官网 | [Anthropic.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Anthropic.yaml) | [Anthropic.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Anthropic.list) |
| Gemini | Google Gemini / AI Studio | [Gemini.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Gemini.yaml) | [Gemini.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Gemini.list) |
| BardAI | 旧 Bard 规则（并入 Gemini） | [BardAI.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/BardAI.yaml) | [BardAI.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/BardAI.list) |
| Copilot | Microsoft Copilot（含部分 OpenAI） | [Copilot.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Copilot.yaml) | [Copilot.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Copilot.list) |

## 国外流媒体

| 集合 | Clash | Surge |
| --- | --- | --- |
| **GlobalMedia** 聚合 | [GlobalMedia.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/GlobalMedia.yaml) | [GlobalMedia.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/GlobalMedia.list) |
| Netflix | [Netflix.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Netflix.yaml) | [Netflix.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Netflix.list) |
| Disney | [Disneyplus.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Disneyplus.yaml) | [Disney.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Disney.list) |
| Disney+ 登录（本地） | — | [DisneyPlus_dl.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/DisneyPlus_dl.list) |
| Disney+ 观看（本地） | — | [Disneyplus.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Disneyplus.list) |
| HBO | [HBO.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/HBO.yaml) | [HBO.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/HBO.list) |
| HBO Asia / USA / HK | [HBOAsia](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/HBOAsia.yaml) / [HBOUSA](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/HBOUSA.yaml) / [HBOHK](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/HBOHK.yaml) | [HBO_asia](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/HBO_asia.list) / [HBO_usa](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/HBO_usa.list) / [HBOHK](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/HBOHK.list) |
| Amazon | [Amazon.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Amazon.yaml) | [Amazon.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Amazon.list) |
| Amazon Prime Video | [AmazonPrimeVideo.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/AmazonPrimeVideo.yaml) | [AmazonPrimeVideo.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/AmazonPrimeVideo.list) |
| Prime Video | [PrimeVideo.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/PrimeVideo.yaml) | [PrimeVideo.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/PrimeVideo.list) |
| Spotify | [Spotify.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Spotify.yaml) | [Spotify.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Spotify.list) |
| YouTube | [YouTube.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/YouTube.yaml) | [YouTube.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/YouTube.list) |
| Twitch | [Twitch.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Twitch.yaml) | [twitch.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/twitch.list) |
| Hulu / HuluUSA | [Hulu](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Hulu.yaml) / [HuluUSA](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/HuluUSA.yaml) | [Hulu](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Hulu.list) / [HuluUSA](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/HuluUSA.list) |
| Paramount+ | [ParamountPlus.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/ParamountPlus.yaml) | [ParamountPlus.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/ParamountPlus.list) |
| Discovery+ | [DiscoveryPlus.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/DiscoveryPlus.yaml) | [DiscoveryPlus.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/DiscoveryPlus.list) |
| Bahamut | [Bahamut.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Bahamut.yaml) | [Bahamut.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Bahamut.list) |
| Emby | [Emby.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Emby.yaml) | [Emby.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Emby.list) |

## 国内服务

| 集合 | 说明 | Clash | Surge |
| --- | --- | --- | --- |
| **ChinaMax Classical** | 国内大全（体积大） | [ChinaMax_Classical.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/ChinaMax_Classical.yaml) | [ChinaMax.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/ChinaMax.list) |
| China / ChinaMedia | 国内通用 / 国内流媒体 | [China](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/China.yaml) / [ChinaMedia](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/ChinaMedia.yaml) | [China](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/China.list) / [ChinaMedia](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/ChinaMedia.list) |
| 爱奇艺 / 优酷 / 腾讯视频 / 哔哩哔哩 / 咪咕 | 爱优腾 + B 站 | [iQIYI](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/iQIYI.yaml) / [Youku](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Youku.yaml) / [TencentVideo](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/TencentVideo.yaml) / [BiliBili](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/BiliBili.yaml) / [Migu](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Migu.yaml) | [iQIYI](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/iQIYI.list) / [Youku](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Youku.list) / [TencentVideo](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/TencentVideo.list) / [BiliBili](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/BiliBili.list) / [Migu](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Migu.list) |
| 腾讯系 | Tencent / WeChat | [Tencent](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Tencent.yaml) / [WeChat](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/WeChat.yaml) | [Tencent](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Tencent.list) / [WeChat](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/WeChat.list) |
| 阿里系 | Alibaba / AliPay | [Alibaba](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Alibaba.yaml) / [AliPay](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/AliPay.yaml) | [Alibaba](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Alibaba.list) / [AliPay](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/AliPay.list) |
| 华为 / 小米 / OPPO / vivo | 厂商云与账号 | [Huawei](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Huawei.yaml) / [XiaoMi](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/XiaoMi.yaml) / [OPPO](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/OPPO.yaml) / [Vivo](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Vivo.yaml) | [Huawei](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Huawei.list) / [XiaoMi](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/XiaoMi.list) / [OPPO](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/OPPO.list) / [Vivo](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Vivo.list) |
| 字节 / 抖音 / 快手 / 小红书 / 微博 / 钉钉 | 内容与社交 | [ByteDance](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/ByteDance.yaml) / [DouYin](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/DouYin.yaml) / [KuaiShou](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/KuaiShou.yaml) / [XiaoHongShu](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/XiaoHongShu.yaml) / [Weibo](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Weibo.yaml) / [DingTalk](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/DingTalk.yaml) | [ByteDance](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/ByteDance.list) / [DouYin](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/DouYin.list) / [KuaiShou](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/KuaiShou.list) / [XiaoHongShu](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/XiaoHongShu.list) / [Weibo](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Weibo.list) / [DingTalk](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/DingTalk.list) |
| 百度 / 京东 / 网易 | | [Baidu](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Baidu.yaml) / [JingDong](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/JingDong.yaml) / [NetEase](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/NetEase.yaml) | [Baidu](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Baidu.list) / [JingDong](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/JingDong.list) / [NetEase](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/NetEase.list) |

## 社交平台

| 集合 | Clash | Surge |
| --- | --- | --- |
| Telegram | [Telegram.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Telegram.yaml) | [Telegram.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Telegram.list) |
| Whatsapp | [Whatsapp.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Whatsapp.yaml) | [Whatsapp.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Whatsapp.list) |
| Facebook | [Facebook.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Facebook.yaml) | [Facebook.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Facebook.list) |
| Instagram | [Instagram.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Instagram.yaml) | [Instagram.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Instagram.list) |
| Threads | [Threads.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Threads.yaml) | [Threads.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Threads.list) |
| Twitter / X | [Twitter.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Twitter.yaml) | [Twitter.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Twitter.list) |
| Discord | [Discord.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Discord.yaml) | [Discord.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Discord.list) |
| Snap | [Snap.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Snap.yaml) | [Snap.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Snap.list) |
| Line | [Line.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Line.yaml) | [Line.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Line.list) |
| Reddit | [Reddit.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Reddit.yaml) | [Reddit.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Reddit.list) |
| TikTok | [TikTok.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/TikTok.yaml) | [TikTok.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/TikTok.list) |
| LinkedIn | [LinkedIn.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/LinkedIn.yaml) | [LinkedIn.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/LinkedIn.list) |

## 苹果 / 微软（含国内节点相关）

| 集合 | Clash | Surge |
| --- | --- | --- |
| Apple | [Apple.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Apple.yaml) | [Apple.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Apple.list) |
| AppleProxy（走代理的苹果服务） | [AppleProxy.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/AppleProxy.yaml) | [AppleProxy.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/AppleProxy.list) |
| AppleMedia / AppleMusic / AppleTV / AppleID / iCloud | [AppleMedia](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/AppleMedia.yaml) / [AppleMusic](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/AppleMusic.yaml) / [AppleTV](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/AppleTV.yaml) / [AppleID](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/AppleID.yaml) / [iCloud](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/iCloud.yaml) | [AppleMedia](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/AppleMedia.list) / [AppleMusic](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/AppleMusic.list) / [AppleTV](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/AppleTV.list) / [AppleID](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/AppleID.list) / [iCloud](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/iCloud.list) |
| Microsoft / Edge / Teams / OneDrive | [Microsoft](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Microsoft.yaml) / [MicrosoftEdge](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/MicrosoftEdge.yaml) / [Teams](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Teams.yaml) / [OneDrive](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/OneDrive.yaml) | [Microsoft](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Microsoft.list) / [MicrosoftEdge](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/MicrosoftEdge.list) / [Teams](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Teams.list) / [Onedrive](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Onedrive.list) |
| Google / GoogleVoice | [Google](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Google.yaml) / [GoogleVoice](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/GoogleVoice.yaml) | [Google](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Google.list) / [Googlevoice](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Googlevoice.list) |
| PayPal | [PayPal.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/PayPal.yaml) | [PayPal.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/PayPal.list) |
| SteamCN / Steam 国际 | [Steam.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Steam.yaml)（国服兼容名） / [SteamGlobal.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/SteamGlobal.yaml) | — |

## 本地补丁

| 文件 | 说明 |
| --- | --- |
| [source/overlays/Crypto.txt](source/overlays/Crypto.txt) | Bitget / Bybit CDN / Gate / MEXC / Jupiter 等 |
| [source/overlays/Web3.txt](source/overlays/Web3.txt) | 钱包与 DEX（Rainbow / Phantom / GMGN / Tangem / Base / WalletConnect） |
| [source/overlays/AI.txt](source/overlays/AI.txt) | Cursor / Grok / xAI / Sora |
| [source/overlays/HBO.txt](source/overlays/HBO.txt) | HBO/Max 额外跟踪与播放域名 |
| `rule/Surge/Disneyplus.list` / `DisneyPlus_dl.list` | 本地 Disney+ 观看/登录，不同步覆盖 |

## 维护

```bash
python3 scripts/sync.py            # 全量
python3 scripts/sync.py --only AI  # 只同步名字匹配的
python3 scripts/validate.py
```

GitHub Actions：每周一 03:17 UTC 自动同步；也可在 Actions 里手动跑 Sync。

新增规则：在 `source/manifest.json` 加 `local` + `remote`（或多个 `remotes`）。纯本地集合只写 `overlay`。

## 声明

规则数据来自互联网开源项目（主要为 blackmatrix7），仅供学习研究。使用后果由使用者自行承担。

## Surge 规则迁移

已从个人 Surge `[Rule]` 迁移并筛查：

- 重复的 WhatsApp / Telegram / Discord / Reddit / Bybit / Rainbow / HBO 域名已去重
- `app-analytics-services.com` 只保留在 HBO overlay，不重复放入 Crypto
- Crypto 新增 Bybit / Bitget API、CDN、跟踪域名
- Web3 新增 Dexscreener
- AI 新增 Poe、Google OAuth / AI 相关域名
- 新增上游 Game、Epic、Apkpure、GitHub、Protonmail 规则
- 新增个人分类：`CustomProxy`、`CustomDirect`

个人规则：

| 集合 | 说明 | Clash | Surge |
| --- | --- | --- | --- |
| CustomProxy | zdassets、tamana、个人站点、Hostloc、Quora、Proton 辅助等代理规则 | [CustomProxy.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/CustomProxy.yaml) | [CustomProxy.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/CustomProxy.list) |
| CustomDirect | 自建节点 IP、国内服务、个人内网/直连域名 | [CustomDirect.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/CustomDirect.yaml) | [CustomDirect.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/CustomDirect.list) |
| Game | 游戏平台及相关服务 | [Game.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Game.yaml) | [Game.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Game.list) |
| GitHub | GitHub | [GitHub.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/GitHub.yaml) | [GitHub.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/GitHub.list) |
| Protonmail | Proton Mail | [Protonmail.yaml](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Clash/Protonmail.yaml) | [Protonmail.list](https://raw.githubusercontent.com/chentanwan/Config_Self/main/rule/Surge/Protonmail.list) |

Config_Self 主配置已接入这些新集合；Clash 使用 `🚀 手动切换` / `🎯 全球直连` / `🎮 游戏平台`，Surge 侧按对应策略组使用。
