# Code written by Jack Clark
# Copyright 2017(c) the M.I.T. License
# This code is used to push a directory, or a file to an empty repository.
import sh
import os

class GitFunction(): 
	def pushToRepo(remote_address):
		os.system("")
	def verifyRemote(remote_address):
		os.system("git remote -v")
	def initializeRepository(remote_address):
		os.system("git init")
	def pull(remote_address):
		os.system("git pull" + remote_address)
	def push():
		os.system("git push -u origin master")
def pushFreshRepo(remote_url):
	GitFunction.initializeRepository(remote_url)
	GitFunction.verifyRemote(remote_url)
	GitFunction.pull(remote_url)
	GitFunction.push()

# For testing purposes
if __name__ == "__main__":
	remote_address_ = raw_input("Remote URL:")
