# -*- coding: utf-8 -*-
# Copyright (c) 2012 - Tom Kadwill <tomkadwill@gmail.com>
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.

import gio
import gtk
import urllib
import datetime

from GTG import _
from GTG.tools.logger import Log
from GTG.tools.dates import Date


class pluginUntouchedTasks:
    """
    The plugin.
    """

    def onTaskOpened(self, plugin_api):
        """
        Adds the button when a task is opened.
        """
        self.plugin_api = plugin_api
        # add a item (button) to the ToolBar
        tb_Taskicon = gtk.Image()
        tb_Taskicon.set_from_icon_name('mail-send', 32)

        self.tb_Taskbutton = gtk.ToolButton(tb_Taskicon)
        self.tb_Taskbutton.set_label(_("Untouched Tasks"))
        self.tb_Taskbutton.connect('clicked', self.onTbTaskButton, plugin_api)
        self.tb_Taskbutton.show_all()
	
        plugin_api.add_toolbar_item(self.tb_Taskbutton)

	#NOTE: get_textview() only works in this function
	# gets initializes textview to use for get_insert()
	self.textview = plugin_api.get_ui().get_textview()

    def deactivate(self, plugin_api):
        """
        Deactivates the plugin.
        """
        #everything should be removed, in case a task is currently opened
        try:
            self.plugin_api.remove_task_toolbar_item(self.tb_Taskbutton)
        except:
            pass

## HELPER FUNCTIONS ###########################################################
    def __log(self, message):
        Log.debug(message)

## CORE FUNCTIONS #############################################################
    def onTbTaskButton(self, widget, plugin_api):
        """
        When the user presses the button.
        """
        task = plugin_api.get_ui().get_task()
        Log.debug('tomkad')
        Log.debug(task)
        modified_time = task.get_modified()
        Log.debug(modified_time)
	yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
	Log.debug('yesterday')
	Log.debug(yesterday)
      
	self.delete_old_closed_tasks() #for testing delete_old_closed_tasks
	if modified_time > yesterday: # set to '>' to show it works but really should be '<' 
	    itera = self.textview.get_insert()
            if itera.starts_line():
                self.textview.insert_text("@untouched",itera)
            else:
                self.textview.insert_text(" @untouched",itera)
            self.textview.grab_focus()


	###BEFORE YOU DO THIS###
	#Get the current onTBTaskButton working
	#When you click button it should get all tasks and add @untouched
	#Then progress to adding @untouched if older than x days
    def delete_old_closed_tasks(self, widget = None):
        self.__log("Starting deletion of old tasks")
        today = Date.today()
        max_days = 30
        requester = self.plugin_api.get_requester()
        closed_tree = requester.get_tasks_tree(name = 'inactive')
        closed_tasks = [requester.get_task(tid) for tid in \
                        closed_tree.get_all_nodes()]
	for task in closed_tasks:
	    modified_time = task.get_modified()
	    self.__log(modified_time)
	    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
	    Log.debug('yesterday')
	    Log.debug(yesterday)
      
	    if modified_time > yesterday: # set to '>' to show it works but really should be '<' 
	    	itera = self.textview.get_insert()
            if itera.starts_line():
                self.textview.insert_text("@untouched",itera)
            else:
                self.textview.insert_text(" @untouched",itera)
            self.textview.grab_focus()

