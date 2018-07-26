#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  CaptureToStream.py
#  
#  Copyright 2018 Matha Goram <baqwas@gmail.com>
#
#	v0.1
#	2018-07-08
#	armw
#	initial version
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  Reference: https://picamera.readthedocs.io/en/release-1.13/api_camera.html
#
#  Acknowledgement: ALL code adapteed from PiCamera documentation referenced above

import getopt							# parse command line options
from io import BytesIO					# stream input/output operations
from picamera import PiCamera			# RPi camera module
import sys
from time import sleep

def CaptureToStream(argv):
	bound = lambda n, minn, maxn: max(min(maxn, n), minn)
		
										# command line parameter processing
	delay = 2							# warm-up time delay in seconds
	format = "jpeg"						# default capture file format
	usage = "usage: CaptureToStream.py -d <delay> -f <file format>"
	try:
										# argv: argument list to be parsed
										# option letters with colon suffix for mandatory parameter value (viz. i and o)
										# long_options with equal suffix for expected parameter value
		opts, args = getopt.getopt(argv, "d:f:h", ["delay=", "format=", "help"])
		for opt, arg in opts:
			if opt in ("-d", "--delay"):
				delay = int(arg)		# use intrinsic function
			elif opt in ("-f", "--format"):
				format = arg			# horizonal resolution in pixels; needs bounds check, please
			elif opt == ("-h", "--help"):# help option keywords
				print(usage)
				sys.exit()				# exit without abend
	except getopt.GetoptError:			# unrecognized option in the argument list
		print(usage)					# standard command line syntax
		sys.exit(1)						# invalid parameters specified when invoking program execution
										# camera work processing
	myStream = BytesIO()
	myCamera = PiCamera()				# instantiate access to camera module
	myCamera.start_preview()			# display preview overlay
	sleep(delay)						# Camera warm-up time
	myCamera.capture(myStream, format)	# capture stream using specified format
	return 0

if __name__ == '__main__':
	sys.exit(CaptureToStream(sys.argv[1:]))
