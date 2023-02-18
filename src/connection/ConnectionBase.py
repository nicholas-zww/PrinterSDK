#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Created Date: 2023-02-18 21:22:13
# Author: WenWei
# -----
# Last Modified: 2023-02-18 21:56:55
# Modified By: WenWei
# -----
# Copyright (c) 2023 WenWei.
# 
# -----
# HISTORY:
# Date    /tBy	Comments
# ----------	---	----------------------------------------------------------
###
from logging import getLogger

class ConnectionBase():
  def __init__(self):
    self.connection = False
    self.logger = getLogger(__name__)

  def open(self):
    return True
    
  def checkConnection(self):
    return self.connection

  def send(self, data):
    return

  def read(self, buffer_size=128):
    ret = ""
    return ret

  def readUntil(self, data, lastN = 64):
    ret = ""
    return ret

  def close(self):
    self.connection = False
    return