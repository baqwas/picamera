#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  CaptureResizedImage.py
#	capture image in primary resolution and save to file at secondary resolution
#  
#  Copyright 2018 Matha Goram <baqwas@gmail.com>
#  
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
from picamera import PiCamera			# RPi camera module
import sys
from time import sleep

def CaptureResizedImage(argv):
	bound = lambda n, minn, maxn: max(min(maxn, n), minn) # utility function to clamp integer value range
		
										# command line parameter processing
	delay = 2							# warm-up time delay in seconds
	frate = 30							# framerate, frames per second
	ofile = "cap2resize.jpg"			# default output filename
	h1 = 1024							# horizontal resolution in pixels for camera
	v1 = 768							# veritical resolution in pixels for camera
	h2 = 1024							# horizontal resolution in pixels for image
	v2 = 768							# veritical resolution in pixels for image
	usage = "usage: CaptureResizedImage.py -o <output filename> -h <pixel> -w <pixel> -x <pixel> -y <pixel>"
	try:
										# argv: argument list to be parsed
										# option letters with colon suffix for mandatory parameter value (viz. i and o)
										# long_options with equal suffix for expected parameter value
		opts, args = getopt.getopt(argv, "d:f:h:?o:v:x:y:", ["delay=", "frate=", "help", "horz=" "ofile=", "vert=", "ximage=", "yimage="])
		for opt, arg in opts:
			if opt in ("-d", "--delay"):
				delay = int(arg)		# use intrinsic function
			elif opt in ("-f", "--frate"):
				frate = bound(int(arg), 1, 120)	# framerate in frames per second; extreme limits
			elif opt in ("-h", "--horz"):
				h1 = bound(int(arg), 1, 4096)	# horizonal resolution in pixels; needs bounds check, please
			elif opt == ("-?", "--help"):# help option keywords
				print(usage)
				sys.exit()				# exit without abend
			elif opt in ("-o", "--ofile"):
				ofile = arg
			elif opt in ("-v", "--vert"):
				v1 = bound(int(arg), 1, 4096) # vertical resolution in pixels; need bounds check, please
	except getopt.GetoptError:		# unrecognized option in the argument list
		print(usage)					# standard command line syntax
		sys.exit(1)						# invalid parameters specified when invoking program execution
										# camera work processing
	myCamera = PiCamera(resolution=(h1, v1), framerate=fmt)	# instantiate access to camera module overriding some parameters
	myCamera.resolution = (h1, v1)	# set (width, height) in pixels
	myCamera.start_preview()			# display preview overlay
	sleep(delay)						# Camera warm-up time
	myCamera.capture(ofile)				# capture image, store in specified filename per filetype format
	return 0

if __name__ == '__main__':
	sys.exit(CaptureResizedImage(sys.argv[1:]))
