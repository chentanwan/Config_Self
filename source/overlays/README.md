# overlays

同步时合并进对应上游规则的本地补丁。格式与 Surge list 相同：

```
TYPE,value
```

在 `source/manifest.json` 里为规则指定 `"overlay": "source/overlays/Foo.txt"`。

- 只追加，不删除上游条目
- 与上游重复的行会被去重
- Clash YAML 会自动转成 `payload` 列表
