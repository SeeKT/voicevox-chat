# README
VOICEVOX と LLM (ELYZA) を組み合わせて簡易ボイスチャットボットを作ります。

## 前提
- VOICEVOX と LLM は別のサーバで動かすことを想定しているので、`docker-compose.yml` ファイルを分けています。


## Usage
### VOICEVOX Engine の起動

```
$ docker compose -f voicevox/docker-compose.yml up -d
```

`docker-compose.yml` 内の環境変数は `voicevox/.env` に記載する。

### サンプル
