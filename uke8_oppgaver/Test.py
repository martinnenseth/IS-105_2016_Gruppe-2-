# -*- coding: utf-8 -*-
import unittest
import os
import Ica_05
from loremipsum import get_sentences
from random import randint


class TestFile(unittest.TestCase):
    def setUp(self) :
        needle = " Hello "                                  # The needle that is to be placed randomly inside the file
        self.inputFile = open('temp_InputFile.txt', 'w+')   # Create a test input file
        needle_pos = randint(1, 150)                        # Randomly set the position to the needle from 1,150
        sentences_list = get_sentences(4000)                # Create 4000 placeholder sentences

        pos = 0                                             # To keep track on where to put the needle
        for item in sentences_list:                         # Go trough sentence in the list
            if pos == needle_pos:                           # Check the pos, if pos = needle -> write needle.
                self.inputFile.write(needle)                # Write needle
            else:
                self.inputFile.write(item)                  # Write Sentence
            pos += 1                                        # plus the pos with 1 for each run

        self.inputFile.close()

    def testSlowAndFastEachWord(self):

        each_word = Ica_05.EachWord(                        # Create a object to test from
                'temp_InputFile.txt',                       # the temp file created earlier
                "Hello")                                    # The needle to look for

        self.assertGreaterEqual(                            # Check if the slow test is greater than the fast one
            each_word.run_test_slow(100),                   # Run the slow test 100 times
            each_word.run_test_fast(100))                   # run the fast test 100 times

        print "File size: " + str(os.path.getsize('temp_InputFile.txt'))

        os.remove('temp_InputFile.txt')                     # Delete the temp file 
