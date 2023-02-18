#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Created Date: 2023-02-18 21:29:20
# Author: WenWei
# -----
# Last Modified: 2023-02-18 22:06:32
# Modified By: WenWei
# -----
# Copyright (c) 2023 WenWei.
# 
# -----
# HISTORY:
# Date    /tBy	Comments
# ----------	---	----------------------------------------------------------
###
import ssl
import socket
from ConnectionBase import ConnectionBase
from logging import getLogger

class ConnectionTcp(ConnectionBase):
  def __init__(self, ipAddr, port = 9100, timeout = 2):
    self.logger = getLogger(__name__)
    self.ip = ipAddr
    self.port = port
    self.timeout = timeout
    super().__init__(self)
  
  def open(self):
    try:
      self.cnn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.cnn.settimeout(self.timeout)
      # self.cnn.setblocking(0)
      self.cnn.connect((self.ip, self.port))
      self.connection = True
    except Exception as e:
      self.logger.error("Init TCP connection to {}:{} error: {}".format(self.ip, self.port, str(e)))
      self.connection = False
    return self.connection

  def send(self, data):
      self.cnn.sendall(data)
      return

  def read(self, buffer_size=128):
      ret = b""
      try:
          ret = self.cnn.recv(buffer_size)
      except Exception as e:
          self.logger.info(f"Read data error:{str(e)}")
      return ret

  def readUntil(self, data, lastN = 64):
      loop = True
      buf = b""
      while loop:
          buf += self.read()
          if data in buf[-lastN:]:
            break
      return buf

  def close(self):
      self.cnn.close()
      super.close()
      return

class ConnectionSslTcp(ConnectionTcp):
  def __init__(self, ipAddr, port = 9100, timeout = 2):
    self.logger = getLogger(__name__)
    super.__init__(ipAddr, port, timeout)

  def open(self):
    try:
      self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.sock.settimeout(self.timeout)
      context = ssl._create_unverified_context(ssl.PROTOCOL_TLSv1_2)
      self.cnn = context.wrap_socket(self.sock)
      self.cnn.connect((self.ip, self.port))
      self.cnn.do_handshake();
      self.connection = True
    except Exception as e:
      self.logger.error("Init TCP connection to {}:{} error: {}".format(self.ip, self.port, str(e)))
      self.connection = False
    return self.connection

  def close(self):
    super.close()
    self.sock.close()