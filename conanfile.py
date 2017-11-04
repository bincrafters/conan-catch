#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class CatchConan(ConanFile):
    """Download Catch Cpp, build and create package
    """
    name = "Catch"
    version = "1.9.6"
    generators = "cmake"
    url = "https://github.com/bincrafters/conan-catch"
    license = "www.boost.org/LICENSE_1_0.txt"
    description = "A modern, C++-native, header-only, framework for unit-tests, TDD and BDD"

    def source(self):
        header_name = "catch.hpp"
        tools.download("https://github.com/philsquared/Catch/releases/download/v%s/%s" % (self.version, header_name), header_name)
        tools.check_md5(header_name, "6e3c2c7dd06d31ae9112b3816da24712")

    def package(self):
        self.copy(pattern="catch.hpp", dst="include")

    def package_id(self):
        self.info.header_only()
        