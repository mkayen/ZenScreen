ZenScreen:
=========

Display Zendesk queues in Terminal and directly on desktop background.

Installation:
=========

Please install the script from this page, and save to a known location (ex. 'documents' folder)

ZenScreen uses the Zendesk Python API wrapper provided by Eventbrite. This must be installed prior to use, via pip. In terminal:

	pip install zendesk

If you do not have pip installed, please refer to the following link: http://www.pip-installer.org/en/latest/installing.html

Once the zendesk library is installed, please configure the script by running config.py in terminal, and answering all questions:

	cd documents/ZenScreen/code
	python config.py

Then please run the following command in terminal to confirm ZenScreen indeed works:

	python ZenScreen.py

Running this script should show you all support tickets in the views defined in Zendesk, and only supports two views at this time.

To view the script on your desktop background, so all ticket information is easily available, please use GeekTool. Download GeekTool from here: http://projects.tynsoe.org/en/geektool/

In Geektool, create a shell Geeklet, and input the directory of where the ZenScreen file is located.

	python /Users/userxyz/documents/ZenScreen/code/zenscreen.py

I would recommend having the sync interval set to 60 seconds.

Once this is complete, you are all set. If you have any questions, please email me at mkayen@gmail.com


