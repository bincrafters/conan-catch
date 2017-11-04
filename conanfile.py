#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class CatchConan(ConanFile):
    name = "Catch"
    version = "2.0.1"
    generators = "cmake"
    url = "https://github.com/bincrafters/conan-catch"
    license = "www.boost.org/LICENSE_1_0.txt"
    description = "A modern, C++-native, header-only, framework for unit-tests, TDD and BDD"

    def source(self):
        header_name = "catch.hpp"
        tools.download("https://github.com/catchorg/Catch2/releases/download/v%s/%s" % (self.version, header_name), header_name)
        
    def package(self):
        self.copy(pattern="catch.hpp", dst="include")

    def package_id(self):
        self.info.header_only()
        