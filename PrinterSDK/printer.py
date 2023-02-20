#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Created Date: 2023-02-16 21:46:32
# Author: WenWei
# -----
# Last Modified: 2023-02-16 21:49:01
# Modified By: WenWei
# -----
# Copyright (c) 2023 WenWei.
# 
# -----
# HISTORY:
# Date    /tBy	Comments
# ----------	---	----------------------------------------------------------
###

__printerList = [
  "RP2",
  "RP4",
  "PC45d",
  "PC45t",
]

def Supported_Printer_List():
  return ", ".join(__printerList)