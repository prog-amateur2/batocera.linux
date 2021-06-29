#!/usr/bin/env python

import Command
from generators.Generator import Generator
import controllersConfig


class ECWolfGenerator(Generator):

    def generate(self, system, rom, playersControllers, gameResolution):
        commandArray = ["ecwolf", rom]
        return Command.Command(
            array=commandArray)

    def getMouseMode(self, config):
        return True