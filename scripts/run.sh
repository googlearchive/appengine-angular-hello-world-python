#!/bin/bash
#
set -uex

dev_appserver.py \
  --host 0.0.0.0 \
  --admin_host 0.0.0.0 \
  --skip_sdk_update_check yes \
  . $*
