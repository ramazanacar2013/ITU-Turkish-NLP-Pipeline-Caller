#!/usr/bin/python3

import pipeline_caller
import unittest
import os

class Test(unittest.TestCase):

    def module_exception_test(self):
        try:
            caller = pipeline_caller.PipelineCaller('pipelineNoisy', 'test sentence', os.environ['pipeline_token'], 'whole')
            print(caller.call())
        except:
            self.fail('Exception thrown')
    
    def tool_exception_test(self):
        try:
            exec(open('./pipeline_caller.py').read())
        except:
            self.fail('Exception thrown')



if __name__ == '__main__':
    unittest.main()


