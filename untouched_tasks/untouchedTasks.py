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

from GTG import _
from GTG.tools.logger      import Log


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

    def deactivate(self, plugin_api):
        """
        Deactivates the plugin.
        """
        #everything should be removed, in case a task is currently opened
        try:
            self.plugin_api.remove_task_toolbar_item(self.tb_Taskbutton)
        except:
            pass

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
        if task.get_status() == "Active":
            tags = task.get_tags()
            Log.debug(tags)
            plugin_api.insert_tag("test")
            for tag in task.get_tags():
                Log.debug(tag)
                task.insert_tag("test")
                task.add_tag_attribute(tag_name,
                                       "location", marker_position)

#        numbers = [0,1,2,3,4,5,6,7,8]
#        for i in numbers:
#            i = str(i) + '@1'
#            blahdy = self.__req.get_task(i)
#            blah = blahdy.get_modified()
#            Log.debug('kadwilly')
#            Log.debug(blah)

