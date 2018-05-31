# -*- coding: utf-8 -*-

"""Top-level package for ytree data worker."""

__author__ = """Matthew Turk"""
__email__ = 'matthewturk@gmail.com'
__version__ = '0.1.0'


from girder_worker import GirderWorkerPluginABC


class YtreeDataWorker(GirderWorkerPluginABC):
    def __init__(self, app, *args, **kwargs):
        self.app = app

    def task_imports(self):
        # Return a list of python importable paths to the
        # plugin's path directory
        return ['ytree_data_worker.tasks']
