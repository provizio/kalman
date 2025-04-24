import os

from conan import ConanFile
from conan.tools.cmake import cmake_layout, CMakeToolchain, CMakeDeps, CMake

class ProvizioKalman(ConanFile):
    name = "kalman"
    license = "Provizio 2025 All Rights Reserved"
    author = "Ivan Fabek <ivan@provizio.ai>"
    url = "https://github.com/provizio/kalman"
    description = "Provizio+s private fork of kalman"
    topics = ("Provizio", "kalman")

    settings = "os", "compiler", "build_type", "arch"

    exports_sources = "conanfile.py", "CMakeLists.txt", "include/*", "cmake/*", "examples/*", "external/*", "test/*"

    package_type = "header-library"

    def requirements(self):
        self.requires("eigen/3.4.0")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.cache_variables["BUILD_TESTING"] = "OFF"
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []

