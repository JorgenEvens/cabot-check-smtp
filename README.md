# SMTP check for Cabot

## Install

First, install the plugin

```sh
pip install https://github.com/JorgenEvens/cabot-check-smtp/archive/master.zip
```

Next, enable it by adding it to the `CABOT_PLUGINS_ENABLED` environment variable.
```sh
export CABOT_PLUGINS_ENABLED=cabot_alert_email,cabot_alert_slack,cabot_check_smtp
```

## Usage

When creating a check, you can set a `host`, `port`, `sender` address and `recipient` address.

Sender and recipient address are optional. If set, the plugin will verify that email from `sender` to `recipient` is accepted by the mail server.
