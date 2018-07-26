#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  CaptureToFile.py
#	capture image to file
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
#  Reference
#  https://picamera.readthedocs.io/en/release-1.13/api_camera.html
#  Basic Recipes 3.1 Capturing to a file
#
#  Acknowledgement: ALL code adapteed from PiCamera documentation referenced above

import getopt							# parse command line options
from picamera import PiCamera			# RPi camera module
import sys
from time import sleep

def CaptureToFile(argv):
	bound = lambda n, minn, maxn: max(min(maxn, n), minn) # function to check on min/max bounds
		
										# command line parameter processing
	delay = 2							# warm-up time delay in seconds
	ofile = "../images/CaptureToFile.jpg"	# default output filename
	horz = 1024							# horizontal resolution in pixels
	vert = 768							# veritical resolution in pixels
	usage = "usage: CaptureToFile.py -o <output filename>"
	try:
										# argv: argument list to be parsed
										# option letters with colon suffix for mandatory parameter value (viz. i and o)
										# long_options with equal suffix for expected parameter value
		opts, args = getopt.getopt(argv, "d:h:?o:v:", ["delay=", "help", "horz=" "ofile=", "vert="])
		for opt, arg in opts:
			if opt in ("-d", "--delay"):
				delay = int(arg)		# use intrinsic function
			elif opt in ("-h", "--horz"):
				horz = bound(int(arg), 1, 4096)	# horizonal resolution in pixels; needs bounds check, please
			elif opt == ("-?", "--help"):# help option keywords
				print(usage)
				sys.exit()				# exit without abend
			elif opt in ("-o", "--ofile"):
				ofile = arg
			elif opt in ("-v", "--vert"):
				vert = bound(int(arg), 1, 4096) # vertical resolution in pixels; need bounds check, please
	except getopt.GetoptError:		# unrecognized option in the argument list
		print(usage)					# standard command line syntax
		sys.exit(1)						# invalid parameters specified when invoking program execution
										# camera work processing
	"""
	class:
		PiCamera
	parameters:
		camera_num=0
		stereo_mode='none'
		stereo_decimate=False
		resolution=None
		framerate=None
		sensor_mode=0
		led_pin=None
		clock_mode='reset'
		framerate_range=None
	"""
	completionCode = 0						# temporary use to avoid error log write operations
	try:
		myCamera = PiCamera()				# instantiate interface to camera module
		myCamera.resolution = (horz, vert)	# set (width, height) in pixels
		myCamera.start_preview()			# display preview overlay
		sleep(delay)						# Camera warm-up time
		"""
		method:
			capture
		parameters:
			output
			format
			use_video_port
			resize
			splitter_port
			bayer
			**options
		"""
		myCamera.capture(ofile)				# capture image, store in specified filename per filetype format
											# image not flipped since this is a generic exercise
	except picamera.PiCameraError:
		completionCode = -2					# further granularity avoided in this sample code
	except:
		completionCode = -1					# error external to PiCamera usage
	else:
		completionCode = 1					# sailed through
	finally:
		"""
		method:
			close
		parameters:
			none
		"""
		myCamera.close()					# good housekeeping
	return completionCode
if __name__ == '__main__':
	sys.exit(CaptureToFile(sys.argv[1:]))
